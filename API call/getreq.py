import requests

#creates an api get request to edamamapi to return recipes given ingredients (q=) and dietary/health restrictions


ingredients = "corn, pasta, tomatoes"
app_id = "1e2add40"
app_key = "a3f2516eac59adac59fca4f60bee47d7"

response = requests.get(f"https://api.edamam.com/search?q={ingredients}&app_id={app_id}&app_key={app_key}").json()

print(response)