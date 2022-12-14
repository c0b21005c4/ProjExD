import tkinter as tk
import tkinter.messagebox as tkm
from math import *

def button_click(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END,num)

def equal(event):
    siki = entry.get()
    root_list = []
    for i in range(0,len(siki)):
        if "√" in siki[i]:
            root_list.append((i,sqrt(int(siki[i+1]))))
    num = 0
    if root_list != []:
        for ind,val in root_list:
            siki = siki.replace(f"{siki[ind-num:ind+2-num]}",str(val))
            num += 1

    ans = eval(siki)
    entry.delete(0,tk.END)
    entry.insert(tk.END,ans)

def c_click(event):
    entry.delete(0,tk.END)

root = tk.Tk()
root.title("電卓")
root.geometry("380x500")

entry = tk.Entry(root, width=10,font=("Times New Roman",40),justify="right")
entry.grid(column=0,row=0,columnspan=10)


num = 9
for i in range(4):
    for j in range(3):
        button = tk.Button(root,text=f"{num}",height=1,width=4,font=("Times New Roman", 30))
        button.bind("<1>",button_click)
        if num >= 0:
            button.grid(column=j+1,row=i+2)
            num -= 1

button_mark = {"+":(4,4),"-":(4,3),"*":(4,2),"/":(4,1),"**2":(3,1),"√":(2,1)}
for key,val in button_mark.items():
    button = tk.Button(root,text=key,height=1,width=4,font=("Times New Roman", 30))
    button.bind("<1>",button_click)
    button.grid(column=val[0],row=val[1])

button = tk.Button(root,text="=",height=1,width=4,font=("Times New Roman", 30),bg="gray")
button.bind("<1>",equal)
button.grid(column=4,row=5)

button = tk.Button(root,text="c",height=1,width=4,font=("Times New Roman", 30),bg="blue")
button.bind("<1>",c_click)
button.grid(column=1,row=1)

root.mainloop()