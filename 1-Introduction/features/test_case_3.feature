Feature: Login functionality
    Scenario Outline: Check positive login functionality
       GIVEN user enters "<email>" and "<password>"
       THEN user should get response status code "<status_code>"
       Examples: Credentials
          | email               | password       | status_code |
          | eve.holt@reqres.in  | cityslicka     |  200        |
          | adam.holt@reqres.in | wrong          |  400        |
          | adam.holt@reqres.in | fail           |  200        |

