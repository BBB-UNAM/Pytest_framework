import pytest
import requests
from pytest_bdd import scenario, given, when,then, parsers

#function to match with the feature of the scenarios
@scenario('../features/test_reqres_get.feature','User 2 data')
def test_add():
    pass

# fixure to instanvce the object with the response of the request
@pytest.fixture(scope="module")
def resp():
    return requests.get("https://reqres.in/api/users/2")

@given(parsers.parse("The user send the requests to 'https://reqres.in/api/users/2'"))
def step_1(resp):
    data = resp.json()
    if data is not None:
        print("\n\n",data,"\n")
    else:
        assert False, "The response is null"
        
@when('The expected status code is 200')
def step_2(resp):
    if resp.status_code == 200:
        print("Codigo de respuesta",resp.status_code,"exitoso")
    else:
        assert False, "Codigo de respuesta incorrecto"
        
@then(parsers.parse("The email is '{email}'"))
def step3(resp, email):
    #Convert the response object to json object
    data = resp.json()
    
    #get the "data" block of user information
    user_data = data["data"]
    
    #validate email
    if user_data["email"] == email:
        print("The email", user_data["email"], "is correct")
    else:
        assert True, "El correo electronico no es correcto"
        
@then(parsers.parse("The ID is '{id}'"))
def step4(resp, id):
    #Convert the response object to json object
    data = resp.json()
    #print(type(id)) 
    #get the "data" block of user information
    user_data = data["data"]
    
    #Validate ID
    if user_data["id"] == int(id):
        print("The id",user_data["id"],"is correct")
    else:
        assert False, "The ID isn´t correct"
        
@then(parsers.parse("The first name is '{first_name}'"))
def step5(resp, first_name):
    #Convert the response object to json object
    data = resp.json()
    #print(type(id)) 
    #get the "data" block of user information
    user_data = data["data"]
    
    #Validate ID
    if user_data["first_name"] == first_name:
        print("The first name",user_data["first_name"],"is correct")
    else:
        assert False, "The first name isn´t correct"
        
@then(parsers.parse("The last name is '{last_name}'"))
def step6(resp, last_name):
    #Convert the response object to json object
    data = resp.json()
    #print(type(id)) 
    #get the "data" block of user information
    user_data = data["data"]
    
    #Validate ID
    if user_data["last_name"] == last_name:
        print("The last name",user_data["last_name"],"is correct")
    else:
        assert False, "The last name isn´t correct"
        
@then(parsers.parse("The last name is '{last_name}'"))
def step7(resp, last_name):
    #Convert the response object to json object
    data = resp.json()
    #print(type(id)) 
    #get the "data" block of user information
    user_data = data["data"]
    
    #Validate ID
    if user_data["last_name"] == last_name:
        print("The last name",user_data["last_name"],"is correct")
    else:
        assert False, "The last name isn´t correct"
        
@then(parsers.parse("The avatar link is '{link}'"))
def step8(resp, link):
    #Convert the response object to json object
    data = resp.json()
    #print(type(id)) 
    #get the "data" block of user information
    user_data = data["data"]
    
    #Validate ID
    if user_data["avatar"] == link:
        print("The avatar link",user_data["avatar"],"is correct")
    else:
        assert False, "The avatar link isn´t correct"
        
@then(parsers.parse("The suppert url is '{support_url}'"))
def step9(resp, support_url):
    #Convert the response object to json object
    data = resp.json()
    #print(type(id)) 
    #get the "data" block of user information
    user_data = data["support"]
    
    #Validate ID
    if user_data["url"] == support_url:
        print("The support url",user_data["url"] ,"is correct")
    else:
        assert False, "The support url isn´t correct"