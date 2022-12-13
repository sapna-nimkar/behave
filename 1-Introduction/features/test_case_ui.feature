Feature: UI Verify Title
  @this
  Scenario: Verify title of the webpage
    GIVEN user navigates to "https://behave.readthedocs.io/en/stable/"
    THEN title of the page is "Welcome to behave! — behave 1.2.6 documentation"
