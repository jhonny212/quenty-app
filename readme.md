# Set Up Project
## Notes
- For Django REST Framework use the prefix "/api/" for example "api/books" or "api/authors"
- Put your .env file at the same location of the settings.py file if this doesn't work send me a message

## Installation

- `clone the next repository: https://github.com/jhonny212/quenty-app.git`
- Install the required dependencies using `pip install -r requirements.txt`
- Create an .env file using the .envexample as a template.
- Create a database called as you set in your env file.

## Start
- Run the migrations using the `python manage.py migrate`
- Start the project using the `python manage.py runserver`

# Custom commands
- `python .\manage.py command`
    - This command will execute 3 queries:
        - Retrieve all authors who have written a book with a rating greater than 4.5.
        - Retrieve all books published in the last year.
        - Calculate the average rating of books for each author and order the authors by their average rating in descending order.

# Run Tests
- In this case for the structure of my project you must run the following command: coverage run manage.py test apps --pattern="test*.py"
- Check coverage: coverage report or coverage html
