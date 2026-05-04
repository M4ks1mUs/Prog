from tkinter import *

root = Tk()

root.title("Канбан-доска")
root.geometry("900x500")
root.minsize(900,500)
root.resizable(width = False, height = True)

def button():
    name = name_task.get()
    def click0():
        btn0.destroy()
        btn1.grid(column = 1)
    def click1():
        btn1.destroy()
        btn2.grid(column = 2)
    def click2():
        btn2.destroy()

    btn0 = Button(root, text = name,
             font = "Arial 10",
             width = 35,
             command = click0
             )
    btn1 = Button(root, text = name,
             font = "Arial 10",
             width = 35,
             command = click1
             )
    btn2 = Button(root, text = name,
             font = "Arial 10",
             width = 35,
             command = click2
             )
    btn0.grid(column = 0)


btn_task = Button(root, 
                text = "Создать новое задание", 
                command = button,
                font = "Arial 14",
                ).grid(row = 2, column = 1)


label_1 = Label(root, text = "Надо сделать", 
                font = "Arial 15", 
                bg = "red",
                width = 26,
                height = 2
                ).grid(row = 0, column = 0)
label_2 = Label(root, text = "В работе", 
                font = "Arial 15", 
                bg = "orange",
                width = 26,
                height = 2
                ).grid(row = 0, column = 1)
label_3 = Label(root, text = "Готово", 
                font = "Arial 15", 
                bg = "green",
                width = 26,
                height = 2
                ).grid(row = 0, column = 2)

name_task = Entry(root, font = "Arial 14")
name_task.grid(row = 1, column = 1)
root.grid_columnconfigure(0, minsize = 300)
root.grid_columnconfigure(1, minsize = 300)
root.grid_columnconfigure(2, minsize = 300)

root.mainloop()