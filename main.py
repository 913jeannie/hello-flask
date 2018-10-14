from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!doctype html>
<html>
    <body>
        <form action="/hello" METHOD="post">
            <label for="first-name">First Name:</label>
            <input type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods=['post'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'
app.run()

time_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value='{hours}' />
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input name="minutes" type="text" value='{minutes}' />
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="Validate" />
    </form>r43e32?
    """

@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours="", hours_error="", 
    minutes="", minutes_error="")



app.run()