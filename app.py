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

def get_recipes(ingredients, dietIndex=[6], healthIndex=[11]):
    #edamam api provided info
    dietLabels = ["balanced", "high-fiber","high-protein","low-carb","low-fat","low-sodium", None]
    healthLabels = ["dairy-free","egg-free", "fish-free","gluten-free", "keto-friendly", "kosher", "peanut-free", "pork-free", "tree-nut-free", "vegan", "vegetarian", None]
    app_id = "1e2add40"
    app_key = "a3f2516eac59adac59fca4f60bee47d7"

    #select diet and health restrictions
    dietRestrict = []
    healthRestrict = []

    for i in range(len(dietIndex)):
        dietRestrict.append(dietLabels[dietIndex[i]])

    for j in range(len(healthIndex)):
        healthRestrict.append(healthLabels[healthIndex[j]])

    response = requests.get(f"https://api.edamam.com/search?q={ingredients}&app_id={app_id}&app_key={app_key}&healthLabels={healthRestrict}&dietLabels={dietRestrict}").json()


    all_recipes_data = []

    for i, hit in enumerate(response['hits']):
        recipe = hit['recipe']
        
        recipe_data = {
            "recipe_name": recipe['label'],
            "image": recipe['image'],
            "url": recipe['url'],
            "ingredients": recipe['ingredientLines'],
            "calories": recipe['totalNutrients'].get('ENERC_KCAL', {}).get('quantity', 'N/A'),
            "sodium": recipe['totalNutrients'].get('NA', {}).get('quantity', 'N/A'),
            "cholesterol": recipe['totalNutrients'].get('CHOLE', {}).get('quantity', 'N/A'),
            "fat": recipe['totalNutrients'].get('FAT', {}).get('quantity', 'N/A'),
            "protein": recipe['totalNutrients'].get('PROCNT', {}).get('quantity', 'N/A'),
            "carbs": recipe['totalNutrients'].get('CHOCDF', {}).get('quantity', 'N/A'),
            "sugar": recipe['totalNutrients'].get('SUGAR', {}).get('quantity', 'N/A'),
            "fiber": recipe['totalNutrients'].get('FIBTG', {}).get('quantity', 'N/A'),
        }
        all_recipes_data.append(recipe_data)

    return all_recipes_data


@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

if __name__ == '__main__':
    app.run(debug=True)