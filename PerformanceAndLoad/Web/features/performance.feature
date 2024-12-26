Feature: API Performance Testing

  Scenario: Load Testing Client Registration
    Given the application is running
    When I send 100 registration requests with random data
    Then all requests should complete within 5 seconds
    And the success rate should be above 95%

  Scenario: Stress Testing Client Login
    Given the application is running
    When I send concurrent login requests with increasing load
    Then the response time should stay under 2 seconds
    And the error rate should be below 5%
