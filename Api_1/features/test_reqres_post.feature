Feature: This feature was done to test all POST services in reqres

    Scenario: Add Alberto leader user to the DB
        Given The user has the below json:
            """
            {
                "name": "morpheus",
                "job": "leader"
            }
            """
        When The user do a request for ''
            