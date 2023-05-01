from pygame import mixer
from time import sleep
from tkinter import *
import threading
from PIL import ImageTk,Image

flag = threading.Event()
flag1 = threading.Event()

def SleepTimer(LabelVar,minut=0):
    for minute in range(minut,0,-1):
        if flag1.is_set():
            LabelVar.set("time: 00:00")
            flag1.clear()
            break
        for second in range(59,0,-1):
            flag.wait()
            if flag1.is_set():
                break
            sleep(1)
            LabelVar.set(f"time: {minute-1}:{second}")

def timer(restEntry,workEntry,cyclesEntry,LabelVar):
    while(True):
        flag.wait()
        rest = int(restEntry.get())
        work = int(workEntry.get())
        cycles = int(cyclesEntry.get())
        for main in range(cycles):
            if flag1.is_set():
                break
            for workw in range(work):
                SleepTimer(LabelVar,minut=work)
            mixer.music.play()
            for restd in range(rest):
                SleepTimer(LabelVar,minut=rest)
            mixer.music.play()
            flag.clear()

class GUI():
    def __init__(self, master):
        self.master = master
        self.master.title("Timer")
        self.master.geometry("320x160")
        self.master.resizable(False,False)

        mixer.init()
        mixer.music.load("sound.mp3")

        menubar = Menu(master)
        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="info", command=self.open_infoWindow)
        menubar.add_cascade(label="File", menu=fileMenu)
        master.config(menu=menubar)

        TimeFrame = Frame(self.master)
        EntryLabelFrame = Frame(self.master)
        EntryFrame = Frame(EntryLabelFrame)
        LabelFrame = Frame(EntryLabelFrame)
        ButtonFrame = Frame(self.master)
        
        ButtonStart = Button(ButtonFrame,text="Start", command=flag.set)
        ButtonClear = Button(ButtonFrame,text="Clear", command=flag1.set)
        ButtonStop = Button(ButtonFrame,text="Stop",command=flag.clear)
        phantomImage = ImageTk.PhotoImage(Image.new("RGB", (1,1), (0,0,1)))
        LabelLine = Label(TimeFrame, image=phantomImage,bg="black", width=280, height=1)
        LabelVar = StringVar(value="time: 00:00")
        LabelWork = Label(LabelFrame, text="work time")
        LabelRest = Label(LabelFrame, text="rest time")
        LabelCycle = Label(LabelFrame, text="cycle")
        
        workEntry = Entry(EntryFrame)
        restEntry = Entry(EntryFrame)
        cyclesEntry = Entry(EntryFrame)
        LabelTimer = Label(TimeFrame,textvariable=LabelVar)

        TimeFrame.pack(side="top")
        EntryLabelFrame.pack(side="top")
        EntryFrame.pack(side="right")
        LabelFrame.pack(side="left")
        ButtonFrame.pack(side="bottom")
        LabelTimer.pack(side="top")
        LabelLine.pack(side="bottom")
        LabelWork.pack(side="bottom")
        LabelRest.pack(side="bottom")
        LabelCycle.pack(side="bottom")
        cyclesEntry.pack(side="bottom")
        restEntry.pack(side="bottom")
        workEntry.pack(side="bottom")
        ButtonStart.pack(side="right", padx=10, pady=10)
        ButtonClear.pack(side="left", padx=10, pady=10)
        ButtonStop.pack(side="left", padx=10, pady=10)

        target1 = threading.Thread(target=timer,daemon=True, args=[workEntry,restEntry,cyclesEntry,LabelVar])
        target1.start()

        self.master.mainloop()

    def open_infoWindow(self,width=400,height=100):
        window = Toplevel(self.master)
        window.title("Info window")
        window.geometry('{}x{}'.format(width,height))
        window.resizable(False,False)

        LabelInfo = Label(window, text="Is program writing is EternalSlow. If my program caused an error, \nthen write to this email: \nnikslastd@gmail.com")
        ButtonClose = Button(window,text="close window", command=window.destroy)
        LabelInfo.pack()
        ButtonClose.pack()


if __name__ == "__main__":
    root = Tk()
    app = GUI(root)

