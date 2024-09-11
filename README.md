Weather CLI Application
Overview
This is a Python-based Command-Line Interface (CLI) application that allows users to log in, search for weather data in various locations using the OpenWeatherMap API, and store their search history in a MySQL database. The application provides secure user authentication and detailed weather search history management.

Features
User Registration & Authentication
Users can create accounts and log in.
Passwords are hashed using bcrypt for security.
Weather Search
After logging in, users can search for current weather in any location (temperature, humidity, weather conditions, wind speed).
Search History Management
Every search is logged in the MySQL database, allowing users to view their past searches along with the weather data retrieved.
Error Handling
Handles invalid inputs, API errors, and database issues gracefully.
Setup Instructions
1. Clone the Repository
bash

Verify

Open In Editor
Edit
Copy code
git clone https://github.com/your-username/weather_cli_project.git
cd weather_cli_project
2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:

For Windows:

bash

Verify

Open In Editor
Edit
Copy code
python -m venv venv
venv\Scripts\activate
For macOS/Linux:

bash

Verify

Open In Editor
Edit
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install the required Python packages:

bash

Verify

Open In Editor
Edit
Copy code
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the project root directory with the following contents:

env

Verify

Open In Editor
Edit
Copy code
OPENWEATHER_API_KEY=your_openweathermap_api_key
DB_USER=sss_assignment_sep24
DB_PASSWORD=doitnow
DB_HOST=localhost
DB_NAME=weather_db
Replace your_openweathermap_api_key with your actual OpenWeatherMap API key.

5. Set Up the MySQL Database
Run the following SQL commands to set up the database:

sql

Verify

Open In Editor
Edit
Copy code
CREATE DATABASE weather_db;
USE weather_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE search_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    location VARCHAR(255),
    temperature FLOAT,
    humidity INT,
    weather_conditions VARCHAR(255),
    wind_speed FLOAT,
    search_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
6. Run the Application
Run the application using the following command:

bash

Verify

Open In Editor
Edit
Copy code
python weather_cli.py
Usage Instructions
Register or Log in
When you run the application, you'll be prompted to register a new account or log in with existing credentials.

Search for Weather
After logging in, you can search for current weather data by entering a location (e.g., "London").

View Search History
You can view your search history, displaying past queries along with the corresponding weather data.

Example Flow
Register
bash

Verify

Open In Editor
Edit
Copy code
$ python weather_cli.py
1. Register
2. Login
Choose an option: 1
Enter username: your_username
Enter password: your_password
User registered successfully!
Login and Search
bash

Verify

Open In Editor
Edit
Copy code
$ python weather_cli.py
1. Register
2. Login
Choose an option: 2
Enter username: your_username
Enter password: your_password
Login successful!
Enter the location to search for weather: New York
Weather data for New York:
- Temperature: 22°C
- Humidity: 60%
- Weather Conditions: clear sky
- Wind Speed: 3.5 m/s
View Search History
bash

Verify

Open In Editor
Edit
Copy code
Do you want to view your search history? (y/n): y
1. New York - 22°C, clear sky, Humidity: 60%, Wind: 3.5 m/s, Time: 2023-10-01 12:34:56
Project Structure

Verify

Open In Editor
Edit
Copy code
weather_cli_project/
├── weather_cli.py        # Main application script
├── .env                  # Environment variables file
├── requirements.txt      # List of dependencies
├── README.md             # Documentation
└── venv/                 # Python virtual environment
Dependencies
The project requires the following Python packages:

requests
bcrypt
python-dotenv
mysql-connector-python
These are listed in the requirements.txt file and can be installed using:

bash

Verify

Open In Editor
Edit
Copy code
pip install -r requirements.txt
Database Schema
users
Stores user credentials (username and hashed password).

search_history
Logs each weather search, linked to the user's account, along with search timestamp and weather data.
