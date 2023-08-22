Feature: This Featre was done to test all GET requests

    Scenario: List Users Request
        Given The user send the requests to 'https://reqres.in/api/users?page=2'
        Then The expected status code is 200
        Then The property page is 2
        Then The property per_page is 6
        Then The propery total is 12
        Then The property total_pages is 2

    Scenario: User 2 data
        Given The user send the requests to 'https://reqres.in/api/users/2'
        When The expected status code is 200
        Then The email is 'janet.weaver@reqres.in'
        Then The ID is '2'
        Then The first name is 'Janet'
        Then The last name is 'Weaver'
        Then The avatar link is 'https://reqres.in/img/faces/2-image.jpg'
        Then The suppert url is 'https://reqres.in/#support-heading'

    Scenario: Single user not found
        Given The user send the requests to 'https://reqres.in/api/users/23'
        When The expected status code is '404'
        Then The body response is empty

    Scenario: Resource 2 data
        Given The user send the request 'https://reqres.in/api/unknown/2'
        When The expected status code is '200'
        Then The ID is '2'
        Then The NAME is '2001'
        Then The color code is '#C74375'
        Then The pantone value is '17-2031'
        Then The resource url is 'https://reqres.in/#support-heading'