import xml.etree.ElementTree as ET
import os
from PIL import Image,ImageDraw,ImageFont

class ChangeImage():
	def __init__(self):
		pass

	def processString(self,lyrics):
		print("processString")
		root = ET.fromstring(lyrics)
		self.createImages(root)


	def createImages(self,root):
		color = ""
		try:
			color = root.attrib["bgColor"]
		except KeyError:
			color = "black"
		for child in root:
			img = None
			img = Image.new("RGB",(800,800),color)
			self.writeText(img,child)

	def writeText(self,img,child):
		draw = ImageDraw.Draw(img)
		font = ImageFont.load_default()
		draw.text((50,20),child.text,(255,255,255),font=font)
		img.save(os.getcwd() + "/Images/" + child.attrib["number"] + ".jpeg","Jpeg")