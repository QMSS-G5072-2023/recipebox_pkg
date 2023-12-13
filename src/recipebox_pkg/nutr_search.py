import pandas as pd
import requests
import os
import json



def nutrient_search_recipe(api_key, nutrients):
    """
    Search for recipes based on specified nutrient parameters using the Spoonacular API.

    Parameters:
    - api_key (str): The API key for accessing the Spoonacular API.
    - nutrients (dict): Dictionary containing nutrient parameters for the recipe search.

    Returns:
    - pd.DataFrame or None: A DataFrame containing recipe information or None if no recipes are found.
    """
    if nutrients is None:
        raise ValueError("Nutrients cannot be None.")
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByNutrients'
    params = nutrients

    headers = {
        'x-rapidapi-host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com',
        'x-rapidapi-key': api_key
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        recipe = response.json()
        recipe_df = pd.DataFrame(recipe)
        return recipe_df
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None

    except pd.errors.EmptyDataError:
        print("No recipes found.")
        return None
    
    

def display_images_nutrient(recipe_df):
    for _, row in recipe_df.iterrows():
        print(f"Title: {row['title']}")
        print(f"Recipe ID: {row['id']}")
        print(f"Calories: {row['calories']:<4}; Protein: {row['protein']:<4}; Fat: {row['fat']:<4}; Carbohydrate: {row['carbs']:<4}")
        display(Image(url=row['image'], width=200))