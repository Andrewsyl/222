# Weather Sensor App

- Full-stack weather app
- App allows users to add sensors based on location.
- Then based on the location, an API call is run in the background to collect real-life data.
- This data is then stored in the apps database.
- The database can then be queried for data to give average temperature, humidity, wind speed etc.

##  Built With

* Python
* Flask
* HTML
* CSS
* SQLite
* Bootstrap
* Javascript

# Installation

Prerequisites:

- Python
- Pip
- Git

1. In a terminal, cd to folder location of your choice
2. Enter
 ```
  git clone https://github.com/Andrewsyl/222.git
  ```
4. cd to 222 folder and enter
```
pip install -r requirements.txt
```
6. To initialise the database:

- run python in the terminal and enter
```
from app import db
```
Then
```
db.create_all()
```
Followed by
```
exit()
```

Once done and still in the 222 folder, run python app.py and open your browser at address http://127.0.0.1:5000

## Reviewing Code

* Main file is app.py. All routing and major functionality is located here.

## Improvements

#### Functionality

* Improve the error handling. Currently there is some handling that flags the user if city + country names are not letters. Instead I would add a JSON file with a list of cities to choose from.
* One of the main criteria in the test was querying, I would add a dropdown list allowing the user to select what data they want to reviece e.g temp and rain fall.

#### Code

* Separate Models into their own file. As the project grows the app.py file would grow too large to manage.
* Breakup functions in app.py. Some functions are doing multiple jobs. All should have one job (where possible) and given comments to explain said job.
* I added an API Key for gathering external weather data. I would remove this and ask the user to fetch their own Key.

#### Testing

* Structure the testing into Unit Tests and Functional Tests:
* Unit Tests will test the Models and data being sent to them.
* Functional tests will test the Views for nominal conditions (GET, POST, etc.) for a view function. Or any invalid data is passed to a view function.

* Use the assert function for the Models to test data being saved to database is correct. e.g 
assert user.city == 'Galway'
assert user.country != 'Ireland'


* Current test would be imporved by removing redundant code. Some tests are similar and could be combined using a loop.



