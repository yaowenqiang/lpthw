from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
@app.route('/')

def hello_world():
    greeting = "Hello World"
    name = request.args.get('name','nobody')
    if name:
        greeting = f"Hello  {name}"
    else:
        greeting = "Hello  world"

    return render_template("index.html",greeting=greeting)

@app.route('/hello' ,methods=["GET","POST"])

def index():
    greeting = "Hello World"
    if request.method == "POST":
        name = request.form["name"]
        greet = request.form["greet"]

        greeting = f"{greet} {name}"

        return render_template("index.html",greeting=greeting)
    else:

        return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
