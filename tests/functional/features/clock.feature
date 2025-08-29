Feature: Functional testing for Clock REST API

Scenario: Check health 
 Given the Clock Rest API is running
 When the health endpoint is accessed
 Then we get an okay response

Scenario: Post a test command
 Given the Clock Rest API is running
 When a test clock command is sent
 Then we get a 201 response
