from flask import render_template, request, jsonify
from app import create_app
from app.utils import get_weather_mood, get_refined_mood, get_music_recommendation

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_mood', methods=['POST'])
def get_mood():
    data = request.json
    location = data.get('location')
    answers = data.get('answers')
    
    weather_mood = get_weather_mood(location)
    refined_mood = get_refined_mood(weather_mood, answers)
    recommendation = get_music_recommendation(refined_mood)
    
    return jsonify({
        'mood': refined_mood,
        'recommendation': recommendation
    })