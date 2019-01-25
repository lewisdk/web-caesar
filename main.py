from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form action="/" method="post">
       <label>
            Rotate by:
            <input type="text" name="rot"/>
        </label>
        <label>
        <textarea rows="10" cols="50"input type="submit" name="text"/>
            {0}
        </textarea>
        </label>
        <input type="submit" value="Submit"/>
    </form>
    </body>
</html>
"""

@app.route("/", methods=["post"])
def encrypt():
    encrypt = request.form["text"]
    rotate = request.form["rot"]
    rot = int(rotate)
    coded_text = rotate_string(encrypt, rot)
    final_text = form.format(coded_text)
    return final_text

@app.route("/")
def index():
    return form.format("")

app.run()