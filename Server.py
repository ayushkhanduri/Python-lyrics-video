from flask import Flask , render_template , jsonify,request
from flask.views import MethodView
from multiprocessing import Process
from ImageProcessing import ChangeImage


class SomeRoutes(MethodView):
	def get(self):
		return render_template('hello.html');

class User(MethodView):
	def get(self):
		print("request received")
		return {"name": "ayush",age:22}
	
	def post(self):
		ChangeImageObject= ChangeImage()
		ChangeImageObject.processString(request.data)
		return jsonify({"name": "ayush","age":22})

def main():
	app = Flask(__name__)
	app.add_url_rule('/',view_func = SomeRoutes.as_view('root'))
	app.add_url_rule('/allUsers',view_func= User.as_view('getUsers'))
	app.run()

main()