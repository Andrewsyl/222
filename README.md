# Weather Sensor App

- Full-stack weaher app
- App allows users to add sensors based on loaction.
- Then based on the location, an API call is run in the background to collecting real-life data.
- This data is then stored in the apps databased. 
- The database can then be quired for data to give average temperateure, humidity windspee etc.

##  Built With

* Python
* Flask
* HTML
* CSS
* SQLite
* CSS
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
```
db.create_all()
```
```
exit()
```

Once done and still in the 222 folder, run python app.py and open your browser at address http://127.0.0.1:5000

## Reviewing Code

* Main file is app.py. All routing and major functionality is located here. 
