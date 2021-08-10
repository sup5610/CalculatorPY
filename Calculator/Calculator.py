from tkinter import *
txt = ""
i = 0

def split(w):
    return [char for char in w]

def insert(a):
    hud.insert(99999, a)

def key(a,k,x,y):
    a = Button(root)
    a.config(text = str(k), command = lambda :insert(str(k)), width = 5, height = 5)
    a.grid(column = x, row = y)

def d():
    x = ""
    txt = hud.get()
    i = int(len(txt))
    txt = split(txt)
    txt.pop(-1)
    for i in txt:
        x = x + txt[i]
        i += 1
    txt = x
    print(txt)
    hud.delete(0, END)
    hud.insert(0, txt)


root = Tk()
root.title("Calculator")
root.geometry("300x500")

hud = Entry(root)
hud.config(state = NORMAL, width = 15)
hud.grid(columnspan = 3, column = 0, row = 0)

key("k1",1,0,1)
key("k2",2,1,1)
key("k3",3,2,1)
key("k4",4,0,2)
key("k5",5,1,2)
key("k6",6,2,2)
key("k7",7,0,3)
key("k8",8,1,3)
key("k9",9,2,3)
key("k0",0,1,4)

delete = Button(root)
delete.config(text = "Del", command = lambda :d(), width = 5, height = 5)
delete.grid(column = 2, row = 4)


root.mainloop()