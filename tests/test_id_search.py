import pandas as pd
import pytest
from id_search import Recipe_id  # Replace 'your_module' and 'YourClass' with the actual module and class names

# Sample data for testing
sample_input_dict = {
    'category1': {'attribute1': 'value1', 'attribute2': 'value2'},
    'category2': {'attribute1': 'value3', 'attribute2': 'value4'}
}

def test_dict_reader():
    # Provide sample values for 'id' and 'api_key'
    sample_id = '123456'
    sample_api_key = '987654321'

    # Create an instance of the class containing dict_reader method
    instance = Recipe_id(sample_id, sample_api_key)

    # Call the dict_reader method with the sample input
    result_series = instance.dict_reader(sample_input_dict)

    # Check if the result is a Pandas Series
    assert isinstance(result_series, pd.Series), "Result should be a Pandas Series"

    # Check if the keys of the result_series match the expected keys
    expected_keys = ['category1_attribute1', 'category1_attribute2', 'category2_attribute1', 'category2_attribute2']
    assert list(result_series.index) == expected_keys, "Incorrect keys in the result_series"

    # Check if the values of the result_series match the expected values
    expected_values = ['value1', 'value2', 'value3', 'value4']
    assert list(result_series.values) == expected_values, "Incorrect values in the result_series"



# Sample data for testing
sample_instruction_list = [
    {'step': 'Preheat the oven to 350°F.'},
    {'step': 'In a large mixing bowl, combine flour, sugar, and baking powder.'},
    {'step': 'Add eggs and vanilla extract to the mixture and stir until well combined.'},
    {'step': '...'}
]

def test_convert_instruction(capsys):
    # Create an instance of the class containing convert_instruction method
    instance = Recipe_id('123456', '987654321')  # Provide sample values for 'id' and 'api_key'

    # Call the convert_instruction method with the sample input
    instance.convert_instruction(sample_instruction_list)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the printed output contains the expected information
    expected_output = """Here are the steps to prepare recipe 123456:
1. Preheat the oven to 350°F.

2. In a large mixing bowl, combine flour, sugar, and baking powder.

3. Add eggs and vanilla extract to the mixture and stir until well combined.

4. ...

"""
    assert captured.out == expected_output, "Incorrect output from convert_instruction method"
