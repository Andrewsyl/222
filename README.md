# Weather Sensor App

- App allows users to add sensors based on loaction.
- These sensors then connect to a real-time API that pulls data into the app database.
- On each query that weather data is collected and stored in the database.
- The app then allows for querys of data to give average temperateure, humidity windspee etc.

# Installation

Prerequisites:

- Python
- Pip
- Git

1. In a terminal, cd to folder location of your choice
2. Enter git clone https://github.com/Andrewsyl/222.git
3. cd to 222 folder and enter 'pip install -r requirements.txt'.
4. To initialise the database:

- run python in the terminata and enter 'from app import db'.
- then 'db.create_all()'
- followed by 'exit()'

Once done and still in the 222 folder, run python app.py and open your browser at address http://127.0.0.1:5000
