from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import webbrowser

root = Tk()
root.title("Simple HTML Editor")
root.maxsize(650,650)
root.minsize(650,650)
root.configure(background="gray")

save_img = ImageTk.PhotoImage(Image.open("save.png"))
open_img = ImageTk.PhotoImage(Image.open("file.png"))
run_img = ImageTk.PhotoImage(Image.open("run.png"))

label_filename = Label(root, text = "File Name: ")
label_filename.place(relx=0.28, rely=0.03, anchor=CENTER)

input_filename = Entry(root)
input_filename.place(relx=0.46, rely=0.03, anchor=CENTER)

html_code = Text(root, bg = "black", fg = "white", height = 35, width = 80)
html_code.place(relx=0.5, rely=0.55, anchor=CENTER)

name = ""

def openFile():
    global name
    html_code.delete(1.0, END)
    input_filename.delete(0, END)
    html_file = filedialog.askopenfilename(title="Open HTML File", filetypes=(("HTML Files","*.html"),))
    print(html_file)
    name = os.path.basename(html_file)
    formatted_name = name.split('.')[0]
    input_filename.insert(END, formatted_name)
    root.title(formatted_name)
    html_file = open(name, 'r')
    paragraph = html_file.read()
    html_code.insert(END, paragraph)
    html_file.close()
    
def saveFile():
    input_name = input_filename.get()
    file = open(input_name+".html", "w")
    data = html_code.get("1.0",END)
    print(data)
    file.write(data)
    input_filename.delete(0,END)
    html_code.delete(1.0,END)
    messagebox.showinfo("Success","Success")
    
def runFile():
    global name
    webbrowser.open(name)
    webbrowser.open_new('file://' + file_path)
    
open_btn = Button(root, image = open_img, text = "Open File", command = openFile)
open_btn.place(relx=0.05, rely=0.03, anchor=CENTER)
save_btn = Button(root, image = save_img, text = "Save File", command = saveFile)
save_btn.place(relx=0.11, rely=0.03, anchor=CENTER)
run_btn = Button(root, image = run_img, text = "Run File", command = runFile)
run_btn.place(relx=0.17, rely=0.03, anchor=CENTER)

root.mainloop()