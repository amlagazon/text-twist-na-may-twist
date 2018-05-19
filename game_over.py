from Tkinter import *
import Tkinter.messagebox
import random

root = Tk() #window properties

def window():
	root.geometry("400x300")
	root.title("Text Twist")
	root.configure(background="black")
	root.resizable(0,0)
score = {1:0}
def game_over():
	file = open("score_record.txt","r")
	a = ""
	for i in file:
		a = str(i)
		b = int(i)
	score[1] = b
	
	
	
	frame = Frame(root, bg="black")
	message = Label(frame, font="Arial 30 bold", fg="white", text="Game Over!", bg="black")
	message.pack()
	message_1 = Label(frame, font="Arial 20 normal", fg="white", text="Your score is", bg="black")
	message_1.pack()
	message_2 = Label(frame, font="Arial 35 bold", fg="white", text=a, bg="black")
	message_2.pack()
	message_3 = Label(frame, font="Arial 15 normal", fg="white", text="Enter your name: ", bg="black")
	message_3.pack(fill=X)
	frame.pack()

def save():
	but_frame = Frame(root, bg="black")
	save = Button(but_frame, text="save", bd=8, bg="black",fg="white", font="Arial 10 normal", command=save_process)
	save.config(width=10, height=2)
	save.pack(side=LEFT)
	quit = Button(but_frame, text="exit", bd=8, bg="black",fg="white", font="Arial 10 normal", command=root.destroy)
	quit.config(width=10, height=2)
	quit.pack()
	
	but_frame.pack()

def high_score():
	a = int(score[1])
	file = open("highscore.txt","r")
	for i in file:
		b = int(i)
		if a > b:
			file = open("highscore.txt","w")
			a = str(a)
			file.write(a)
			file.close()


def save_process():
	high_score()
	a = str(score[1])
	b = name.get()
	score_file = open("all_scores.txt","a")
	score_file.write(b+" ")
	score_file.write(a+"\n")
	score_file.close()
	root.destroy()
	
window()
game_over()


frame_1 = Frame(root, bg="black")
name = Entry(frame_1, bg="white", justify="center", bd=5, font = "Arial 30 normal")
name.pack()
frame_1.pack()

save()


root.mainloop()