import requests

#creates an api get request to edamamapi to return recipes given ingredients (q=) and dietary/health restrictions

#user input, example values filled in here
ingredients = "corn, pasta, tomatoes"
dietIndex = [0, 1]
healthIndex = [3]


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

print(response)