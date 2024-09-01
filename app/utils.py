import requests
import json
import subprocess
from flask import current_app

def run_fluvio_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        result.check_returncode()
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Fluvio command failed: {e}")
        return None

def produce_to_fluvio(topic, data):
    try:
        json_data = json.dumps(data)
        command = ['fluvio', 'produce', topic, json_data]
        output = run_fluvio_command(command)
        if output is None:
            raise Exception(f"Failed to produce to Fluvio topic {topic}")
    except Exception as e:
        print(f"Error producing to Fluvio: {e}")

def get_weather_mood(location):
    try:
        api_key = current_app.config['WEATHER_API_KEY']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        
        weather_id = data['weather'][0]['id']
        if weather_id < 300:
            mood = 'Stormy'
        elif weather_id < 600:
            mood = 'Rainy'
        elif weather_id < 700:
            mood = 'Snowy'
        elif weather_id == 800:
            mood = 'Sunny'
        else:
            mood = 'Cloudy'
        
        # Produce weather data to Fluvio
        produce_to_fluvio('weather-data', {'location': location, 'mood': mood})
        
        return mood
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return "Error"
    except KeyError:
        print("Unexpected data format received from weather API")
        return "Error"

def get_refined_mood(weather_mood, answers):
    try:
        day_rating = int(answers['day_rating'])
        energy_level = answers['energy_level']
        
        if day_rating > 3 and energy_level == 'High':
            refined_mood = 'Energetic'
        elif day_rating < 3 and weather_mood in ['Rainy', 'Cloudy']:
            refined_mood = 'Melancholic'
        else:
            refined_mood = weather_mood
        
        # Produce refined mood data to Fluvio
        produce_to_fluvio('refined-mood', {'weather_mood': weather_mood, 'refined_mood': refined_mood})
        
        return refined_mood
    except Exception as e:
        print(f"Error refining mood: {e}")
        return weather_mood

def get_music_recommendation(mood):
    try:
        recommendations = {
            'Energetic': 'Upbeat pop playlist',
            'Melancholic': 'Slow jazz playlist',
            'Sunny': 'Feel-good summer hits',
            'Rainy': 'Acoustic covers playlist',
            'Stormy': 'Epic movie soundtracks',
            'Snowy': 'Cozy winter classics',
            'Cloudy': 'Indie folk playlist'
        }
        recommendation = recommendations.get(mood, 'General mood playlist')
        
        # Produce recommendation data to Fluvio
        produce_to_fluvio('recommendations', {'mood': mood, 'recommendation': recommendation})
        
        return recommendation
    except Exception as e:
        print(f"Error getting music recommendation: {e}")
        return "General mood playlist"
