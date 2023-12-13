import pytest
import pandas as pd
from fetch_recipe import convert_recipes  

sample_response = {'results': [{'id': 1, 'title': 'Recipe 1', 'servings': 4, 'readyInMinutes': 30, 'sourceUrl': 'http://www.skinnytaste.com/2015/03/healthy-salmon-quinoa-burgers.html'},
                               {'id': 2, 'title': 'Recipe 2', 'servings': 2, 'readyInMinutes': 45, 'sourceUrl': 'http://www.bonappetit.com/recipe/stellar-quinoa-burger'}]}

def test_convert_recipes():
    # Call the function with the sample response
    styled_df = convert_recipes(sample_response)

    # Check if the result is a Pandas Styler
    assert isinstance(styled_df, pd.io.formats.style.Styler), "Result should be a Pandas Styler"

    # Get the HTML representation of the Styler's underlying DataFrame
    styled_html = styled_df.data.to_html(escape=False)

    # Check if the expected columns are present in the HTML representation
    expected_columns = ['title', 'servings', 'readyInMinutes', 'sourceUrl']
    assert all(col in styled_html for col in expected_columns), "Missing columns in the HTML representation"
