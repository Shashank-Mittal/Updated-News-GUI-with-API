from tkinter import *
import sqlite3
import requests  
import json
class registration:
	def __init__(self,first):
		#frame1=Frame(first)
		#frame1.pack()
		self.first=first
		self.first.title("Login Page")

		#self.photo=PhotoImage(file="images.png")
		self.background_image=PhotoImage(file="helll.png")
		#first.configure(bg="black",height=3000,width=3000)
		canvas=Canvas(first,height=3000,width=3000)
		canvas.pack()
		canvas.create_image(0,50,anchor=NW,image= self.background_image )
		self.label1=Label(first,text="User ID",fg="black",font = (30),bg="white")
		self.label1.place(x=450,y=190)
		self.entryU=Entry(first,font = (20))
		self.entryU.place(x=530,y=193)
		self.UserIDch=Label(first,text="",fg="red",font = (30),bg="white")
		self.UserIDch.place(x=780,y=190)
		self.label2=Label(first,text="Password",fg="black",bg="white",font = (30))
		self.label2.place(x=420,y=260)
		self.entryP=Entry(first,show="*",font = (30))
		self.entryP.place(x=530,y=263)
		self.PasswordC=Label(first,text="",fg="red",bg="white",font = (30))
		self.PasswordC.place(x=780,y=260)
		self.buttonL=Button(first,text="Log In",bg="red",font = (30),width=15,command=self.log,fg="white")
		self.buttonL.place(x=535,y=330)
		self.buttonS=Button(first,text="Create a new account",bg="red",font = (30),width=20,command=self.pageS,fg="white")
		self.buttonS.place(x=510,y=400)
	def pageS(self):
		#self.first.withdraw()
		self.newWindow = Toplevel(self.first)
		bb = Buttons1(self.newWindow)
	def NewsH(self):
		self.newWindow2 = Toplevel(self.first)
		b1 = News(self.newWindow2)
	def log(self):
		#if(self.check()):
		self.Q=self.entryP.get()
		#print(self.Q)
		ids=(self.entryU.get())
		query="SELECT Password FROM user WHERE User_ID = ?"
		self.run_query1(query,(ids,))
	def run_query1(self,query,parameters=()):
		self.db_name ='user1D.db'
		with sqlite3.connect(self.db_name) as conn1:
			cursor1=conn1.cursor()
			try:	
				query_result=str(cursor1.execute(query,parameters))
				cp=str(cursor1.fetchone()[0])
			except:	
				self.UserIDch.configure(text="Use ID is not Registered")
			else:
				if(cp==""):
					self.UserIDch.configure(text="Use ID is not Registered")
					self.PasswordC.configure(text="")
				elif(cp!=self.Q):
					self.PasswordC.configure(text="Incorrect Password")
					self.UserIDch.configure(text="")
				else:
					self.PasswordC.configure(text="")
					self.UserIDch.configure(text="")
					#self.buttonL.configure(command=self.NewsH)
					self.NewsH()
					#print("Task Completed")
					#print(cp)
					#print(type(cp))
			'''else:
				self.Error.configure(text="SignUp Succesfully")
				self.UserCh.configure(text="")'''
			conn1.commit()
class Buttons1:
	def __init__(self,second):
		second.configure(bg="black",height=5000,width=5000)
		self.background_image=PhotoImage(file="io.png")
		#first.configure(bg="black",height=3000,width=3000)
		canvas=Canvas(second,height=3000,width=3000)
		canvas.pack()
		canvas.create_image(850,200,anchor=NW,image= self.background_image )
		self.Fname=Label(second,text="First Name",font=(20),bg="white",fg="black")
		#self.Fname=Label(second,text="First Name",font=(20),background="Transparent",fg="black")
		self.Fname.place(x=300,y=100)
		self.entryF=Entry(second,font=(20))
		self.entryF.place(x=410,y=100)
		self.Lname=Label(second,text="Last Name",font=(20),bg="white",fg="black")
		self.Lname.place(x=300,y=150)
		self.entryL=Entry(second,font=(20))
		self.entryL.place(x=410,y=150)
		self.EMname=Label(second,text="Email",font=(20),bg="white",fg="black")
		self.EMname.place(x=350,y=200)
		self.entryEM=Entry(second,font=(20))
		self.entryEM.place(x=410,y=200)
		self.EMnameCH=Label(second,text="",font=(20),bg="white",fg="red")
		self.EMnameCH.place(x=650,y=200)
		self.Pname=Label(second,text="New Password",font=(20),bg="white",fg="black")
		self.Pname.place(x=264,y=250)
		self.entryP=Entry(second,font=(20),show="*")
		self.entryP.place(x=410,y=250)
		self.Pcname=Label(second,text="",font=(5),bg="white",fg="red")
		self.Pcname.place(x=650,y=250)
		self.CPname=Label(second,text="Confirm Password",font=(20),bg="white",fg="black")
		self.CPname.place(x=235,y=300)
		self.entryCP=Entry(second,font=(20),show="*")
		self.entryCP.place(x=410,y=300)
		self.CPcname=Label(second,text="",font=(5),bg="white",fg="red")
		self.CPcname.place(x=650,y=300)
		self.Mobile=Label(second,text="Mobile Number",font=(20),bg="white",fg="black")
		self.Mobile.place(x=265,y=350)
		self.MobileE=Entry(second,font=(20))
		self.MobileE.place(x=410,y=350)
		self.MobileCh=Label(second,text="",font=(5),bg="white",fg="red")
		self.MobileCh.place(x=650,y=350)
		self.Gender=Label(second,text="Gender",font=(20),bg="white",fg="black")
		self.Gender.place(x=330,y=400)
		self.R=IntVar()
		self.RM=Radiobutton(second,text="Male",variable=self.R,fg="black",font=(20),value=1)
		self.RM.place(x=410,y=400)
		self.RF=Radiobutton(second,text="Female",variable=self.R,fg="black",font=(20),value=2)
		self.RF.place(x=500,y=400)
		self.User=Label(second,text="Create user Id",font=(20),bg="white",fg="black")
		self.User.place(x=260,y=450)
		self.UEntry=Entry(second,font=(20))
		self.UEntry.place(x=410,y=450)
		self.UserCh=Label(second,text="",font=(5),bg="white",fg="red")
		self.UserCh.place(x=650,y=450)
		self.ButtonSignUp=Button(second,text="Sign Up",font=(30),width=10,bg="red",fg="white",command=self.adding)
		self.ButtonSignUp.place(x=410,y=500)
		self.Error=Label(second,text="",font=(5),bg="white",fg="red")
		self.Error.place(x=450,y=550)
	def run_query(self,query,parameters=()):
		self.db_name ='user1D.db'
		a=""
		with sqlite3.connect(self.db_name) as conn:
			cursor=conn.cursor()
			try:
				query_result=cursor.execute(query,parameters)
			except sqlite3.IntegrityError as a:
				if(str(a)=="UNIQUE constraint failed: User.Mobile"):
					self.MobileCh.configure(text="Mobile Number already Registered")
				elif(str(a)=="UNIQUE constraint failed: User.Email"):
					self.EMnameCH.configure(text="Email Id already Registered")
				elif(str(a)=="UNIQUE constraint failed: User.User_ID"):
					self.UserCh.configure(text="User ID already taken!!")
			else:
				self.Error.configure(text="SignUp Succesfully")
				self.UserCh.configure(text="")
				print(a)

			conn.commit()
	def adding(self):
		if(self.check()):
			query="INSERT INTO User VALUES (?,?,?,?,?,?,NULL)"
			parameters=(self.UEntry.get(),self.entryP.get(),self.entryF.get(),self.entryL.get(),self.entryEM.get(),self.MobileE.get())
			self.run_query(query,parameters)
	def check(self):
		if(self.entryP.get()=="" or len(self.entryL.get())<1 or len(self.entryEM.get())<1 or len(self.UEntry.get())<1 ):
			self.Error.configure(text="Please fill all the Field")
			self.CPcname.configure(text="")
			self.MobileCh.configure(text="")
			self.Pcname.configure(text="")
			self.EMnameCH.configure(text="")
			self.UserCh.configure(text="")
		elif(len(self.entryEM.get())<10):
			self.Pcname.configure(text="")
			self.Error.configure(text="")
			self.MobileCh.configure(text="")
			self.CPcname.configure(text="")
			self.UserCh.configure(text="")
			self.EMnameCH.configure(text="invalid Email")
		elif(self.Emailcheck(self.entryEM.get())):
			self.Pcname.configure(text="")
			self.Error.configure(text="")
			self.MobileCh.configure(text="")
			self.CPcname.configure(text="")
			self.UserCh.configure(text="")
			self.EMnameCH.configure(text="invalid Email")
		elif(len(self.entryP.get())<8):
			#self.Pcname.configure(text="Password min 8 digits")
			self.Pcname.configure(text="Password should be minimum 8 digits\n consists of Atleast \n 1 UpperCase letter \n 2 Lowercase letter \n 1 Numeric Character \n 1 special Character",font=(5))
			self.Error.configure(text="")
			self.MobileCh.configure(text="")
			self.CPcname.configure(text="")
			self.EMnameCH.configure(text="")
			self.UserCh.configure(text="")
		elif(self.passwordCheck(self.entryP.get())):
			self.Pcname.configure(text="Password should be minimum 8 digits\n consists of Atleast \n 1 UpperCase letter \n 2 Lowercase letter \n 1 Numeric Character \n 1 special Character",font=(5))
			self.Error.configure(text="")
			self.MobileCh.configure(text="")
			self.CPcname.configure(text="")
			self.EMnameCH.configure(text="")
			self.UserCh.configure(text="")
		elif(self.entryP.get()!=self.entryCP.get()):
			self.CPcname.configure(text="Password can't Match")
			self.Error.configure(text="")
			self.MobileCh.configure(text="")
			self.Pcname.configure(text="")
			self.EMnameCH.configure(text="")
			self.UserCh.configure(text="")
		elif(len(self.MobileE.get())!=10):
			self.MobileCh.configure(text="Invalid Mobile Number")
			self.Error.configure(text="")
			self.CPcname.configure(text="")
			self.Pcname.configure(text="") 
			self.EMnameCH.configure(text="")
			self.UserCh.configure(text="")
		elif(self.mobile6789(self.MobileE.get())):
			self.MobileCh.configure(text="Invalid Mobile Number")
			self.Error.configure(text="")
			self.CPcname.configure(text="")
			self.Pcname.configure(text="") 
			self.EMnameCH.configure(text="")
			self.UserCh.configure(text="")
		elif(len(self.UEntry.get())<8):
			self.UserCh.configure(text="User Id contains minimum 8 Character")
			self.MobileCh.configure(text="")
			self.Error.configure(text="")
			self.CPcname.configure(text="")
			self.Pcname.configure(text="") 
			self.EMnameCH.configure(text="")
		else:
			self.Pcname.configure(text="")
			self.CPcname.configure(text="")
			self.MobileCh.configure(text="")
			self.EMnameCH.configure(text="")
			self.Error.configure(text="")
			self.UserCh.configure(text="")
			return True
	def mobile6789(self,mobilenum):
		if(mobilenum[0]=='6'or mobilenum[0]=='7'or mobilenum[0]=='8'or mobilenum[0]=='9'):
			return False
		else:
			return True
	def Emailcheck(self,Echeck):
		p=False
		for i in Echeck:
			if(i=='@' or p==True):
				p=True
				if(i=="."):
					return False
		return True
	def passwordCheck(self,pch):
		A=0
		a=0
		nu=0
		sp=0
		for i in pch:
			if(i>='A' and i<="Z"):
				A=A+1
			elif(i>='a' and i<="z"):
				a=a+1
			elif(i>='0' and i<='9'):
				nu=nu+1
			else:
				sp=sp+1
		if(A>0 and a>0 and nu>1 and sp>0):
			return False
		else:
			return True
class News:
	def __init__(self,third):
		self.third=third
		self.third.title("Updated News")
		#self.main_url = "https://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=80dcf91e3abd4c62a5154f0e33c25bc4"
		self.third.configure(bg="black",height=5000,width=5000)
		self.background_image=PhotoImage(file="789.png")
		self.b=PhotoImage(file="ll.png")
		#first.configure(bg="black",height=3000,width=3000)
		canvas=Canvas(self.third,height=3000,width=3000)
		canvas.pack()
		canvas.create_image(0,0,anchor=NW,image= self.b)
		canvas.create_image(250,0,anchor=NW,image= self.background_image )
		self.button1=Button(third,text="Business",bg="red",fg="white",command=self.business,width=15,font=(20))
		self.button1.place(x=40,y=140)
		self.button2=Button(third,text="Entertainment",bg="red",fg="white",command=self.Entertainment,width=15,font=(20))
		self.button2.place(x=240,y=140)
		self.button3=Button(third,text="Health",bg="red",fg="white",command=self.Health,width=15,font=(20))
		self.button3.place(x=440,y=140)
		self.button4=Button(third,text="Science",bg="red",fg="white",command=self.Science,width=15,font=(20))
		self.button4.place(x=640,y=140)
		self.button5=Button(third,text="Sports",bg="red",fg="white",command=self.Sports,width=15,font=(20))
		self.button5.place(x=840,y=140)
		self.button6=Button(third,text="Technology",bg="red",fg="white",command=self.Technology,width=15,font=(20))
		self.button6.place(x=1040,y=140)
		self.buttonLO=Button(third,text="Logout",bg="black",fg="white",command=self.quit,width=5,font=(20))
		self.buttonLO.place(x=1180,y=60)
		try:
			main_url1 = "https://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=80dcf91e3abd4c62a5154f0e33c25bc4"
			open_page = requests.get(main_url1).json()
			article = open_page["articles"]
			results = []
			'''self.MainHead=Label(self.third,text="TODAY TIMELINE",fg="blue",font=(2000),bg="white")
			self.MainHead.place(x=500,y=100)'''
			down=240
			for i in range(10):
				self.rubb=Label(self.third,text=" ",fg="white",font=(20),bg="black",width=120)
				self.rubb.place(x=20,y=down)
				down=down+27
				i=i+1
			down=240
			for ar in article:
				results.append(ar["title"])
			for j in range(10):
				self.Head=Label(self.third,text=results[j],fg="white",font=(20),bg="black")
				self.Head.place(x=20,y=down)
				down=down+27
				j=j+1
			print("completed")
		except:
			down=240
			for i in range(10):
				self.rubb=Label(self.third,text=" ",fg="white",font=(20),bg="black",width=80)
				self.rubb.place(x=20,y=down)
				down=down+27
				i=i+1
			self.Head=Label(self.third,text="OOPS!!! Please connect to th Network",fg="White",font=(20),bg="black")
			self.Head.place(x=500,y=300)
	def button11(self,main_url):
	
		#self.main_url1="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=80dcf91e3abd4c62a5154f0e33c25bc4"
		try:	
			self.main_url1=main_url
			open_page = requests.get(self.main_url1).json()
			article = open_page["articles"]
			results = []
			'''self.MainHead=Label(self.third,text="TODAY TIMELINE",fg="blue",font=(2000),bg="white")
			self.MainHead.place(x=500,y=100)'''
			down=240
			for i in range(10):
				self.rubb=Label(self.third,text=" ",fg="white",font=(20),bg="black",width=120)
				self.rubb.place(x=20,y=down)
				down=down+27
				i=i+1
			down=240
			try:
				for ar in article:
					results.append(ar["title"])
				for j in range(10):
					
					self.Head=Label(self.third,text=results[j],fg="white",font=(20),bg="black")
					self.Head.place(x=20,y=down)
					down=down+27
					j=j+1
			except:
				print("Less then 10 lines")
			print("completed")
		except:
			down=240
			for i in range(10):
				self.rubb=Label(self.third,text=" ",fg="white",font=(20),bg="black",width=80)
				self.rubb.place(x=20,y=down)
				down=down+27
				i=i+1
			self.Head=Label(self.third,text="OOPS!!! Please connect to th Network",fg="black",font=(50),bg="white")
			self.Head.place(x=500,y=300)
	def business(self):
		main_url=self.main_url1="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=80dcf91e3abd4c62a5154f0e33c25bc4"
		self.button11(main_url)
	def Technology(self):
		main_url=self.main_url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=80dcf91e3abd4c62a5154f0e33c25bc4"
		self.button11(main_url)
	def Entertainment(self):
		main_url=self.main_url="https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=80dcf91e3abd4c62a5154f0e33c25bc4"
		self.button11(main_url)
	def Science(self):
		main_url=self.main_url="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=80dcf91e3abd4c62a5154f0e33c25bc4"
		self.button11(main_url)
	def Health(self):
		main_url=self.main_url="https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=80dcf91e3abd4c62a5154f0e33c25bc4"
		self.button11(main_url)
	def Sports(self):
		main_url=self.main_url="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=80dcf91e3abd4c62a5154f0e33c25bc4"
		self.button11(main_url)
	def quit(self):
		self.third.destroy()
my=Tk()
obj=registration(my)
my.mainloop()

