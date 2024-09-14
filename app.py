from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    # do the submission
    ingredients = request.form['ingredients']
    # dietIndex = request.form[]
    # healthIndex = request.form[]
    # Call getreq function to fetch recipes
    recipes = get_recipes(ingredients)# , dietIndex, healthIndex)

    # Pass the recipes data to the recipes template
    return render_template('recipes.html', recipes=recipes)
    # real.

def get_recipes(ingredients, dietIndex=[0], healthIndex=[10]):
    dietLabels = ["balanced", "high-fiber","high-protein","low-carb","low-fat","low-sodium"]
    healthLabels = ["dairy-free","egg-free", "fish-free","gluten-free", "keto-friendly", "kosher", "peanut-free", "pork-free", "tree-nut-free", "vegan", "vegetarian"]

    # Select diet and health restrictions
    dietRestrict = [dietLabels[i] for i in dietIndex]
    healthRestrict = [healthLabels[i] for i in healthIndex]

    app_id = "1e2add40"
    app_key = "a3f2516eac59adac59fca4f60bee47d7"

    response = requests.get(f"https://api.edamam.com/search?q={ingredients}&app_id={app_id}&app_key={app_key}&healthLabels={healthRestrict}&dietLabels={dietRestrict}").json()

    return response.get('hits', [])

def get_recipes(ingredients):
    app_id = "1e2add40"
    app_key = "a3f2516eac59adac59fca4f60bee47d7"

    response = requests.get(f"https://api.edamam.com/search?q={ingredients}&app_id={app_id}&app_key={app_key}").json()

    return response.get('hits', [])

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

if __name__ == '__main__':
    app.run(debug=True)