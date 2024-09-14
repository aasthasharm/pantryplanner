import requests
import json

#creates an api get request to edamamapi to return recipes given ingredients (q=) and dietary/health restrictions

#user input, example values filled in here
ingredients = "corn, pasta, tomatoes"
dietIndex = [0, 1]
healthIndex = [0, 3, 1]


#edamam api provided info
dietLabels = ["balanced", "high-fiber","high-protein","low-carb","low-fat","low-sodium"]
healthLabels = ["dairy-free","egg-free", "fish-free","gluten-free", "keto-friendly", "kosher", "peanut-free", "pork-free", "tree-nut-free", "vegan", "vegetarian"]
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
    
    # Print the extracted information for each recipe
print(all_recipes_data)
