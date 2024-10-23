import requests
import json

# URL to fetch the JSON data
url = "https://dummyjson.com/recipes"

# Fetch the JSON data from the URL
response = requests.get(url)
data = response.json()  # Parse the response JSON data

# Define the Recipe class (same as before)
class Recipe:
    def __init__(self, id, name, ingredients, instructions, prep_time, cook_time, servings, difficulty, cuisine, calories_per_serving, tags, user_id, image, rating, review_count, meal_type):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.difficulty = difficulty
        self.cuisine = cuisine
        self.calories_per_serving = calories_per_serving
        self.tags = tags
        self.user_id = user_id
        self.image = image
        self.rating = rating
        self.review_count = review_count
        self.meal_type = meal_type

    def __str__(self):
        return f"Recipe: {self.name} (ID: {self.id})\n" \
               f"Difficulty: {self.difficulty} | Cuisine: {self.cuisine}\n" \
               f"Servings: {self.servings} | Prep time: {self.prep_time} min | Cook time: {self.cook_time} min\n" \
               f"Calories per serving: {self.calories_per_serving}\n" \
               f"Rating: {self.rating} ({self.review_count} reviews)\n" \
               f"Meal Type: {', '.join(self.meal_type)}\n" \
               f"Ingredients: {', '.join(self.ingredients)}\n" \
               f"Instructions:\n" + "\n".join(f"{i+1}. {step}" for i, step in enumerate(self.instructions))

# Create a list of Recipe objects from the fetched data
recipes = [Recipe(
    id=recipe['id'],
    name=recipe['name'],
    ingredients=recipe['ingredients'],
    instructions=recipe['instructions'],
    prep_time=recipe['prepTimeMinutes'],
    cook_time=recipe['cookTimeMinutes'],
    servings=recipe['servings'],
    difficulty=recipe['difficulty'],
    cuisine=recipe['cuisine'],
    calories_per_serving=recipe['caloriesPerServing'],
    tags=recipe['tags'],
    user_id=recipe['userId'],
    image=recipe['image'],
    rating=recipe['rating'],
    review_count=recipe['reviewCount'],
    meal_type=recipe['mealType']
) for recipe in data['recipes']]