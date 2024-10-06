# Movie Recommendation System

This project implements a movie recommendation system using a dataset of movies and their associated metadata. The system leverages Natural Language Processing (NLP) techniques to analyze movie features such as genres, keywords, cast, crew, and overview to provide recommendations based on user input.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Features](#features)
- [How to Run the Project](#how-to-run-the-project)
- [Usage](#usage)
- [License](#license)

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

3. Run the main Python script:

```bash
streamlit run app.py
```

## Acknowledgments
The datasets used in this project are from The Movie Database (TMDB).
Special thanks to the developers of Streamlit and other libraries used in this project.
