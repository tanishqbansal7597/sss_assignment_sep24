import requests
import sqlite3
import bcrypt
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('weather_cli.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS search_history (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        location TEXT,
                        weather_data TEXT,
                        FOREIGN KEY (user_id) REFERENCES users (id))''')
    conn.commit()
    conn.close()

# Register a new user
def register_user():
    conn = sqlite3.connect('weather_cli.db')
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    conn.close()

# User login
def login_user():
    conn = sqlite3.connect('weather_cli.db')
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        user_id, stored_password = result
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            print("Login successful!")
            return user_id
        else:
            print("Invalid password.")
    else:
        print("User not found.")
    conn.close()
    return None

# Fetch weather data
def fetch_weather(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Error: Could not retrieve weather data.")
        return None

# Store search history
def store_search(user_id, location, weather_data):
    conn = sqlite3.connect('weather_cli.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO search_history (user_id, location, weather_data) VALUES (?, ?, ?)",
                   (user_id, location, str(weather_data)))
    conn.commit()
    conn.close()

# Main CLI Function
def main():
    init_db()  # Initialize database

    print("1. Register")
    print("2. Login")
    choice = input("Choose an option: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        user_id = login_user()
        if user_id:
            location = input("Enter the location to search for weather: ")
            weather_data = fetch_weather(location)
            if weather_data:
                print(f"Weather in {location}: {weather_data['weather'][0]['description']}, Temp: {weather_data['main']['temp']}°C")
                store_search(user_id, location, weather_data)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
