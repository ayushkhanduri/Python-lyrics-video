from tkinter import *
import requests
import json

class Application():
	def __init__(self,master):
		self.master = master
		self.generateGui()

	def generateGui(self):
		self.submitHtml = Button(self.master,text="Get Text",command=self.getText)
		self.htmlText = Text(self.master,height=30 ,width= 100)
		self.scrollBar = Scrollbar(self.master)
		self.scrollBar.config(command=self.htmlText.yview)
		self.htmlText.config(yscrollcommand= self.scrollBar.set)
		self.htmlText.insert(END,"something to say")
		self.htmlText.pack(side=LEFT, fill=Y)
		self.scrollBar.pack(side=LEFT, fill=Y)
		self.submitHtml.pack(expand=True)

	def getText(self):
		input = self.htmlText.get("1.0",'end-1c')
		request =requests.post('http://localhost:5000/allUsers',data=input)
		if request.status_code ==200:
			response = json.loads(request.text)
			print(response["age"])

if __name__=="__main__":
	root = Tk()
	gui = Application(root)
	root.mainloop()