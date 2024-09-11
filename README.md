Weather CLI Application
Overview
This project is a Python-based Command-Line Interface (CLI) application that allows users to log in, search for weather data in various locations using the OpenWeatherMap API, and store their search history in a MySQL database. The application provides user authentication and search history management while ensuring secure handling of user information.

Features
User Registration & Authentication: Users can create accounts and log in securely. Passwords are hashed using bcrypt for security.
Weather Search: Once logged in, users can search for current weather information, including temperature, humidity, weather conditions, and wind speed.
Search History Management: Every search is logged in a MySQL database, allowing users to view their past searches along with the weather data retrieved at the time.
Error Handling: Handles invalid inputs, API errors, and database connection issues gracefully.
Project Structure
bash
Copy code
weather_cli_project/
├── weather_cli.py        # Main application script
├── .env                  # Environment variables (API key, DB credentials)
├── venv/                 # Python virtual environment
├── requirements.txt      # List of dependencies
└── README.md             # Documentation file
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/weather_cli_project.git
cd weather_cli_project
2. Set Up a Virtual Environment
It's recommended to run the project in a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
source venv/Scripts/activate   # Windows
# or
source venv/bin/activate       # macOS/Linux
3. Install Dependencies
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the project root directory and add the following variables:

env
Copy code
OPENWEATHER_API_KEY=your_openweathermap_api_key
DB_USER=sss_assignment_sep24
DB_PASSWORD=doitnow
DB_HOST=localhost
DB_NAME=weather_db
Replace your_openweathermap_api_key with your actual OpenWeatherMap API key.

5. Set Up MySQL Database
Create a MySQL database and apply the following schema:

sql
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
Once the environment is set up, run the application using the following command:

bash
Copy code
python weather_cli.py
Usage Instructions
Register or Log in:
The CLI will prompt you to either register a new account or log in with existing credentials.

Search for Weather:
After logging in, you can search for weather data by entering a location (e.g., "London").

View Search History:
You can view your search history, displaying past queries along with the corresponding weather data at the time.

Example Flow
Register/Login:

yaml
Copy code
$ python weather_cli.py
1. Register
2. Login
Choose an option: 1
Enter username: example_user
Enter password: example_password
User registered successfully!
Search for Weather:

yaml
Copy code
Enter the location to search for weather: New York
Weather data for New York:
Temperature: 21.3°C
Humidity: 70%
Weather Conditions: clear sky
Wind Speed: 3.5 m/s
View Search History:

sql
Copy code
View your search history:
1. New York - 21.3°C, clear sky, Humidity: 70%, Wind: 3.5 m/s
Database Schema
users: Stores user information (username, password hash).
search_history: Logs each weather search, linked to the user account, along with search timestamp and weather data.
Error Handling
The application has robust error handling for:

Invalid login attempts.
Errors in API requests (e.g., invalid location or API key).
Database connection issues.
Missing API keys or environment variables.
Bonus Features
Delete Search History: Users can delete specific search entries from their history.
Profile Updates: Users can update their username or password.
Extended Weather Data: The application can be extended to fetch 5-day weather forecasts or other weather-related data.
Future Enhancements
Support for additional weather queries, such as multi-day forecasts.
Improve scalability and performance by optimizing database schema and queries.
Conclusion
This project demonstrates interaction with external APIs, secure user authentication, database management, and robust error handling in a Python-based CLI application. The modular design makes it easy to add new features or extend the existing functionality.
