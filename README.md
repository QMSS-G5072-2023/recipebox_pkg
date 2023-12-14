# recipebox_pkg

A Python package designed for fetching information about recipes.

## Installation

```bash
$ pip install recipebox_pkg
```
## Features

- **Explore Recipe Details:** Access comprehensive information about recipes through user queries.

- **Nutrition Insights:** Retrieve detailed nutritional information tailored to specific dietary constraints.

- **Ingredient Details:** Discover essential details about ingredients required for a recipe.

- **Visualize the Dish:** View images showcasing the appearance of the prepared dish.

## Usage

```python
# Import the necessary function from recipebox_pkg
from recipebox_pkg import fetch_recipe

# Replace the empty string with your actual API key
api_key = 'your_actual_api_key'

# Use the fetch_recipe.search_recipes function to search for recipes 
recipes = fetch_recipe.search_recipes(api_key, 'pizza')

# Convert the retrieved recipes into a Pandas DataFrame
recipes_retrieved = fetch_recipe.convert_recipes(recipes)
```

## Dependencies

This package requires the following Python libraries:
- Pandas
- Requests
- IPython
To install these libraries, run:

```bash
pip install pandas requests IPython
```
## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`recipebox_pkg` was created by Yuchen An. It is licensed under the terms of the MIT license.

## Credits

`recipebox_pkg` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Links

[Documentation](file:///Users/anyuchen/Desktop/recipebox_pkg/docs/_build/html/index.html)
[Recipe-Food-Nutrition API Documentation](https://spoonacular.com/food-api/docs)

