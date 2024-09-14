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
readable_response = json.dumps(response, indent=4)

response = requests.get(f"https://api.edamam.com/search?q={ingredients}&app_id={app_id}&app_key={app_key}&healthLabels={healthRestrict}&dietLabels={dietRestrict}").json()



for i, hit in enumerate(response['hits']):
    recipe = hit['recipe']
    
    # Extract desired information
    recipe_name = recipe['label']
    image = recipe['image']
    url = recipe['url']
    ingredients = recipe['ingredientLines']
    
    nutrients = recipe['totalNutrients']
    calories = nutrients.get('ENERC_KCAL', {}).get('quantity', 'N/A')
    sodium = nutrients.get('NA', {}).get('quantity', 'N/A')
    cholesterol = nutrients.get('CHOLE', {}).get('quantity', 'N/A')
    fat = nutrients.get('FAT', {}).get('quantity', 'N/A')
    protein = nutrients.get('PROCNT', {}).get('quantity', 'N/A')
    carbs = nutrients.get('CHOCDF', {}).get('quantity', 'N/A')
    sugar = nutrients.get('SUGAR', {}).get('quantity', 'N/A')
    fiber = nutrients.get('FIBTG', {}).get('quantity', 'N/A')
    
    # Print the extracted information for each recipe
    print(f"Recipe {i+1}:")
    print(f"Recipe Name: {recipe_name}")
    print(f"Image URL: {image}")
    print(f"Recipe URL: {url}")
    print("\nIngredients:")
    for ing in ingredients:
        print(f"- {ing}")
    
    print("\nNutritional Information:")
    print(f"Calories: {calories} kcal")
    print(f"Sodium: {sodium} mg")
    print(f"Cholesterol: {cholesterol} mg")
    print(f"Fat: {fat} g")
    print(f"Protein: {protein} g")
    print(f"Carbohydrates: {carbs} g")
    print(f"Sugar: {sugar} g")
    print(f"Fiber: {fiber} g")
    print("\n" + "="*50 + "\n")  # Separator between recipes