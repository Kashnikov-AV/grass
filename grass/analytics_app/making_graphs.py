import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imange_png = buffer.getvalue()
    graph = base64.b64encode(imange_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph

def get_plot():

    f = open('C:\\Users\\User\PycharmProjects\grass\grass\static\csv\jobibi.txt')
    df = pd.read_csv(f, sep=',', encoding='utf-8')
    plt.style.use('fivethirtyeight')
    a = df['Вакансия'].value_counts()
    a = a[:10]
    y = list(a.keys())
    ax = plt.bar(y, a)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Вакансии')
    plt.ylabel('Востребованность')
    graph = get_graph()
    return graph