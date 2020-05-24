Roomie users,

The following program allows students at The College of New Jersey to find a empty room in a building of their choosing.

This project requires the following tools:

Python - The programming language
virtualenv - A tool for creating isolated Python environments.

For windows machines:
Step 1. Extract and open the downloaded code.

	cd pathtocode\Roomie

Step 2. Create a Virtual Environment and install Dependencies.

	virtualenv venv
	venv\Scripts\activate

Next, we need to install the project dependencies, which are listed in requirements.txt

	(venv) > pip install -r requirements.txt

Step 3. Run the Roomie program
	
	python Roomie.py

Everyone on the roomie team hopes that the application can be as useful to others as it was to us.

As this is a prototype, the rooms and times are not completely accurate for Spring 2019 semester.