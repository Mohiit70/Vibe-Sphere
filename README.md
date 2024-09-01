# VibeSphere: Your Personal Vibe Curator

VibeSphere is a web application that curates personalized media recommendations based on real-time weather data and user inputs. Utilizing Fluvio for real-time data streaming, VibeSphere delivers dynamic mood-based suggestions that resonate with your current vibe.

## Project Overview

VibeSphere offers users media recommendations such as music, books, movies, and activities by analyzing real-time weather conditions and personal inputs like mood and energy levels. This project integrates real-time data streaming, user interaction, and personalized content delivery into a cohesive, engaging experience.

## Features

- **Real-Time Weather-Based Mood Setting:** Fetches real-time weather data to set an initial mood.
- **Personalized Recommendations:** Refines mood suggestions based on user input and offers tailored media recommendations.
- **Mood Tracking and Insights:** Tracks and analyzes mood patterns over time, providing valuable insights.
- **Community Vibes:** Displays trending moods and popular recommendations within the user's area.

## Technologies Used

- **Flask:** Web framework for Python used to build the backend.
- **Fluvio:** Real-time streaming platform used for processing weather data and user inputs.
- **HTML/CSS/JavaScript:** For building the user interface.
- **OpenWeatherMap API:** For fetching real-time weather data.
- **Python-dotenv:** For managing environment variables securely.

## Installation

To run VibeSphere locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/vibesphere.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd vibesphere
    ```

3. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows, use venv\Scripts\activate
    ```

4. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up Fluvio and start the cluster:** Ensure Fluvio is installed and the cluster is running. Follow the [Fluvio documentation](https://www.fluvio.io/docs/getting-started/) for installation and setup instructions.

Now you are ready to start using VibeSphere locally! Enjoy your personalized vibe curation experience.