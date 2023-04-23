from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, password_validation
from django import forms


ROLE_CHOICES =(
    (False, "Работник"),
    (True, "Работодатель"),
)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='E-mail',
        label_suffix='',
        widget=forms.EmailInput(attrs={
            "class": "input_item",
            "type": "email",
            "placeholder": "Электронная почта",
        }
        ))

    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "class": "input_item",
            "type": "password",
            "placeholder": "Пароль",
        }),
        help_text=password_validation.password_validators_help_text_html(),
        label_suffix="",
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "class": "input_item",
            "type": "password",
            "placeholder": "Повторите пароль",
        }),
        strip=False,
        help_text="Enter the same password as before, for verification.",
        label_suffix="",
    )

    role = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        label="",
        choices=((0, 'Ищу работу'), (1, 'Ищу сотрудника')),
        widget=forms.RadioSelect(attrs={
            "class": "btn btn-default"
        })
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'role')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='E-mail',
        label_suffix='',
        widget=forms.EmailInput(attrs={
            "class": "input is-primary",
            "type": "email",
            "placeholder": "Электронная почта",
        }
        ))

    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "class": "input is-primary",
            "type": "password",
            "placeholder": "Пароль",
        }),
        help_text=password_validation.password_validators_help_text_html(),
        label_suffix="",
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'password',)

