import tkinter as tk

root = tk.Tk()
root.geometry("250x250")
result = ""
def f1():
    global result
    result += "1"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def f2():
    global result
    result += "2"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def f3():
    global result
    result += "3"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def f4():
    global result
    result += "4"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def f5():
    global result
    result += "5"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def f6():
    global result
    result += "6"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def f7():
    global result
    result += "7"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def f8():
    global result
    result += "8"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def f9():
    global result
    result += "9"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def f0():
    global result
    result += "0"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def fp():
    global result
    result += "+"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def fm():
    global result
    result += "-"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def fd():
    global result
    result += "/"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def fmul():
    global result
    result += "*"
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def fres():
    global result
    resultEntry.delete(0, tk.END)
    re = str(eval(result))
    resultEntry.insert(1 ,re)
    result = re
def fc():
    global result
    result = result[:-1]
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)
def fca():
    global result
    result = ""
    resultEntry.delete(0, tk.END)
    resultEntry.insert(1, result)



resultEntry = tk.Entry()
n1 = tk.Button(text="1", command=f1)
n2 = tk.Button(text="2", command=f2)
n3 = tk.Button(text="3", command=f3)
n4 = tk.Button(text="4", command=f4)
n5 = tk.Button(text="5", command=f5)
n6 = tk.Button(text="6", command=f6)
n7 = tk.Button(text="7", command=f7)
n8 = tk.Button(text="8", command=f8)
n9 = tk.Button(text="9", command=f9)
n0 = tk.Button(text="0", command=f0)
bp = tk.Button(text="+", command=fp)
bm = tk.Button(text="-", command=fm)
bd = tk.Button(text="/", command=fd)
bmul = tk.Button(text="*", command=fmul)
bres = tk.Button(text="=", command=fres)
bclr = tk.Button(text="c", command=fc)
bclra = tk.Button(text="ca", command=fca)



#GRID
resultEntry.grid(columnspan=4, row=0)
n1.grid(column=0, row=1)
n2.grid(column=1, row=1)
n3.grid(column=2, row=1)
n4.grid(column=0, row=2)
n5.grid(column=1, row=2)
n6.grid(column=2, row=2)
n7.grid(column=0, row=3)
n8.grid(column=1, row=3)
n9.grid(column=2, row=3)
bp.grid(column=3, row=1)
bm.grid(column=3, row=2)
bd.grid(column=3, row=3)
bmul.grid(column=3, row=4)
bres.grid(column=0, row=5)
bclr.grid(column=1, row=5)
bclra.grid(column=2, row=5)


n0.grid(columnspan=3, row=4)
#CONFIG
n0.config(width=10)


root.mainloop()
