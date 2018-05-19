"""
Author: Lagazon, Aaron Louie M.
Date: 5/13/16
Description: This is a game made in python. I modified the game. I changed some of its rules to make it more fun.
I used GUI to make it more user friendly. A user can choose level of difficulty. User is granted 3 lives, and 2 skips.
User also can shuffle the word. You can save your score once the game is over. And you can view the top 3 high scores if you wish to.

"""
import Tkinter
# import tkMessageBox
from Tkinter import *
# from Tkinter import messagebox

# import Tkinter.messagebox
import random

root = Tk() #window properties


def window():
	root.geometry("400x400");
	root.title("Text Twist")   #sets the window property
	root.configure(background="#202020")
	root.resizable(0,0)
#message box for instructions. To be seen in dropdown menu
def mechanics():
	a="	User must enter a word that can be built out from the shuffled word given. All letters of the shuffled word must be used. User can have two points for each correct answer for 'very easy round', three points for 'easy round', and four points for 'not so easy round.' The user is granted 3 lives on start of the game and two skips that can be used to skip the word if ever the user find it hard. Every two consecutive correct answers, the user will get +2 skips. But for every wrong answer, one life would be deducted."
	Tkinter.messagebox.showinfo("Mechanics",a)
	
def difficulty():
	a="	There are three levels of dificulty--easy, medium and hard. Easy has four or five letter shuffled words. Medium has six-letter shuffled words. And hard has seven or eight letter shuffled words."
	Tkinter.messagebox.showinfo("Difficulty",a)
def about():
	a="	This game is a modified Text Twist game. Unlike the original game, in this game, your answer must contain all the letters from the shuffled word. This only means that all letters from the shuffled word given must be used. If you can think of the exact word, then you are a genius! Good luck!"
	Tkinter.messagebox.showinfo("About",a)

#game over window
def over():
	root_over = Frame(root, bg="black")
	
	def no():
		root_over.pack_forget() #if ever the user doesn't want to save his score
		frame_all.pack()
	def window():
		root.geometry("400x400");
		root.title("Text Twist") #sets the window property
		root.configure(background="black")
		root.resizable(0,0)   #para di ma resize yung window
	
	score = {1:0}
	
	def game_over():
		file = open("score_record.txt","r") #gets the previous score from the file.
		a = ""
		for i in file:
			a = str(i)
			b = int(i)
		score[1] = b #nilagay sa dictionary para maging universal.
		
		
		
		frame = Frame(root_over, bg="black")
		message = Label(frame, font="Arial 30 bold", fg="white", text="Game Over!", bg="black")
		message.pack()
		message_1 = Label(frame, font="Arial 20 normal", fg="white", text="Your score is", bg="black")
		message_1.pack()
		message_2 = Label(frame, font="Arial 35 bold", fg="white", text=a, bg="black") #prints the score
		message_2.pack()
		message_3 = Label(frame, font="Arial 15 normal", fg="white", text="Enter your name: ", bg="black")
		message_3.pack(fill=X)
		frame.pack()
	#saving buttons
	def save():
		but_frame = Frame(root_over, bg="black")
		#save button
		save = Button(but_frame, text="save", bd=8, bg="black",fg="white", font="Arial 10 normal", command=save_process)
		save.config(width=10, height=2)
		save.pack(side=LEFT)
		#not a save button
		quit = Button(but_frame, text="no", bd=8, bg="black",fg="white", font="Arial 10 normal", command=no)
		quit.config(width=10, height=2)
		quit.pack()
		but_frame.pack()

	def high_score():
		a = int(score[1])
		file = open("highscore.txt","r")
		for i in file:
			b = int(i)
			if a > b:
				file = open("highscore.txt","w") #overwrites the high score file if ever may bagong high score
				a = str(a)
				file.write(a)
				file.close()


	def save_process():
	
		def bubble(alist):
			n=0
			for passnum in range(len(alist)-1,0,-1):
				n+=1
				for i in range(passnum):
					if alist[i] > alist[i+1]:
						temp = alist[i]
						alist[i]=alist[i+1]
						alist[i+1]=temp
			
			return alist
		"""
		high_score()
		a = score[1]
		b = name.get()
		num = open("all_scores.txt","r")
		nam = open("names.txt","r")
		numlist=[]
		namlist=[]
		dict = {}
		numlist.append(int(a))
		namlist.append(b)
		for z in num:
			h =int(z[:-1])
			numlist.append(h)
		for x in nam:
			namlist.append(x[:-1])
		c = 0
		while c < len (numlist):
			sc = numlist[c]
			nm = namlist[c]
			dict[sc]=nm
		sorted_list = []
		sorted=bubble(numlist)
		for n in range (-1,-4,-1):
			high_sc = sorted[n]
			sorted_list.append(high_sc)
		print(sorted_list)
		"""
		
		high_score()
		
		a = score[1]
		b = name.get()
		scores=[]
		scores.append(int(a))
		file = open("all_scores.txt","r")
		for i in file:
			z=int(i)
			scores.append(z)
		sort = bubble(scores)
		cut_sort = reversed(sort[-3:len(sort)])    #gets the top 3 high scores
		
		
		file_w = open("all_scores.txt","w")
		file_w.write("")
		file_w.close()
		file_a = open("all_scores.txt", "a")
		for v in cut_sort:
			file_a.write(str(v)+"\n")             #puts the top 3 high scores inside a file
		file_a.close()
		
		
		root_over.pack_forget()
		frame_all.pack()
		
	window()
	game_over()


	frame_1 = Frame(root_over, bg="black")
	name = Entry(frame_1, bg="white", justify="center", bd=5, font = "Arial 30 normal")
	name.pack()
	frame_1.pack()

	save()
	root_over.pack()

#I have different codes for each difficulty for I have made different files for them. But most of the codes are just the same. 
#I will just leave a comment for the easy mode.
def easy(): #code for easy mode
	life_container = {1:3} #a dictionary that contains the user's life
	frame_all.pack_forget() #forgets the previous window and procedes on a new one
	root_like = Frame(root, bg="#202020")
	def window():
		root.geometry("400x400");
		root.title("Text Twist")
		root.configure(background="#202020")               #sets window properties
		root.resizable(0,0) #non-resizable window
	def quit():
		root.destroy()			#quits the window
	def reset():
		root_like.pack_forget()    #unpacks the frame(GUI thingy)
		frame_all.pack()
	def menu (): #drop down menu
		menu = Menu(root_like)
		root.config(menu=menu)
		moreagain = Menu(menu)                         
		menu.add_cascade(label="More", menu=moreagain)
		moreagain.add_command(label="Mechanics", command=mechanics)  		#A dropdown menu for instructions. Made for newbie users.
		moreagain.add_command(label="Difficulty", command=difficulty)
		moreagain.add_command(label="About", command=about)
		
	container={1:""}		#shuffled word.				
	prev_correct = {1:""}    #Previous correct answer
	correct= {1:""}			#correct answer
	
	def word_provide():
		file = open ("easy.txt", "r") #opens the notepad containing five letter words since this is easy mode.
		random_words=[] #container for the words to be randomized
		for line in file:
			random_words+=[line[:-1]] 
		random_i = random.randint(0, len(random_words)-1) #calls a function from random module. Randomizes a number from 0 to number of words minus one. :)
		s = random_words [random_i] #di ba randomized yung number so randomized din yung word kasi randomized yung index niya. hehe
		correct[1]=s  
		print(correct, "correct answer")
		file.close()
		shuf = "".join(random.sample(s,len(s))) #calls random module again. This just simply shuffles a word. Built-in function from random module.
		ref.configure(text=shuf) #para ipakita siya sa window. Using Tkinter syntax.
		container[1]=shuf #puts the shuffled word into a dictionary kasi diba hindi universal yung mga element under ng  function. SO isesave ko siya sa dic
		print (container)
	
	def shuffle(): #shuffles the word in "container" dictionary
		s=container[1]
		shuf = "".join(random.sample(s,len(s)))
		ref.configure(text=shuf)
		

	def life():  #updates the life of the user
		s = life_container[1]
		t = s - 1
		life_container[1]= t
		u = str(t)
		life.configure(text=u)
		

	ans_container={1:""} #just to be universal. I put user's answer to a dictionary

	def get_ans(): #gets and stores user answer to a dictionary
		answer = ans.get()
		ans_container[1]=answer
	
	pscore={1:0} #container ng score ng user. "1" ung key para mag append lang siya
	
	def score_update():
		a = pscore[1]
		a+=2 #adds two sa current score
		b = str(a)
		pscore[1]=int(b) #appends the value in the dictionary. #update lang
		cscore.configure(text=b)
		
	def if_wrong():
		a = prev_correct[1]
		#pops message if answer = Wrong
		show.configure(text="Try Again!")
		show_1.configure(text="Correct answer: ")
		show_correct.configure(text=a)  #shows the correct answer if wrong
		
	score_combo={1:0}
	next_word_ability = {1:2}   #skip ability
	
	def if_correct():
		#add skip ability
		a = score_combo[1]
		a+=1
		score_combo[1] = a
		
		#configuration
		show.configure(text="Nice!")
		show_1.configure(text="+2 points")
		show_correct.configure(text="")
			#skip ability if-else
		if score_combo[1] == 3:                                           
			show_correct.configure(text="+2 Skips")
			c = next_word_ability[1]
			c+=2
			next_word_ability[1] = c                         #pag nagka 2 consecutive correct answers +2 skips yun
			
			skip = str(next_word_ability[1])
			nwa_1.configure(text=skip)  #updates the GUI
			score_combo[1]=0            #resets to zero
			print(score_combo,"combo")
			
	def checker(): #checks if the answer is correct
		get_ans() #function para makuha yung answer ng user
		print(ans_container)
		dic = open ("list_words.txt","r") #so bubuksan yung listahan ng all words.
		answer = ans_container[1].lower() #kinuha lang yung sagot ng user
		correct_answer = container[1]
		cor = correct[1]
		all_words=[]
		same = False
		for l in dic:
			all_words+=[l[:-1]]
		
		if answer == cor:
			same = True
		else:
			if answer in all_words:
				if len(answer)==len(correct_answer):
					for a in answer:                       #this just compares user's answer to the correct answer.
						if a in correct_answer:
							same = True
							continue
						else:
							same = False
							break
						
				else:
					same = False
			else:
				same = False

		w = ans.get()
		x = len(w)
		if same:
			print ("nice!")
			score_update() #+2 points
			word_provide()
			ans.delete(0,x)   #empties the entry box
			if_correct()
		else:
			print("Stupid!") 
			swap = correct[1]
			prev_correct[1]=swap
			word_provide()    
			ans.delete(0,x)   #para maempty yung "Entry box"
			s = life_container[1]
			t = s - 1
			life_container[1]= t   #deducts 1 in life
			u = str(t)
			life.configure(text=t)
			if_wrong()
			score_combo[1]=0
			
			#
			score_final = str(pscore[1])  #must be string to be put in a file
			life_no = life_container[1]
			if life_no < 0:
				file = open("score_record.txt","w")
				file.write(score_final)
				file.close()
				root_like.pack_forget()
				over()
				
	def next_word():
		w = ans.get()
		x = len(w)
		
		swap = correct[1]
		prev_correct[1]=swap
		s = prev_correct[1]
		if next_word_ability[1] > 0:
			word_provide()
			show.configure(text="Previous answer:")
			show_1.configure(text=s)
			show_correct.configure(text="")
			a = next_word_ability[1]
			a-=1
			next_word_ability[1] = a        #once skip is used ma dededuct yung skip power niya
			skip = str(next_word_ability[1])
			nwa_1.configure(text=skip)
			ans.delete(0,x)
		else:
			show.configure(text="Sorry!")
			show_1.configure(text="No skips left.")
			show_correct.configure(text="")
			ans.delete(0,x)
			
	def buttons():
		frame = Frame(root_like, bg="black")
		butt1 = Button(frame, text="Reset", bg= "black",fg="white", bd=4, activebackground="gold", command=reset)
		butt1.config(width=10, height=2)
		butt1.pack( padx=2 , pady=2, side=LEFT)
		butt3 = Button(frame, text="Submit", bg= "black",fg="white", bd=4, activebackground="gold", command=checker) #add_command
		butt3.config(width=15, height=2)
		butt3.pack( padx=2 , pady=2, side=LEFT)
		butt4 = Button(frame, text="Shuffle", bg= "black",fg="white", bd=4,activebackground="gold", command=shuffle)
		butt4.config(width=10, height=2)
		butt4.pack( padx=2 , pady=2,side=LEFT)
		butt2 = Button(frame, text="Skip >>>", bg= "black",fg="white", bd=4,activebackground="gold", command=next_word)
		butt2.config(width=15, height=2)
		butt2.pack( padx=2 , pady=2,side=LEFT)
		frame.pack(fill=X)		

	window()
	menu()
	#========================================================
	#shuffled word reference
	case_ref= Frame(root_like, bg="black")
	ref= Tkinter.Label(case_ref, text="", bg="black", font="Arial 40 bold", fg="white", justify=CENTER)
	ref.pack()
	case_ref.pack(fill=X)
	#========================================================
	ans= Entry(root_like, font = "Arial 30 normal",justify="center", bd=5, bg="white")
	ans.pack(ipady=5)

	#---------------------------------------------------------------
	word_provide()
	buttons()
	
	#scores
	case= Frame(root_like, bg="#202020")
	score= Label(case, text="Score:", bg="#202020", font = "Arial 15 normal", fg="white")
	score.pack()
	cscore= Label(case, text="0", bg="#202020", font = "Arial 12 normal", fg="white")
	cscore.pack()
	case.pack(side=LEFT)                               #shows on GUI the score
	case1=Frame(root_like, bg="#202020")
	#shows on GUI number of skips left
	nwa = Label(case1, bg="#202020", text="Skips:", fg="white", font = "Arial 10 bold")
	nwa.pack()
	nwa_1 = Label(case1, bg="#202020", text="2", fg="white", font = "Arial 10 normal")
	nwa_1.pack()
	
	#highscore
	high_s = open("highscore.txt","r")
	high_score = 0
	for i in high_s:                  #shows on UI the highscore
		high_score+=int(i)
	str_high_score = str(high_score)
	
	
	highest_score= Label(case1, text="High Score:", bg="#202020", font = "Arial 15 normal", fg="white").pack()
	highest_cscore= Label(case1, text=str_high_score, bg="#202020", font = "Arial 24 normal", fg="white").pack()
	life_label = Label(case, text="Life:", bg="#202020", font= "Arial 15 normal", fg="white")
	life_label.pack()                #shows the life remaining
	life = Label(case, text="3",fg="white", bg="#202020", font= "Arial 12 normal")
	life.pack()
	case1.pack(side=RIGHT)
	
	#
	show_frame = Frame (root_like, bg="#202020")
	show = Label(show_frame, bg = "#202020", text ="", fg="white", font="Arial 15 bold")
	show_1 = Label(show_frame, bg = "#202020", text ="", fg="white", font="Arial 10 normal")
	show_correct =Label (show_frame, bg= "#202020", fg = "white", text="")
	
	show.pack()
	show_1.pack()
	show_correct.pack()
	show_frame.pack()	
	
	root_like.pack()
	
	#=====================================================================
	
	
#END OF EASY FUNCTION==================================================================================================================end of easy

def medium(): #code for easy mode
	life_container = {1:3} #a dictionary that contains the user's life
	frame_all.pack_forget() #forgets the previous window and procedes on a new one
	root_like = Frame(root, bg="#202020")
	def window():
		root.geometry("400x400");
		root.title("Text Twist")
		root.configure(background="#202020")
		root.resizable(0,0) #non-resizable window
	def menu (): #drop down menu
		menu = Menu(root)
		root.config(menu=menu)
		moreagain = Menu(menu)
		menu.add_cascade(label="More", menu=moreagain)
		moreagain.add_command(label="Mechanics", command=mechanics)  #no cmmands yet, pero lalagyan ko po siya
		moreagain.add_command(label="Difficulty", command=difficulty)
		moreagain.add_command(label="About", command=about)
		
	def quit():
		root.destroy()
	def reset():
		root_like.pack_forget()
		frame_all.pack()
		
	container={1:""}
	prev_correct = {1:""}
	correct= {1:""}
	
	def word_provide():
		file = open ("medium.txt", "r") #opens the notepad containing five letter words
		random_words=[] #container for the words to be randomized
		for line in file:
			random_words+=[line[:-1]] 
		random_i = random.randint(0, len(random_words)-1) #calls a function from random module. Randomizes a number from 0 to number of words minus one. :)
		s = random_words [random_i] #di ba randomized yung number so randomized din yung word kasi randomized yung index niya. hehe
		correct[1]=s
		print(correct, "correct answer")
		file.close()
		shuf = "".join(random.sample(s,len(s))) #calls random module again. This just simply shuffles a word. Built-in function from random module.
		ref.configure(text=shuf) #para ipakita siya sa window. Using Tkinter syntax.
		container[1]=shuf #puts the shuffled word into a dictionary kasi diba hindi universal yung mga element under ng  function. SO isesave ko siya sa dic
		print (container)
	
	def shuffle(): #shuffles the word in "container" dictionary
		s=container[1]
		shuf = "".join(random.sample(s,len(s)))
		ref.configure(text=shuf)
		

	def life():
		s = life_container[1]
		t = s - 1
		life_container[1]= t
		u = str(t)
		life.configure(text=u)
		

	ans_container={1:""}

	def get_ans(): #gets and stores user answer to a dictionary
		answer = ans.get()
		ans_container[1]=answer
	
	pscore={1:0} #container ng score ng user. "1" ung key para mag append lang siya
	def score_update():
		a = pscore[1]
		a+=3 #adds two sa current score
		b = str(a)
		pscore[1]=int(b) #appends the value in the dictionary.
		cscore.configure(text=b)
	def if_wrong():
		a = prev_correct[1]
		#pops message if answer = Wrong
		print(score_combo,"combo")
		show.configure(text="Try Again!")
		show_1.configure(text="Correct answer: ")
		show_correct.configure(text=a)
		
	score_combo={1:0}
	next_word_ability = {1:2}
	def if_correct():
		#add skip ability
		a = score_combo[1]
		a+=1
		score_combo[1] = a
		#configuration
		show.configure(text="Nice!")
		show_1.configure(text="+3 points")
		show_correct.configure(text="")
			#skip ability if-else
		if score_combo[1] == 3:                                            #<<<<<<<<------------ check this beh
			show_correct.configure(text="+2 skips")
			c = next_word_ability[1]
			c+=2
			next_word_ability[1] = c
			
			skip = str(next_word_ability[1])
			nwa_1.configure(text=skip)
			score_combo[1]=0 #resets to zero
			print(score_combo,"combo")
			
	def checker(): #checks if the answer is correct
		get_ans() #function para makuha yung answer ng user
		print(ans_container)
		dic = open ("list_words.txt","r") #so bubuksan yung listahan ng all words.
		answer = ans_container[1].lower() #kinuha lang yung sagot ng user
		correct_answer = container[1]
		all_words=[]
		same = False
		for l in dic:
			all_words+=[l[:-1]]
		cor = correct[1]
		if answer == cor:
			same = True
		else:
			if answer in all_words:
				if len(answer)==len(correct_answer):
					for a in answer:                       #this just compares user's answer to the correct answer.
						if a in correct_answer:
							same = True
							continue
						else:
							same = False
							break
						
				else:
					same = False
			else:
				same = False

		w = ans.get()
		x = len(w)
		if same:
			print ("nice!")
			score_update()
			word_provide()
			ans.delete(0,x)
			if_correct()
		else:
			print("Stupid!") 
			swap = correct[1]
			prev_correct[1]=swap
			word_provide()    
			ans.delete(0,x)   #para maempty yung "Entry box"
			s = life_container[1]
			t = s - 1
			life_container[1]= t
			u = str(t)
			life.configure(text=t)
			if_wrong()
			score_combo[1]=0
			
			#
			score_final = str(pscore[1])  #must be string to be put in a file
			life_no = life_container[1]
			if life_no < 0:
				file = open("score_record.txt","w")
				file.write(score_final)
				file.close()
				root_like.pack_forget()
				over()
	def next_word():
		w = ans.get()
		x = len(w)
		swap = correct[1]
		prev_correct[1]=swap
		s = prev_correct[1]
		if next_word_ability[1] > 0:
			word_provide()
			
			show.configure(text="Previous answer:")
			show_1.configure(text=s)
			show_correct.configure(text="")
			
			a = next_word_ability[1]
			a-=1
			next_word_ability[1] = a
			skip = str(next_word_ability[1])
			nwa_1.configure(text=skip)
			ans.delete(0,x)
		else:
			ans.delete(0,x)
			show.configure(text="Sorry!")
			show_1.configure(text="No skips left.")
			show_correct.configure(text="")
			
	def buttons():
		frame = Frame(root_like, bg="black")
		butt1 = Button(frame, text="Reset", bg= "black",fg="white", bd=4, activebackground="gold", command=reset)
		butt1.config(width=10, height=2)
		butt1.pack( padx=2 , pady=2, side=LEFT)
		butt3 = Button(frame, text="Submit", bg= "black",fg="white", bd=4, activebackground="gold", command=checker) #add_command
		butt3.config(width=15, height=2)
		butt3.pack( padx=2 , pady=2, side=LEFT)
		butt4 = Button(frame, text="Shuffle", bg= "black",fg="white", bd=4,activebackground="gold", command=shuffle)
		butt4.config(width=10, height=2)
		butt4.pack( padx=2 , pady=2,side=LEFT)
		butt2 = Button(frame, text="Skip >>>", bg= "black",fg="white", bd=4,activebackground="gold", command=next_word)
		butt2.config(width=15, height=2)
		butt2.pack( padx=2 , pady=2,side=LEFT)
		frame.pack(fill=X)		
		
	window()
	menu()
	#========================================================
	case_ref= Frame(root_like, bg="black")
	ref= Tkinter.Label(case_ref, text="", bg="black", font="Arial 40 bold", fg="white", justify=CENTER)
	ref.pack()
	case_ref.pack(fill=X)
	#========================================================
	ans= Entry(root_like, text="Enter Answer Here!", font = "Arial 30 normal",justify="center", bd=5, bg="white")
	ans.pack(ipady=5)



	#---------------------------------------------------------------
	word_provide()
	buttons()
	
	#scores
	case= Frame(root_like, bg="#202020")
	score= Label(case, text="Score:", bg="#202020", font = "Arial 15 normal", fg="white")
	score.pack()
	cscore= Label(case, text="0", bg="#202020", font = "Arial 12 normal", fg="white")
	cscore.pack()
	case.pack(side=LEFT)
	case1=Frame(root_like, bg="#202020")
	nwa = Label(case1, bg="#202020", text="Skips", fg="white", font = "Arial 10 bold")
	nwa.pack()
	nwa_1 = Label(case1, bg="#202020", text="2", fg="white", font = "Arial 10 normal")
	nwa_1.pack()
	
	#highscore
	high_s = open("highscore.txt","r")
	high_score = 0
	for i in high_s:
		high_score+=int(i)
	str_high_score = str(high_score)
	
	highest_score= Label(case1, text="High Score:", bg="#202020", font = "Arial 15 normal", fg="white").pack()
	highest_cscore= Label(case1, text=str_high_score, bg="#202020", font = "Arial 24 normal", fg="white").pack()
	life_label = Label(case, text="Life:", bg="#202020", font= "Arial 15 normal", fg="white")
	life_label.pack()
	life = Label(case, text="3",fg="white", bg="#202020", font= "Arial 12 normal")
	life.pack()
	case1.pack(side=RIGHT)
	
	#
	show_frame = Frame (root_like, bg="#202020")
	show = Label(show_frame, bg = "#202020", text ="", fg="white", font="Arial 15 bold")
	show_1 = Label(show_frame, bg = "#202020", text ="", fg="white", font="Arial 10 normal")
	show_correct =Label (show_frame, bg= "#202020", fg = "white", text="")
	
	show.pack()
	show_1.pack()
	show_correct.pack()
	show_frame.pack()	
	root_like.pack()
	
	#=====================================================================

#end of medium function ================================================================================================================end of medium function
def hard(): #code for easy mode
	life_container = {1:3} #a dictionary that contains the user's life
	frame_all.pack_forget() #forgets the previous window and procedes on a new one
	root_like = Frame(root, bg="#202020")
	def window():
		root.geometry("400x400");
		root.title("Text Twist")
		root.configure(background="#202020")
		root.resizable(0,0) #non-resizable window
	def menu (): #drop down menu
		menu = Menu(root)
		root.config(menu=menu)
		moreagain = Menu(menu)
		menu.add_cascade(label="More", menu=moreagain)
		moreagain.add_command(label="Mechanics", command=mechanics) 
		moreagain.add_command(label="Difficulty", command=difficulty)
		moreagain.add_command(label="About", command=about)
		
	def quit():
		root.destroy()
	def reset():
		root_like.pack_forget()
		frame_all.pack()
	container={1:""}
	prev_correct = {1:""}
	correct= {1:""}
	
	def word_provide():
		file = open ("hard.txt", "r") #opens the notepad containing five letter words
		random_words=[] #container for the words to be randomized
		for line in file:
			random_words+=[line[:-1]] 
		random_i = random.randint(0, len(random_words)-1) #calls a function from random module. Randomizes a number from 0 to number of words minus one. :)
		s = random_words [random_i] #di ba randomized yung number so randomized din yung word kasi randomized yung index niya. hehe
		correct[1]=s
		print(correct, "correct answer")
		file.close()
		shuf = "".join(random.sample(s,len(s))) #calls random module again. This just simply shuffles a word. Built-in function from random module.
		ref.configure(text=shuf) #para ipakita siya sa window. Using Tkinter syntax.
		container[1]=shuf #puts the shuffled word into a dictionary kasi diba hindi universal yung mga element under ng  function. SO isesave ko siya sa dic
		print (container)
	
	def shuffle(): #shuffles the word in "container" dictionary
		s=container[1]
		shuf = "".join(random.sample(s,len(s)))
		ref.configure(text=shuf)
		

	def life():
		s = life_container[1]
		t = s - 1
		life_container[1]= t
		u = str(t)
		life.configure(text=u)
		

	ans_container={1:""}

	def get_ans(): #gets and stores user answer to a dictionary
		answer = ans.get()
		ans_container[1]=answer
	
	pscore={1:0} #container ng score ng user. "1" ung key para mag append lang siya
	def score_update():
		a = pscore[1]
		a+=4 #adds four sa current score
		b = str(a)
		pscore[1]=int(b) #appends the value in the dictionary.
		cscore.configure(text=b)
	def if_wrong():
		a = prev_correct[1]
		#pops message if answer = Wrong
		print(score_combo,"combo")
		show.configure(text="Try Again!")
		show_1.configure(text="Correct answer: ")
		show_correct.configure(text=a)
		
	score_combo={1:0}
	next_word_ability = {1:2}
	def if_correct():
		#add skip ability
		a = score_combo[1]
		a+=1
		score_combo[1] = a
		#configuration
		show.configure(text="Nice!")
		show_1.configure(text="+4 points")
		show_correct.configure(text="")
			#next skip if-else
		if score_combo[1] == 3:                                            #<<<<<<<<------------ check this beh
			show_correct.configure(text="+2 skips")
			c = next_word_ability[1]
			c+=2
			next_word_ability[1] = c
			
			skip = str(next_word_ability[1])
			nwa_1.configure(text=skip)
			score_combo[1]=0 #resets to zero
			print(score_combo,"combo")
			
	def checker(): #checks if the answer is correct
		get_ans() #function para makuha yung answer ng user
		print(ans_container)
		dic = open ("list_words.txt","r") #so bubuksan yung listahan ng all words.
		answer = ans_container[1].lower() #kinuha lang yung sagot ng user
		correct_answer = container[1]
		all_words=[]
		same = False
		for l in dic:
			all_words+=[l[:-1]]
		cor = correct[1]
		if answer == cor:
			same = True
		else:
			if answer in all_words:
				if len(answer)==len(correct_answer):
					for a in answer:                       #this just compares user's answer to the correct answer.
						if a in correct_answer:
							same = True
							continue
						else:
							same = False
							break
						
				else:
					same = False
			else:
				same = False

		w = ans.get()
		x = len(w)
		if same:
			print ("nice!")
			score_update()
			word_provide()
			ans.delete(0,x)
			if_correct()
		else:
			print("Stupid!") 
			swap = correct[1]
			prev_correct[1]=swap
			word_provide()    
			ans.delete(0,x)   #para maempty yung "Entry box"
			s = life_container[1]
			t = s - 1
			life_container[1]= t
			u = str(t)
			life.configure(text=t)
			if_wrong()
			score_combo[1]=0
			
			#
			score_final = str(pscore[1])  #must be string to be put in a file
			life_no = life_container[1]
			if life_no < 0:
				file = open("score_record.txt","w")
				file.write(score_final)
				file.close()
				root_like.pack_forget()
				over()
	def next_word():
		w = ans.get()
		x = len(w)
		#
		swap = correct[1]
		prev_correct[1]=swap
		s = prev_correct[1]
		if next_word_ability[1] > 0:
			word_provide()
			#
			show.configure(text="Previous answer:")
			show_1.configure(text=s)
			show_correct.configure(text="")
			#
			a = next_word_ability[1]
			a-=1
			next_word_ability[1] = a
			skip = str(next_word_ability[1])
			nwa_1.configure(text=skip)
			ans.delete(0,x)
		else:
			show.configure(text="Sorry!")
			show_1.configure(text="No skips left.")
			show_correct.configure(text="")
			ans.delete(0,x)
			
	def buttons():
		frame = Frame(root_like, bg="black")
		butt1 = Button(frame, text="Reset", bg= "black",fg="white", bd=4, activebackground="gold", command=reset)
		butt1.config(width=10, height=2)
		butt1.pack( padx=2 , pady=2, side=LEFT)
		butt3 = Button(frame, text="Submit", bg= "black",fg="white", bd=4, activebackground="gold", command=checker)#add_command
		butt3.config(width=15, height=2)
		butt3.pack( padx=2 , pady=2, side=LEFT)
		butt4 = Button(frame, text="Shuffle", bg= "black",fg="white", bd=4,activebackground="gold", command=shuffle)
		butt4.config(width=10, height=2)
		butt4.pack( padx=2 , pady=2,side=LEFT)
		butt2 = Button(frame, text="Skip >>>", bg= "black",fg="white", bd=4,activebackground="gold", command=next_word)
		butt2.config(width=15, height=2)
		butt2.pack( padx=2 , pady=2,side=LEFT)
		frame.pack(fill=X)		
		
	window()
	menu()
	#========================================================
	case_ref= Frame(root_like, bg="black")
	ref= Tkinter.Label(case_ref, text="", bg="black", font="Arial 40 bold", fg="white", justify=CENTER)
	ref.pack()
	case_ref.pack(fill=X)
	#========================================================
	ans= Entry(root_like, text="Enter Answer Here!", font = "Arial 30 normal",justify="center", bd=5, bg="white")
	ans.pack(ipady=5)



	#---------------------------------------------------------------
	word_provide()
	buttons()
	
	#scores
	case= Frame(root_like, bg="#202020")
	score= Label(case, text="Score:", bg="#202020", font = "Arial 15 normal", fg="white")
	score.pack()
	cscore= Label(case, text="0", bg="#202020", font = "Arial 12 normal", fg="white")
	cscore.pack()
	case.pack(side=LEFT)
	case1=Frame(root_like, bg="#202020")
	nwa = Label(case1, bg="#202020", text="Skips", fg="white", font = "Arial 10 bold")
	nwa.pack()
	nwa_1 = Label(case1, bg="#202020", text="2", fg="white", font = "Arial 10 normal")
	nwa_1.pack()
	
	#highscore
	high_s = open("highscore.txt","r")
	high_score = 0
	for i in high_s:
		high_score+=int(i)
	str_high_score = str(high_score)
	
	highest_score= Label(case1, text="High Score:", bg="#202020", font = "Arial 15 normal", fg="white").pack()
	highest_cscore= Label(case1, text=str_high_score, bg="#202020", font = "Arial 24 normal", fg="white").pack()
	life_label = Label(case, text="Life:", bg="#202020", font= "Arial 15 normal", fg="white")
	life_label.pack()
	life = Label(case, text="3",fg="white", bg="#202020", font= "Arial 12 normal")
	life.pack()
	case1.pack(side=RIGHT)
	
	#
	show_frame = Frame (root_like, bg="#202020")
	show = Label(show_frame, bg = "#202020", text ="", fg="white", font="Arial 15 bold")
	show_1 = Label(show_frame, bg = "#202020", text ="", fg="white", font="Arial 10 normal")
	show_correct =Label (show_frame, bg= "#202020", fg = "white", text="")
	
	show.pack()
	show_1.pack()
	show_correct.pack()
	show_frame.pack()
	
	root_like.pack()
	
	#=====================================================================
	
#end of hard function================================================================================================================end of hard function

frame_all = Frame (root, bg = "#202020")
def menu ():
	menu = Menu(frame_all)
	root.config(menu=menu)
	moreagain = Menu(menu)
	menu.add_cascade(label="More", menu=moreagain)
	moreagain.add_command(label="Mechanics", command=mechanics) #dropdown menu
	moreagain.add_command(label="Difficulty", command=difficulty)
	moreagain.add_command(label="About", command=about)

def view_scores():
	def back():
		fr.pack_forget()
		frame_all.pack()
	frame_all.pack_forget()
	fr = Frame(root, bg="#202020")
	file = open("all_scores.txt","r")
	button = Button(fr, bg="black", fg="white", text="Back", command=back)

	ban = Label(fr, text="Top 3 Scores", font="Arial 40 bold", fg="white", bg="black")
	ban.pack(fill=X)
	
	for a in file:
		print_sc = Label(fr, text=a[:-1], bg="#202020", font="Arial 40 normal", fg="white")
		print_sc.pack()           #shows the user the top 3 high scores
	button.pack(side=LEFT)	
	fr.pack(fill=X)
	
	
	
	
	
def buttons():

	frame = Frame(frame_all, bg="#202020")
	butt1 = Button(frame, text="Easy", bg= "black",fg="white", bd=2, activebackground="gold", font = "Arial 10 normal", command=easy)
	butt1.config(width=15, height=2)
	butt1.pack( padx=2 , pady=2)
	butt3 = Button(frame, text="Medium", bg= "black",fg="white", bd=2, activebackground="gold", font = "Arial 10 normal", command=medium) #add_command
	butt3.config(width=15, height=2)
	butt3.pack( padx=2 , pady=2)
	butt4 = Button(frame, text="Hard", bg= "black",fg="white", bd=2,activebackground="gold", font = "Arial 10 normal", command=hard)
	butt4.config(width=15, height=2)
	butt4.pack( padx=2 , pady=2)
	butt5 = Button(frame, text="View Scores", bg= "black",fg="white", bd=2,activebackground="gold", font = "Arial 10 normal", command=view_scores)
	butt5.config(width=15, height=2)
	butt5.pack( padx=2 , pady=1)
	frame.pack(fill=X)
	
	
window()
imgPath = r"bg.png"
photo = PhotoImage(file=imgPath)
label = Label(frame_all, image=photo, bg = "black")
menu()
label.pack()
buttons()
frame_all.pack()
root.mainloop()