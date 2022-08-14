from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.title('Audio Player'); window.resizable(0,0)
        

        Load = Button(window, activeforeground = "blue", activebackground = "green", text = 'Chọn File',  width = 5, font = ('Arial', 10), command = self.load)
        Play = Button(window, activeforeground = "blue", activebackground = "green", text = 'Phát',  width = 5,font = ('Arial', 10), command = self.play)
        Pause = Button(window,activeforeground = "blue", activebackground = "green", text = 'Tạm Dừng',  width = 5, font = ('Arial', 10), command = self.pause)
        Stop = Button(window ,activeforeground = "blue", activebackground = "green", text = 'Dừng!!',  width = 5, font = ('Arial', 10), command = self.stop)
        Up = Button(window, activeforeground = "blue", activebackground = "green", text = '+ Volume',  width = 5, font = ('Arial', 10), command = self.volume_up)
        Down = Button(window, activeforeground = "blue", activebackground = "green", text = '- Volume',  width = 5, font = ('Arial', 10), command = self.volume_down)
        Cre = Button(window, activeforeground = "blue", activebackground = "green", text = '?',  width = 5, font = ('Arial', 10), command = self.cre)

        Load.grid(row=1, column=0, sticky="nwse", ipadx=10,ipady=10)
        Cre.grid(row=1, column=1, sticky="nwse", ipadx=10,ipady=10)
        Play.grid(row=3, column=0, sticky="nwse", ipadx=10,ipady=10)
        Pause.grid(row=3, column=1, sticky="nwse", ipadx=10,ipady=10)
        Stop.grid(row=3, column=2, sticky="nwse", ipadx=10,ipady=10)
        Up.grid(row=4, column=0, sticky="nwse", ipadx=10,ipady=10)
        Down.grid(row=4, column=2, sticky="nwse", ipadx=10,ipady=10)

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename(title="Select a file", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
    #up and down volume 
    def volume_up(self):
        volume = mixer.music.get_volume()
        if volume < 1:
            mixer.music.set_volume(volume+0.1)
    def volume_down(self):
        volume = mixer.music.get_volume()
        if volume > 0:
            mixer.music.set_volume(volume-0.1)
    def cre(self):
        messagebox.showinfo(title="Publisher",
			message="ducjoin")        


root = Tk()
app= MusicPlayer(root)
root.mainloop()





