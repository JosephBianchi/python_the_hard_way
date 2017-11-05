from flask import Flask
from flask import render_template #import new function knows to load .html files out of templates directory


app = Flask(__name__)

@app.route('/')
def index():
    greeting =  "I'm learning Python's Flask"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()
