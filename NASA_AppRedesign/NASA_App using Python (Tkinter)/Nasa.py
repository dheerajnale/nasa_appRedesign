from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import Entry,Tk
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser
root = Tk()
root.geometry("280x400")#widthxheight
root.configure(bg="white")
root.title("NASA")
root.minsize(280,400)#width,height
root.maxsize(280,400)

def msg():
    messagebox.showinfo("Message","You will be directed to next page!")

label1 = Label(text="Artemis Program", font="calibri 10", bg="white").place(x=90,y=250)

label2 = Label(text="Commercial Crew Program", font="calibri 10", bg="white").place(x=70,y=360)

img1 = ImageTk.PhotoImage(Image.open("search icon.png").resize((20, 20)))
Button1 = Button(image=img1, bg="white",borderwidth=0, highlightthickness=0, command = msg).place(x=230,y=7)

img2 = ImageTk.PhotoImage(Image.open("image1.png").resize((120, 80)))
Button2 = Button(image=img2, bg="white",borderwidth=0, highlightthickness=0, command = msg).place(x=80,y=170)

img3 = ImageTk.PhotoImage(Image.open("image2.png").resize((120, 80)))
Button3 = Button(image=img3, bg="white",borderwidth=0, highlightthickness=0, command = msg).place(x=80,y=282)

img4 = ImageTk.PhotoImage(Image.open("TV.png").resize((60,28)))
Button4 = Button(image=img4, bg="white",borderwidth=0, highlightthickness=0, command = msg).place(x=10,y=50)

def youtube():
    URL1="https://www.youtube.com/channel/UCLA_DiR1FfKNvjuUpBHmylQ"
    webbrowser.open_new_tab(URL1)

img5 = ImageTk.PhotoImage(Image.open("Video.png").resize((60,28)))
Button5 = Button(image=img5, bg="white",borderwidth=0, highlightthickness=0, command = youtube).place(x=80,y=50)

img6 = ImageTk.PhotoImage(Image.open("MSS1.png").resize((60,28)))
Button6 = Button(image=img6, bg="white",borderwidth=0, highlightthickness=0, command = msg).place(x=150,y=50)

def tweets():
    URL="https://twitter.com/NASA"
    webbrowser.open_new_tab(URL)

img7 = ImageTk.PhotoImage(Image.open("Tweets.png").resize((50,28)))
Button7 = Button(image=img7, bg="white",borderwidth=0, highlightthickness=0, command = tweets).place(x=220,y=50)

img12 = ImageTk.PhotoImage(Image.open("MSS.png").resize((190,28)))
Button12 = Button(image=img12, bg="white",borderwidth=0, highlightthickness=0, command = msg).place(x=10,y=83)

img8 = ImageTk.PhotoImage(Image.open("All.png").resize((55,25)))
Button8 = Button(image=img8, bg="white",borderwidth=0, highlightthickness=0, command = msg).place(x=10,y=120)

img9 = ImageTk.PhotoImage(Image.open("featured.png").resize((55,25)))
Button9 = Button(image=img9, bg="white",borderwidth=0, highlightthickness=0, command = msg).place(x=75,y=120)



img11 = ImageTk.PhotoImage(Image.open("Sightings.png").resize((55,25)))
Button11 = Button(image=img11, bg="white",borderwidth=0, highlightthickness=0, command = msg).place(x=205,y=120)

def scheduling():
    root1 = Toplevel(root)
    root1.geometry("280x400")#widthxheight
    root1.configure(bg="white")
    root1.title("NASA")
    root1.minsize(280,400)#width,height
    root1.maxsize(280,400)
    def msg():
        URL3="wwwwwwwwwwwwwwwwww"
        webbrowser(URL3)
    
    def msg():
        URL3="wwwwwwwwwwwwwwwwww"
        webbrowser(URL3)

    label1 = Button(root1,text="MISSIONS: Double Aesteroid Redirection Test(DART) Aesteroid Impact", font="calibri 7", bg="white", fg="#00a3e9", borderwidth=0, highlightthickness=0, command = msg)
    label1.place(x=7,y=150)
    
    label2 = Button(root1,text="MISSIONS: Artemis I", font="calibri 7", bg="white", fg="#00a3e9", borderwidth=0, highlightthickness=0, command = msg)
    label2.place(x=7,y=170)
    
    label3 = Button(root1,text="MISSIONS: NASA SpaceX Crew5 Mission to International Space Station", font="calibri 7", bg="white", fg="#00a3e9", borderwidth=0, highlightthickness=0, command = msg)
    label3.place(x=7,y=190)
    
    label4 = Button(root1,text="MISSIONS: Quesst", font="calibri 7", bg="white", fg="#00a3e9", borderwidth=0, highlightthickness=0, command = msg)
    label4.place(x=7,y=210)
    
    label5 = Button(root1,text="MISSIONS: JPSS-2", font="calibri 7", bg="white", fg="#00a3e9", borderwidth=0, highlightthickness=0, command = msg)
    label5.place(x=7,y=230)
    
    label6 = Button(root1,text="MISSIONS: Surface Water and Ocean Topology", font="calibri 7", bg="white", fg="#00a3e9", borderwidth=0, highlightthickness=0, command = msg)
    label6.place(x=7,y=250)
    
    label7 = Button(root1,text="MISSIONS: Intuitive Machines Commercial Payload Lunar Services", font="calibri 7", bg="white", fg="#00a3e9", borderwidth=0, highlightthickness=0, command = msg)
    label7.place(x=7,y=270)
    
    label8 = Button(root1,text="MISSIONS: Tropospheric Emissions Monitoring of Pollution (TEMPO)", font="calibri 7", bg="white", fg="#00a3e9", borderwidth=0, highlightthickness=0, command = msg)
    label8.place(x=7,y=290)
    
    label9 = Button(root1,text="MISSIONS: NASA's Boeing Crew Flight Test", font="calibri 7", bg="white", fg="#00a3e9", borderwidth=0, highlightthickness=0, command = msg)
    label9.place(x=7,y=310)
    
    label10 = Button(root1,text="MISSIONS: XRISM", font="calibri 7", bg="white", fg="#00a3e9", borderwidth=0, highlightthickness=0, command = msg)
    label10.place(x=7,y=330)
    
    label11 = Button(root1,text="MISSIONS: Lunar Trialblazer", font="calibri 7", bg="white", fg="#00a3e9", borderwidth=0, highlightthickness=0, command = msg)
    label11.place(x=7,y=350)


    img1 = ImageTk.PhotoImage(Image.open("search icon.png").resize((20, 20)))
    Button1 = Button(root1,image=img1, bg="white",borderwidth=0, highlightthickness=0, command = msg)
    Button1.image=img1
    Button1.place(x=230,y=7)

    img4 = ImageTk.PhotoImage(Image.open("TV.png").resize((60,28)))
    Button4 = Button(root1,image=img4, bg="white",borderwidth=0, highlightthickness=0, command = msg)
    Button4.image=img4
    Button4.place(x=10,y=50)

    def youtube():
        URL1="https://www.youtube.com/channel/UCLA_DiR1FfKNvjuUpBHmylQ"
        webbrowser.open_new_tab(URL1)

    img5 = ImageTk.PhotoImage(Image.open("Video.png").resize((60,28)))
    Button5 = Button(root1,image=img5, bg="white",borderwidth=0, highlightthickness=0, command = youtube)
    Button5.image=img5
    Button5.place(x=80,y=50)

    img6 = ImageTk.PhotoImage(Image.open("MSS1.png").resize((60,28)))
    Button6 = Button(root1,image=img6, bg="white",borderwidth=0, highlightthickness=0, command = msg)
    Button6.image=img6
    Button6.place(x=150,y=50)

    def tweets():
        URL="https://twitter.com/NASA"
        webbrowser.open_new_tab(URL)

    img7 = ImageTk.PhotoImage(Image.open("Tweets.png").resize((50,28)))
    Button7 = Button(root1,image=img7, bg="white",borderwidth=0, highlightthickness=0, command = tweets)
    Button7.image=img7
    Button7.place(x=220,y=50)

    img12 = ImageTk.PhotoImage(Image.open("MSS.png").resize((190,28)))
    Button12 = Button(root1,image=img12, bg="white",borderwidth=0, highlightthickness=0, command = msg)
    Button12.image=img12
    Button12.place(x=10,y=83)

    img8 = ImageTk.PhotoImage(Image.open("All.png").resize((55,25)))
    Button8 = Button(root1,image=img8, bg="white",borderwidth=0, highlightthickness=0, command = msg)
    Button8.image=img8
    Button8.place(x=10,y=120)

    img9 = ImageTk.PhotoImage(Image.open("featured.png").resize((55,25)))
    Button9 = Button(root1,image=img9, bg="white",borderwidth=0, highlightthickness=0, command = msg)
    Button9.image=img9
    Button9.place(x=75,y=120)

    img10 = ImageTk.PhotoImage(Image.open("scheduling.png").resize((55,25)))
    Button10 = Button(root1,image=img10, bg="white",borderwidth=0, highlightthickness=0, command = msg)
    Button10.image=img10
    Button10.place(x=140,y=120)

    img11 = ImageTk.PhotoImage(Image.open("Sightings.png").resize((55,25)))
    Button11 = Button(root1,image=img11, bg="white",borderwidth=0, highlightthickness=0, command = msg)
    Button11.image=img11
    Button11.place(x=205,y=120)

    #All labels
    heading = Label(root1, text="NASA",font=("calibri",14,"bold"),bg="White")
    heading.place(x=10, y=7)

heading = Label(root, text="NASA",font=("calibri",14,"bold"),bg="White")
heading.place(x=10, y=7)
img10 = ImageTk.PhotoImage(Image.open("scheduling.png").resize((55,25)))
Button10 = Button(image=img10, bg="white",borderwidth=0, highlightthickness=0, command = scheduling).place(x=140,y=120)

root.mainloop()