## How to run Cucumber(behave)
- Execute **one** feature file: `behave <path/to/file.feature>`
- Execute **all** feature files in the directory and sub directory: `behave`
- To get python print output use *--no-capture* option: `behave --no-capture`

## API testing with Behave and requests package
- Use 'requests' python package for get, post, put etc. API requests

## UI testing with Behave and Selenium WebDriver
- Easy UI testing with Selenium Webdriver

## How to retry failed test cases
- This can be achieved using RerunFormatter, which creates a .txt file containing failed test cases of previous run.
- Put this in your behave.ini (configuration) file :
[behave]
format   = rerun
outfiles = rerun_failing.feature
- To rerun failed scenarios, use this command: 
- behave @rerun_failing.feature

## How to run select test cases
- We can use @tags before Scenario to run specific test cases only

## Setup and Teardown
- This is done in environment.py file. This file should be within the same directory as steps folder.