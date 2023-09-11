#test_reqres_get4_steps

import pytest
import requests
from pytest_bdd import scenario, given, when,then, parsers

#function to match with the feature of the scenarios
@scenario('../features/test_reqres_post.feature','Add Alberto leader user to the DB')
def test_add():
    pass

@given(parsers.parse("The user has the below json:\n{json_request}"))
def step_1(json_request):
    print("\n\n",json_request)
    print(type(json_request))