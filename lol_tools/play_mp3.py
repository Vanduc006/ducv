import playsound
from tkinter import filedialog
from tkinter import messagebox

SOUND_PATH = filedialog.askopenfilename()
messagebox.showinfo(title="AUDIO ON",
			message= "PLAY SOUND :" + SOUND_PATH )   
playsound.playsound(SOUND_PATH)

 

