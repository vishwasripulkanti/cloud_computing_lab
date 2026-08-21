from flask import Flask 
app=Flask(__name__)
@app.route("/")
def home():
	
	return """
	<html>
	<body>
	<h1>hello worls</h1>
	</body>
	</html>
	"""
	
	
if  __name__==('__main__'):
	app.run('0.0.0.0',5000) #host=0.0.0.0 ; port=5000

