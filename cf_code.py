from tkinter import *

import requests

def main():


	def do_it():
		
		url = ("https://codeforces.com/api/user.info?handles=") 
		
		data = (url + (str(name.get())))
	
		resp = requests.get(data)
	
		json = resp.json()
	
		
		unavailable =  (json['status'])
	
		if (unavailable == "FAILED"):
			label_unavailable = Label(root, text= "USER NOT FOUND", font=("arial", 15, "bold"), fg="red").place(x=10, y=100)
		else:
			pass
	
		handle = ("Handle is> " + json['result'][0]['handle'])
	
		currentRating = ("Rating is> " + str(json['result'][0]['rating']))
	
		rank = ("Current Rank is> " + (json['result'][0]['rank']))
		
		maxRating = ("Max rating is> " + str(json['result'][0]['maxRating']))
	
		maxRank = ("Maximum Rank is> " + (json['result'][0]['maxRank']))
	
		label_handle = Label(root, text= handle, font=("arial", 10, "bold")).place(x=10, y=100)
		
		label_current_rating = Label(root, text= currentRating, font=("arial", 10, "bold")).place(x=10, y=120)
	
		label_rank = Label(root, text= rank, font=("arial", 10, "bold")).place(x=10, y=140)
	
		label_max_rating = Label(root, text= maxRating, font=("arial", 10, "bold")).place(x=10, y=160)
	
		label_max_rank = Label(root, text= maxRank, font=("arial", 10, "bold")).place(x=10, y=180)
	
	
	root = Tk()
	
	root.title("CodeForces Info")
	
	root.geometry("350x255+0+0")
	
	head = Label(root, text="CodeForces", font=("arial", 25, "bold"), fg="black").pack()
	
	labelOne = Label(root, text="Enter the CodeForces handle> ", font=("arial", 10, "bold"), fg="black").place(x=10,y=50)
	
	name = StringVar()
	
	entry_box = Entry(root, textvariable=name, width=25, bg="white", ).place(x=10, y=75)
	
	work = Button(root, text="Search", width = 4, height=1, bg="white", command=do_it).place(x=10, y=210)
	
	root.mainloop()

main()