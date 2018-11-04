from flask import Flask, redirect, request
import cgi

app=Flask(__name__)

app.config['DEBUG'] = True

header = """
<!doctype html>
<html>
<head></head>"""
<body> </body>
footer= """
</html>


form = """
<form action='/'>
<label for='user_input'> User Input </label>
<input type='text' name='user_input' id='user_input' />
<input type='submit' value='enter' />
</form>




@app.route('/')
def index():
    user_input = request.args.get("user_input")
    another_input = request.args.get("another_input")
    return header + form + footer

app.run()