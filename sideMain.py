import math
import tkinter as tk
from tkinter import ttk

k = 12


def nCalc(a, b):
    n = math.ceil((((k * ((b - a) ** 2)) / (180 * (5 * 10 ** -11)))) ** (1 / 4))
    if n % 2 == 0:
        return n
    else:
        return n + 1


def dxCalc(a, b, n):
    return (b - a) / n


def coefficientEval(intervals):
    coef = []
    # make sure interval number is even for Simpson rule
    if intervals % 2 == 0:
        for x in range(intervals + 1):
            if x == 0:
                coef.append(1)
            elif x == intervals:
                coef.append(1)
            elif (x % 2) == 1:
                coef.append(4)
            elif (x % 2) == 0:
                coef.append(2)
        return coef
    else:
        return "Please use an even n value"


def nSummation(delta, coefList):
    partialSum = 0
    for nthValue in range(len(coefList)):
        partialSum += pow(math.e, ((-pow((nthValue * delta), 2)) / 2)) * coefList[nthValue]
    return partialSum


def phi(zScore):
    if zScore == 0:
        return 0.5  # hardcoded case of 0, to avoid division by 0
    else:
        coefList = coefficientEval(nCalc(0, zScore))
        nSum = nSummation(dxCalc(0, zScore, nCalc(0, zScore)), coefList)
        return round((1 / 2) * (1 + (math.sqrt(2 / math.pi)) * (nSum * (dxCalc(0, zScore, nCalc(0, zScore)) / 3))), 4)


def generateZScoreTable():
    table = []
    #
    for i in range(-34, 35):
        row = []
        for j in range(10):
            z = (i / 10) + (j / 100)
            row.append(phi(z))
        table.append(row)
    return table


#
def displayZScoreTable():

    window = tk.Tk()
    window.title("Z-Score Table")


    zScoreTable = generateZScoreTable()


    columns = ['Z-Score'] + [f'{i / 100:.2f}' for i in range(10)]  # e.g., 0.00 to 0.09


    tree = ttk.Treeview(window, columns=columns, show='headings')


    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)


    for i, row in enumerate(zScoreTable):

        zValue = -3.4 + (i / 10)
        tree.insert("", "end", values=[f'{zValue:.2f}'] + row)


    tree.pack(expand=True, fill="both")


    window.mainloop()



displayZScoreTable()
