import pytest
import requests
from pytest_bdd import scenario, given, when, then, parsers

#function to match with the feature of the scenarios
@scenario('../features/test_reqres_get.feature','List Users Request')
def test_add():
    pass

# fixure to instanvce the object with the response of the request
@pytest.fixture(scope="module")
def resp():
    return requests.get("https://reqres.in/api/users?page=2")

@given(parsers.parse("The user send the requests to 'https://reqres.in/api/users?page=2'"))
def step_1(resp):
    data = resp.json()
    print("\n\n",data,"\n")
    
@then('The expected status code is 200')
def step_4(resp):
    if resp.status_code == 200:
        print("Codigo de respuesta",resp.status_code,"exitoso")
    else:
        assert False, "Codigo de respuesta incorrecto"
    
@then('The property page is 2')
def step_5(resp):
    data = resp.json()
    if data["page"] == 2:
        print("The PAGE value",data["page"],"is correct")
    else:
        assert False, "The page value isn´t correct"
    
@then('The property per_page is 6')
def step_6(resp):
    data = resp.json()
    if data["per_page"] == 6:
        print("The PER_PAGE value",data["per_page"],"is correct")
    else:
        assert False, "The PER_PAGE value isn´t correct"

@then('The propery total is 12')  
def step_7(resp):
    data = resp.json()
    if data["total"] == 12:
        print("The TOTAL value",data["total"],"is correct")
    else:
        assert False, "The VALUE value isn´t correct"

@then('The property total_pages is 2')
def step_8(resp):
    data = resp.json()
    if data["total_pages"] == 2:
        print("The TOTAL_PAGES value",data["total"],"is correct")
    else:
        assert False, "The TOTAL_PAGES value isn´t correct"
    
    