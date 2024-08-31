document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('mood-form');
    const resultDiv = document.getElementById('result');
    const moodSpan = document.getElementById('mood');
    const recommendationSpan = document.getElementById('recommendation');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const location = document.getElementById('location').value;
        const dayRating = document.getElementById('day-rating').value;
        const energyLevel = document.getElementById('energy-level').value;

        fetch('/get_mood', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                location: location,
                answers: {
                    day_rating: dayRating,
                    energy_level: energyLevel
                }
            }),
        })
        .then(response => response.json())
        .then(data => {
            moodSpan.textContent = data.mood;
            recommendationSpan.textContent = data.recommendation;
            resultDiv.classList.remove('hidden');
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});