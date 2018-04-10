import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import itertools

def process(dataset):
    result = list()

    for k, g in itertools.groupby(dataset, lambda v: v[1]):
        print(k)
        values = np.array(list(g))
        full = np.int32(values[:, 2])
        last = np.int32(values[:, 3])
        
        row = [(int(k)), np.mean(full), np.max(full), np.mean(last), np.max(last)];
        print(row)
        result.append(row)

    return np.array(result)


def plot_one(binomial, fibonacci):
    fig, ax = plt.subplots()

    ax.plot(binomial[:, 0], binomial[:, 4], label="Binomial") 
    ax.plot(fibonacci[:, 0], fibonacci[:, 4], label="Fibonacci")
#    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda a, b: r"$2^{%d}$" % a))
    ax.set(xlabel="Qtd. elementos", ylabel="Tempo (ns)", title="Inserção de um elemento")

    ax.legend(loc="upper right")
    ax.grid()
    plt.show()


def plot_multiple(binomial, fibonacci):
    fig, ax = plt.subplots()

    ax.plot(binomial[:, 0], binomial[:, 2], label="Binomial") 
    ax.plot(fibonacci[:, 0], fibonacci[:, 2], label="Fibonacci")
#    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda a, b: r"$2^{%d}$" % a))
    
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda a, b: r"%d" % (a / 1000000)))
#    ax.set_yscale("log")
    ax.set(xlabel="Elementos inseridos", ylabel="Tempo (ms)", title="Inserção de múltiplos elementos")

    ax.legend(loc="lower right")
    ax.grid()
    plt.show()




with open("experiments.csv", "r") as output:
    reader = csv.reader(output, delimiter=",");

    data = list(reader)
    binomial_raw = [val for val in data if val[0] == "binomial"]
    fibonacci_raw = [val for val in data if val[0] == "fibonacci"]

    binomial = process(binomial_raw);
    fibonacci = process(fibonacci_raw);

    plot_one(binomial, fibonacci)
    plot_multiple(binomial, fibonacci)



