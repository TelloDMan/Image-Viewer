from fileinput import filename
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
"""
Import all this into a class to eliminate memory issues
such as importing 400 images will take alot to load in a list
in line:60
"""

main = Tk()
main.title('Image selection')
main.state('zoomed')

heightt = main.winfo_screenheight()
widthh = main.winfo_screenwidth()

frame_image = Frame()
frame_image.configure(height=int((heightt*2)/2.24), width=widthh)
frame_image.pack_propagate(0)

filename2 = []
indexer = 0
image = Label()


def resizer(open_image):
      
    img=ImageTk.PhotoImage(open_image)
    
    img_h = img.height()
    img_w = img.width()
    if img_h > heightt or img_w > widthh:
        while img_h > heightt-200:
            img_h/=1.001
            img_w/=1.001
    open_image = open_image.resize((int(img_w), int(img_h)), Image.ANTIALIAS)
    
    return open_image


def open_images():
#main.file = filedialog.askdirectory(initialdir="This PC", title="Select The USB")
    global filename2
    global indexer
    global btn_bak
    global btn_for
    
    btn_bak.grid_forget()
    btn_for.grid_forget()
    
    btn_for = Button(main, text=">>>", command=plus)
    btn_bak = Button(main, text="<<<", command=minus, state=DISABLED) 

    indexer = 0
    filename2 = []
    
    filename1 = filedialog.askopenfilenames(initialdir="E:\menyeke", title="Select A File", filetypes=(("jpg files", "*.jpg"),("png files", "*.png"),("all files", "*.*")))
    filename2 = list(filename1)
    filename2 = list(map(lambda x: ImageTk.PhotoImage(resizer(Image.open(x))), filename2))
    
    if len(filename2) == 1 or len(filename2) == 0:
        btn_for = Button(main, text=">>>", command=plus, state=DISABLED)
        btn_bak = Button(main, text="<<<", command=minus, state=DISABLED)   
            
    btn_for.grid(row=2, column=1, sticky="WE")
    btn_bak.grid(row=2, column=0, sticky="WE") 
    
    viewer()


def plus():
    global indexer
    global btn_bak
    global btn_for
    
    btn_bak.grid_forget()
    btn_for.grid_forget()
    
    indexer += 1
    btn_for = Button(main, text=">>>", command=plus)
    btn_bak = Button(main, text="<<<", command=minus)
    if indexer+1 == len(filename2):
        btn_for = Button(main, text=">>>", command=plus, state=DISABLED) 
    viewer() 
    btn_for.grid(row=2, column=1, sticky="EW") 
    btn_bak.grid(row=2, column=0, sticky="EW")
        
     
def minus():
    global indexer
    global btn_bak
    global btn_for
    
    btn_bak.grid_forget()
    btn_for.grid_forget()
    
    indexer -= 1
    viewer()
    btn_for = Button(main, text=">>>", command=plus)
    btn_bak = Button(main, text="<<<", command=minus)
    if indexer == 0:
        btn_bak = Button(main, text="<<<", command=minus, state=DISABLED)
    btn_bak.grid(row=2, column=0, sticky="EW")
    btn_for.grid(row=2, column=1, sticky="EW") 
    
    
def viewer():
    global filename2
    global indexer
    global image
    
    image.pack_forget()
    image = Label(frame_image, image=filename2[indexer])
    image.pack(anchor=CENTER, pady=50)
    
    

btn = Button(main, text="click", command=open_images)
btn_for = Button(main, text=">>>", command=plus)
btn_bak = Button(main, text="<<<", command=minus, state=DISABLED)

btn.grid(row=0, column=0, columnspan=2, sticky="EW")
btn_for.grid(row=2, column=1, sticky="EW")
btn_bak.grid(row=2, column=0, sticky="EW")
frame_image.grid(row=1, column=0,columnspan=2)


main.mainloop()






