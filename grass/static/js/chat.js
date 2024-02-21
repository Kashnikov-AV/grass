const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);
const receiver = JSON.parse(document.getElementById('json-username-receiver').textContent);
const room = JSON.parse(document.getElementById('json-room').textContent);

console.log(id);


const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + id
    + '/'
);

socket.onopen = function(e){
    console.log("CONNECTION ESTABLISHED");
}

socket.onclose = function(e){
    console.log("CONNECTION LOST");
}

socket.onerror = function(e){
    console.log("ERROR OCCURED");
}

socket.onmessage = function(e){
    const data = JSON.parse(e.data);
    console.log(data);
    const d = new Date();
    let minutes = d.getMinutes();
	if (minutes < 10) {minutes = "0" + minutes}
    let hours = d.getHours();
	if (hours < 10) {hours = "0" + hours}
    if(data.username == message_username){
        document.querySelector('#chat-body').innerHTML += `<div class="message-area__my-flex">
                                                                <div class="message-area__my-text">
                                                                    <p class="message-area__message">${data.message}</p>
                                                                    <p class="message-area__time">${hours}:${minutes}</p>
                                                                </div>
                                                            </div>`
    }else{
        document.querySelector('#chat-body').innerHTML += `<div class="message-area__my-flex">
                                                                <div class="message-area__other-text">
                                                                    <p class="message-area__message">${data.message}</p>
                                                                    <p class="message-area__time">${hours}:${minutes}</p>
                                                                </div>
                                                            </div>`
    }
}

document.querySelector('#chat-message-submit').onclick = function(e){
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;

    socket.send(JSON.stringify({
        'message':message,
        'username':message_username,
        'receiver':receiver
    }));

    message_input.value = '';
}

const messageInput = JSON.parse(JSON.stringify(document.getElementById('message_input')));

messageInput.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        
        event.preventDefault();
        
       const message = messageInput.value.trim();

       if(message !== ''){
            socket.send(JSON.stringify({
                'message' : message,
                'username' : message_username,
                'receiver':receiver
            }))

            messageInput.value = '';
       }
    }
});