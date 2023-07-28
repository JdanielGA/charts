import matplotlib.pyplot as plt

def generate_bar_chart(data_got):

    labes = list(data_got.keys())
    values = list(data_got.values())

    fig, ax = plt.subplots()
    ax.bar(labes, values)
    plt.show()

def generate_pie_chart(data_got):

    labes = list(data_got.keys())
    values = list(data_got.values())

    fig, ax = plt.subplots()
    ax.pie(values, labels=labes)
    ax.axis('equal')
    plt.show()