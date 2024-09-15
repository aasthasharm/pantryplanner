from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)
ingredients = ""

@app.route('/')
def index():
    global ingredients
    if ingredients != "":
        ingredients = ""
    return render_template('home.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    global ingredients
    # do the submission
    if ingredients == "":
        ingredients = request.form['ingredients']
    # dietIndex = request.form[]
    # healthIndex = request.form[]
    # Call getreq function to fetch recipes
    recipes, recipe_images = get_recipes(ingredients)  # , dietIndex, healthIndex)
    # print(recipes[1])

    # Pass the recipes data to the recipes template
    return render_template('recipes.html', recipes=recipes, backgroundImages=recipe_images)
    # real.


def get_recipes(ingredients, dietIndex=[6], healthIndex=[11]):
    # edamam api provided info
    dietLabels = ["balanced", "high-fiber", "high-protein", "low-carb", "low-fat", "low-sodium", None]
    healthLabels = ["dairy-free", "egg-free", "fish-free", "gluten-free", "keto-friendly", "kosher", "peanut-free",
                    "pork-free", "tree-nut-free", "vegan", "vegetarian", None]
    app_id = "1e2add40"
    app_key = "a3f2516eac59adac59fca4f60bee47d7"

    # select diet and health restrictions
    dietRestrict = []
    healthRestrict = []

    for i in range(len(dietIndex)):
        dietRestrict.append(dietLabels[dietIndex[i]])

    for j in range(len(healthIndex)):
        healthRestrict.append(healthLabels[healthIndex[j]])
    
    if (type(ingredients) is list):
        ingredients = ','.join(ingredients)
    ingredients = ingredients.replace(" ","%20").replace(",","%20")
    health = ""
    if (None not in healthRestrict):
        for string in healthRestrict:
            health += "&health=" + string
    diet = ""
    if (None not in dietRestrict):
        for string in dietRestrict:
            diet += "&diet=" + string

    print(f"https://api.edamam.com/search?q={ingredients}&app_id={app_id}&app_key={app_key}{diet}{health}")

    response = requests.get(
        f"https://api.edamam.com/search?q={ingredients}&app_id={app_id}&app_key={app_key}{diet}{health}").json()

    all_recipes_data = []
    recipe_images = []

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
        recipe_images.append(recipe['image'])

    return all_recipes_data, recipe_images


@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/update', methods=['GET','POST'])
def update():
    # we have ingredients
    # we need to get dietIndex and healthIndex as arrays with index values in them
    # then we run get_recipes with ingredients, dietIndex, and healthIndex
    health_limits = request.form.getlist('health-limits')
    print(health_limits)
    diets = request.form.getlist('diets')
    print(diets)

    health_options = ["dairy-free", "egg-free", "fish-free", "gluten-free", "keto-friendly", "kosher", 
                      "peanut-free", "pork-free", "tree-nut-free", "vegan", "vegetarian"]
    diet_options = ["balanced", "high-fiber", "high-protein", "low-carb", "low-far", "low-sodium"]

    healthIndex = []
    dietIndex = []

    for limit in health_limits:
        if limit in health_options:
            healthIndex.append(health_options.index(limit))
    for diet in diets:
        if diet in diet_options:
            dietIndex.append(diet_options.index(diet))

    print(healthIndex)

    recipes, recipe_images = get_recipes(ingredients, dietIndex, healthIndex)
    return render_template('recipes.html', recipes=recipes, backgroundImages=recipe_images)

if __name__ == '__main__':
    app.run(debug=True)
