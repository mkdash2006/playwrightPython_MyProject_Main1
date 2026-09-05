import json
import pytest

@pytest.mark.smoke5
def test_jsonhandling():
    with open('testdata\\creds.json') as data:
        formated_data=json.load(data)   # read the data and store
        print(formated_data['email'])
        
        