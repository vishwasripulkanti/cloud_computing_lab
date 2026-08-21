from flask import Flask 
app=Flask(__name__)
@app.route("/")
def home():
	<html>
	<body>
	<h1>Hello Rgukt</h1>
	</body>
	</html>
	return "flask application running successfully"
	
if  __name__==('__main__'):
	app.run('0.0.0.0',5000) #host=0.0.0.0 ; port=5000

