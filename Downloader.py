#An application for downloading videos and audios from YouTube

from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
import os
import pafy


def OK(event):
    url = videoEntry.get()
    try:
        video = pafy.new(url)   #Creating a url object through pafy for downloading
        name = titleEntry.get()
        path = pathEntry.get()
        origin = video.title
        flag = 1
        ext = " "
        
        if name ==  "":
            name = origin
            flag = 0
        if path ==  "":
            homedir = os.environ['HOME']   #Setting the current user as the environment
            path = homedir + "/Downloads"   #Default path is the Downloads folder

        if checkVar.get() == 0:
            showinfo("Message", "Video will be downloaded in a few moments...")
            best = video.getbest()   #Getting the best available quality of video
            ext = best.extension
            best.download(path)
        else:
            bestaudio = video.getbestaudio()   #Getting the best available quality of audio
            showinfo("Message", "Audio will be downloaded in a few moments...")
            ext = bestaudio.extension
            bestaudio.download(path)
        if flag == 1:
            os.rename((path + "/" + origin + "." + ext), (path + "/" + name + "." + ext))   #Renaming the file
        showinfo("Message", "Download Completed")
    except Exception as e:
        showerror("Error", e)
        

def fileTray():
    tray = askdirectory(parent = root, title = "Choose folder")
    pathEntry.delete(0, END)
    pathEntry.insert(0, tray)



#GUI of the program:

root = Tk()
root.geometry("500x370+0+0")
root.wm_title("Video & Audio Downloader")

videoLabel = Label(text = "Enter URL of video here:")
pathLabel = Label(text = "Enter path for storing videos:")
titleLabel = Label(text = "Enter name for the video:")
okButton = Button(text = "OK")
videoEntry = Entry(root)
pathEntry = Entry(root)
titleEntry = Entry(root)
menu = Menu(root)
root.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Open... ", command = fileTray)
filemenu.add_command(label = "Quit", command = root.quit)
checkVar = IntVar()   #Check variable for toggling the checkbox
audioButton = Checkbutton(text = "Extract only audio", variable = checkVar, onvalue = 1, offvalue = 0)

videoLabel.place(x = 40, y = 30)
pathLabel.place(x = 40, y = 100)
titleLabel.place(x = 40, y = 170)
videoEntry.place(x = 250, y = 30)
pathEntry.place(x = 250, y = 100)
titleEntry.place(x = 250, y = 170)
okButton.place(x = 120, y = 240)
audioButton.place(x = 250, y = 240)

okButton.bind("<Button-1>", OK)

root.mainloop()


