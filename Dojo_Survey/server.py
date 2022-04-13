from xml.etree.ElementTree import Comment
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'Can-I-Has-Survey-Meow_Prease'


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/results', methods = ['POST'])
def user_results():
    print("Survey Received")
    name = request.form['name'],
    location = request.form['location'],
    language = request.form['language'],
    comment = request.form['comment']
    print(name,location,language,comment)
    return render_template("results.html", name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])
# redirect isn't functioning on button click
    return redirect("/")

# not sure how to have results page return back to home page
# @app.route("/reset")
# def reset_session():
#     session.clear()
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
