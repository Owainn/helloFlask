from flask import Flask, render_template                 # import de l’objet Flask

app = Flask(__name__)                   # instantiation application

@app.route("/")                         # association d'une route (URL) avec la fonction suivante
def home():
    return render_template("home.html",
                            name="Kévinou")

@app.route("/about/")
def about():
    page_title = "About"
    my_content = "/static/text_about.txt"
    return render_template("about.html",
                            my_title=page_title,
                            my_content=my_content)

@app.route("/form/")
def form():
    page_title = "form"
    return render_template("form.html",
                            my_title=page_title,
                            my_content="Hello World")

app.run()                               # demarrage de l'appli
