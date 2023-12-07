Feature: API Tests on Reqres Public API

Scenario: Verify a successful user retrieval
    Given a valid API endpoint for user retrieval
    When a GET request is made
    Then the status code should be 200
    And the response message should contain "Successful"


