import pytest
import requests
from pytest_bdd import scenario, given, when,then, parsers

#function to match with the feature of the scenarios
@scenario('../features/test_reqres_get.feature','Resource 2 data')
def test_add():
    pass

# fixure to instanvce the object with the response of the request
@pytest.fixture(scope="module")
def resp():
    return requests.get("https://reqres.in/api/unknown/2")

@given("The user send the request 'https://reqres.in/api/unknown/2'")
def step_1(resp):
    data = resp.json()
    print("\n\n",data)
    
@when(parsers.parse("The expected status code is '{status_code}'"))
def step_2(resp, status_code):
    #print(resp.status_code)
    #print(type(resp.status_code))
    
    if resp.status_code == int(status_code):
        print("The status",resp.status_code ,"is correct")
    else:
        assert False, "This status code isn´t correct"
        
@then(parsers.parse("The ID is '{id}'"))
def step_3(resp, id):
    
    data = resp.json()
    resource_data = data["data"]
    
    if resource_data["id"] == int(id):
        print("the ID", resource_data["id"],"is correct")
    else:
        assert False, "The given ID isn`t correct"
        
@then(parsers.parse("The NAME is '{year}'"))
def step_3(resp, year):
    
    data = resp.json()
    resource_data = data["data"]
    
    if resource_data["year"] == int(year):
        print("the YEAR", resource_data["year"],"is correct")
    else:
        assert False, "The given YEAR isn`t correct"
        
@then(parsers.parse("The color code is '{color_code}'"))
def step_3(resp, color_code):
    
    data = resp.json()
    resource_data = data["data"]
    
    if resource_data["color"] == color_code:
        print("the color code", resource_data["color"],"is correct")
    else:
        assert False, "The given color code isn`t correct"

@then(parsers.parse("The pantone value is '{pantone_value}'"))
def step_3(resp, pantone_value):
    
    data = resp.json()
    resource_data = data["data"]
    
    if resource_data["pantone_value"] == pantone_value:
        print("the pantone_value", resource_data["pantone_value"],"is correct")
    else:
        assert False, "The given pantone_value isn`t correct"
        
@then(parsers.parse("The resource url is '{url}'"))
def step_3(resp, url):
    
    data = resp.json()
    resource_data = data["support"]
    
    if resource_data["url"] == url:
        print("the url", resource_data["url"],"is correct")
    else:
        assert False, "The given url isn`t correct"