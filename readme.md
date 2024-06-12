# Set Up Project

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