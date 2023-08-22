import pytest
import requests
from pytest_bdd import scenario, given, when, then, parsers

@scenario('../features/test_basic.feature','this is a basic test')
def test_add_two():
    pass
@pytest.fixture
def examplefixure():
    yield "hola"
    return "adios"

@given("step one")
def step_1(examplefixure):
    print(examplefixure)
    #print(examplefixure)
    
@then("step two")
def step_2(examplefixure):
    print(examplefixure, examplefixure)