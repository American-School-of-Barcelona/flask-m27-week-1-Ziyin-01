from flask import Flask , render_template, request

app = Flask(__name__)

# TODO: Add your routes below this line

tasks = [
    {"title" : "Complete math practice"},
    {"title" : "Complete Paper 2 draft for English"},
    {"title" : "Complete financial report before Wednesday"},
]

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/task")
def task():
    return render_template("task.html", tasks=tasks)

@app.route("/here")
def here():
    return render_template("here.html")

@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "world"))

@app.route("/index")
def index():
    return render_template("index.html")

#@app.route("/", methods=["GET", "POST"])
#def index():
    #if request.method == "POST":
        #return render_template("about.html", name=request.form.get("name", "world"))
    #else:
        #return render_template("index.html")

#if __name__ == "__main__":
    #app.run(debug=True)
