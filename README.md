# to start working on this branch
1. git clone
2. git checkout base_before_login
3. python -m venv venv
4. ./venv/Scripts/Activate
5. pip install -r requirements.txt

# 1st phase: login urls + functions
1. add simple login form - elogin.html
2. add url() in all places - so login links will work
3. add function for login - no need to login yet

# 2nd phase: login - implementation
1. implement login function
2. implement logout function

# 3rd phase: register
1. implement register using UserCreationForm class

# 4th phase: single book
1. add book_detail.html
2. add function and urls to get single book using <pk> parameter in url

# 5th phase: edit book
1. add edit form to book_detail.url
2. add urls and functions for edit





# 2nd phase

# book model
Id (PK)  
Name  
Author  
Year Published  
Type (1/2/3) 


## book actions:
Add a new book  
Display all books  
Find book by name  
Remove book  


# Versions and installation
## Version 1.0 models_and_views_basic_1:
Created basic models for Books, Loans
enabled static folder - you can upload from Admin interface.
basic view for books.html

to get this version:
git clone https://github.com/ranerlich7/library_django.git

## Version 1.1

Add views
Add Forms
Add bootstrap
