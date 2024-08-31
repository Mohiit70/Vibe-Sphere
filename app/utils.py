import requests
import json
import subprocess
from flask import current_app

def run_fluvio_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

def produce_to_fluvio(topic, data):
    json_data = json.dumps(data)
    command = ['fluvio', 'produce', topic, json_data]
    run_fluvio_command(command)

def get_weather_mood(location):
    api_key = current_app.config['WEATHER_API_KEY']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
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

def get_refined_mood(weather_mood, answers):
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

def get_music_recommendation(mood):
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