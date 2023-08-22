import pytest
import requests
from pytest_bdd import scenario, given, when,then, parsers

#function to match with the feature of the scenarios
@scenario('../features/test_reqres_get.feature','Single user not found')
def test_add():
    pass

# fixure to instanvce the object with the response of the request
@pytest.fixture(scope="module")
def resp():
    return requests.get("https://reqres.in/api/users/23")

@given(parsers.parse("The user send the requests to 'https://reqres.in/api/users/23'"))
def step_1(resp):
    print("Request correctly sent")
    
@when(parsers.parse("The expected status code is '{status_code}'"))
def step_2(resp, status_code):
    #print(resp.status_code)
    #print(type(resp.status_code))
    
    if resp.status_code == int(status_code):
        print("The status",resp.status_code ,"is correct")
    else:
        assert False, "This status code isn´t correct"
        
@then("The body response is empty")
def step_3(resp):
    data = resp.json()
    print(type(data))
    
    if data == {}:
        print("The response data is OK (Empty)")
    else:
        assert False, "This response data is not the espected"