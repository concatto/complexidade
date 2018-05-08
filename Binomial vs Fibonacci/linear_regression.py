import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import itertools
from matplotlib import style
from statistics import mean
import matplotlib.lines as mlines

def process(dataset):
    result = list()

    for k, g in itertools.groupby(dataset, lambda v: v[1]):
        #print(k)
        values = np.array(list(g))
        full = np.int32(values[:, 2])
        last = np.int32(values[:, 3])

        row = [(int(k)), np.mean(full), np.max(full), np.mean(last), np.max(last)];
        #print(row)
        result.append(row)

    return np.array(result)

def linear_regression(xs,ys,label):
    m = ((mean(xs)* mean(ys)) - mean(xs*ys)) / ( (mean(xs)**2) - (mean(xs**2)) )
    b = mean(ys) - m*mean(xs)
    regression_line = [(m*x)+b for x in xs]
    plt.scatter(xs,ys,s=1, color='r')
    legenda = mlines.Line2D([], [], color='blue',markersize=15, label=label)
    plt.legend(handles=[legenda])
    plt.plot(xs, regression_line)
    plt.show()

with open("experiments.csv", "r") as output:
    reader = csv.reader(output, delimiter=",");

    data = list(reader)
    binomial_raw = [val for val in data if val[0] == "binomial"]
    fibonacci_raw = [val for val in data if val[0] == "fibonacci"]

    binomial = process(binomial_raw);
    fibonacci = process(fibonacci_raw);

    binomial_y_full = [y for y in binomial[:,1]]
    binomial_y_full_m = [y for y in binomial[:,2]]
    binomial_y_last = [y for y in binomial[:,3]]
    binomial_y_last_m = [y for y in binomial[:,4]]
    binomial_x = [x for x in binomial[:,0]]
    linear_regression(np.array(binomial_x, dtype=np.float64),np.array(binomial_y_full, dtype=np.float64),"Binomial Full Média")
    linear_regression(np.array(binomial_x, dtype=np.float64),np.array(binomial_y_full_m, dtype=np.float64),"Binomial Full Máximo")
    linear_regression(np.array(binomial_x, dtype=np.float64),np.array(binomial_y_last, dtype=np.float64),"Binomial Last Média")
    linear_regression(np.array(binomial_x, dtype=np.float64),np.array(binomial_y_last_m, dtype=np.float64),"Binomial Last Máximo")

    fibonacci_y_full = [y for y in fibonacci[:,1]]
    fibonacci_y_full_m = [y for y in fibonacci[:,2]]
    fibonacci_y_last = [y for y in fibonacci[:,3]]
    fibonacci_y_last_m = [y for y in fibonacci[:,4]]
    fibonacci_x = [x for x in fibonacci[:,0]]
    linear_regression(np.array(fibonacci_x, dtype=np.float64),np.array(fibonacci_y_full, dtype=np.float64),"Fibonacci Full Média")
    linear_regression(np.array(fibonacci_x, dtype=np.float64),np.array(fibonacci_y_full_m, dtype=np.float64),"Fibonacci Full Máximo")
    linear_regression(np.array(fibonacci_x, dtype=np.float64),np.array(fibonacci_y_last, dtype=np.float64),"Fibonacci Last Média")
    linear_regression(np.array(fibonacci_x, dtype=np.float64),np.array(fibonacci_y_last_m, dtype=np.float64),"Fibonacci Last Máximo")
