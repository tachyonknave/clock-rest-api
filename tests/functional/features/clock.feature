Feature: Functional testing for Clock REST API

Scenario: Check health 
 Given the Clock Rest API is running
 When the health endpoint is accessed
 Then we get an okay response 