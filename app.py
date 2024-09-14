from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    # do the submission
    ingredients = request.form['ingredients']
    return redirect(url_for('recipes'))
    # do this render_template with recipes information

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')