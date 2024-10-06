# Movie Recommendation System

This project is a content-based movie recommendation system built with machine learning and deployed via Streamlit. It uses metadata (genres, keywords, cast, crew, and plot overview) from TMDB to recommend movies based on similarity to a selected movie.

Key Features:
- Content-Based Filtering: Movies are represented as vectors using their metadata. A cosine similarity matrix is computed to recommend movies with 
  similar features.
- NLP Processing: Text data is processed using NLTK for tokenization and stemming, enabling effective feature extraction for similarity calculations.
- API Integration: Fetches additional movie details (ratings, release date, posters) using an external movie database API.
- Interactive Web App: The system is deployed on Streamlit, allowing users to input a movie title and receive recommendations with rich details.


## Table of Contents

- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Features](#features)
- [How to Run the Project](#how-to-run-the-project)
- [Acknowledgments](#acknowledgments)
  

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- NLTK
- Ast
- Pickle

## Dataset

The project uses the following datasets:

1. **Movies Dataset**: `tmdb_5000_movies.csv`
   - Contains movie information such as titles, genres, keywords, and overviews.
   
2. **Credits Dataset**: `tmdb_5000_credits.csv`
   - Contains information about the cast and crew for each movie.

The datasets can be found on [Kaggle: The Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

## Features

- **Data Preprocessing**: Merges movie and credits datasets, removes duplicates and missing values, and extracts relevant information.
- **Natural Language Processing**: Converts textual data into a format suitable for machine learning. This includes tokenization, stemming, and vectorization.
- **Cosine Similarity**: Calculates similarity scores between movies based on their features.
- **Movie Recommendations**: Provides top movie recommendations based on user input using a content-based filtering approach.
-  Fetches additional movie information by hitting an external API to display relevant details/posters about a movie.

## How to Run the Project

1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   cd movie-recommendation-system
   
2. Download the datasets from Kaggle and place them in the project directory.

3. Install the required packages:
   ```bash
   pip install -r requirements.txt 

4. Run the main Python script:

   ```bash
   streamlit run app.py
   ```

5. Open your web browser and go to http://localhost:8501 to access the application.


## Acknowledgments
The datasets used in this project are from The Movie Database (TMDB).
Special thanks to the developers of Streamlit and other libraries used in this project.
