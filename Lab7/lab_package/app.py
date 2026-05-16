from tkinter import *
from palindrome import is_palindrom, is_palindrom_rec, get_x, get_x_rec
from logger import create_file_logger
from image_processor import find_color_in_image

root = Tk()
root.title("GUI Lab №4-6")
root.geometry("900x600")
root.resizable(width = False, height = False)

root.grid_columnconfigure(0, minsize = 300)
root.grid_columnconfigure(1, minsize = 300)
root.grid_columnconfigure(2, minsize = 300)

Label_4 = Label(root, text = 'Lab №4', 
                font = "Arial 15",
                width = 26,
                height = 2
                ).grid(row = 0, column = 0)
Label_palindrom = Label(root, text = "Проверка на палиндром:", 
                font = "Arial 15",
                width = 26,
                height = 2
                ).grid(row = 1, column = 0)
Label_get_x = Label(root, text = "Функция для вычисления\nx(i) = x(i-1) + x(i-3),\nx(1) = x(2) = x(3) = 1", 
                font = "Arial 15",
                width = 26,
                height = 4
                ).grid(row = 5, column = 0)
Label_5 = Label(root, text = 'Lab №5', 
                font = "Arial 15",
                width = 26,
                height = 2
                ).grid(row = 0, column = 1)
Label_logger = Label(root, text = "Запись значений в файл", 
                font = "Arial 15",
                width = 26,
                height = 2
                ).grid(row = 1, column = 1)
Label_6 = Label(root, text = 'Lab №6', 
                font = "Arial 15",
                width = 26,
                height = 2
                ).grid(row = 0, column = 2)
Label_image = Label(root, text = "Поиск цвета в изображении", 
                font = "Arial 15",
                width = 26,
                height = 2
                ).grid(row = 1, column = 2)

def button_4_palindrom():
    arg = Lab4_E_palindrom.get()
    res = is_palindrom(arg)
    if res == 1:
        res = "это палиндром"
    elif res == 0:
        res = "это не палиндром"
    Res_4_palindrom = Label(root, text = res, 
                font = "Arial 15",
                width = 26,
                height = 2
                ).grid(row = 4, column = 0)
def button_4_get_x():
    arg = Lab4_E_get_x.get()
    res = str(get_x(int(arg)))
    Res_4_get_x = Label(root, text = f'x_{arg} =' + res, 
                font = "Arial 15",
                width = 26,
                height = 2
                ).grid(row = 8, column = 0)
def button_5():
    arg = Lab5_E.get()
    res = create_file_logger('Lab7/text.txt')
    res(arg)
    Res_5 = Label(root, text = f'{arg}, записано в файл',
                font = "Arial 15",
                width = 26,
                height = 2
                ).grid(row = 4, column = 1)
def button_6():
    arg = Lab6_E.get().split(' ')
    res = find_color_in_image((int(arg[0]), int(arg[1]), int(arg[2])))
    Res_6 = Label(root, text = res,
                font = "Arial 15",
                width = 26,
                height = 4
                ).grid(row = 4, column = 2)

Lab4_E_palindrom = Entry(root, font = "Arial 14")
Lab4_E_get_x = Entry(root, font = "Arial 14")
Lab5_E = Entry(root, font = "Arial 14")
Lab6_E = Entry(root, font = "Arial 14")

Lab4_E_palindrom.grid(row = 2, column = 0)
Lab4_E_get_x.grid(row = 6, column = 0)
Lab5_E.grid(row = 2, column = 1)
Lab6_E.grid(row = 2, column = 2)

btn_lab4_palindrom = Button(root, 
                text = "pull", 
                command = button_4_palindrom,
                font = "Arial 14",
                ).grid(row = 3, column = 0)
btn_lab4_get_x = Button(root, 
                text = "pull", 
                command = button_4_get_x,
                font = "Arial 14",
                ).grid(row = 7, column = 0)
btn_lab5 = Button(root, 
                text = "записать", 
                command = button_5,
                font = "Arial 14",
                ).grid(row = 3, column = 1)
btn_lab6 = Button(root, 
                text = "поиск", 
                command = button_6,
                font = "Arial 14",
                ).grid(row = 3, column = 2)

root.mainloop()