# Movie Recommender System
Welcome to the Movie Recommender System! This project is a simple web application built using Streamlit that recommends movies similar to the one selected by the user. It utilizes cosine similarity to suggest movies based on their descriptions and genres.

# Demo
![Demo Prediction](https://github.com/jeel-coder/MovieRecommender/blob/master/demo.png)


# Features
Movie Selection: Users can select a movie from a dropdown menu containing a list of available movies.
Recommendation: Upon selecting a movie and clicking the "Recommend" button, the system displays five recommended movies along with their posters.
Poster Display: Alongside movie titles, the system displays movie posters fetched from the TMDB API.
# Installation
To run this application locally, follow these steps:

Clone this repository.
Install the required dependencies using pip install -r requirements.txt.
Run the Streamlit application with streamlit run app.py.
Dataset
The dataset used for this project consists of movie information including title, overview, genre, and ID. This dataset was preprocessed to extract relevant features for recommendation.

# Model
The recommendation model utilizes cosine similarity to find similar movies based on their descriptions and genres. The model was trained on the processed dataset to provide accurate recommendations.
