import streamlit as st
import pickle
import requests
import omdb

# Title of the Streamlit app
st.title('MOVIEFLIX - MOVIE INFORMATION AND RECOMMENDATION SITE')

# Load movies data and similarity matrix
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown for selecting a movie
selected_movie_name = st.selectbox(
    'Please select a movie from the dropdown',
    movies_list['title'].values
)

# Function to fetch movie details from TMDB API
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return movie details in JSON format
    else:
        st.error("Error fetching movie details")  # Display error message

# Function to fetch ratings from OMDb API
def fetch_omdb_ratings(imdb_id):
    omdb_url = f"http://www.omdbapi.com/?i={imdb_id}&apikey=YOUR_OMDB_API_KEY"
    response = requests.get(omdb_url)
    if response.status_code == 200:
        omdb_data = response.json()
        if omdb_data["Response"] == "True":
            return omdb_data["imdbRating"], omdb_data["imdbVotes"]
        else:
            st.error("Failed to fetch ratings from OMDB API")
            return None, None
    else:
        st.error("Error fetching data from OMDB API")
        return None, None

# Fetch movie details when a movie is selected
if selected_movie_name:
    movie_id = movies_list[movies_list['title'] == selected_movie_name]['movie_id'].iloc[0]
    movie_details = fetch_movie_details(movie_id)

    if movie_details:
        # Display movie title and poster
        st.header(movie_details['title'])
        st.image(f"https://image.tmdb.org/t/p/w500/{movie_details['poster_path']}", use_column_width=True)

        # Display overview and release year
        st.subheader('Overview')
        st.write(movie_details['overview'])
        st.subheader('Release Year')
        st.write(movie_details['release_date'][:4])

        # Display genres and runtime
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Genres')
            genres = ', '.join([genre['name'] for genre in movie_details['genres']])
            st.write(genres)
        with col2:
            st.subheader('Runtime')
            st.write(f"{movie_details['runtime']} minutes")

        # Display tagline and budget
        col3, col4 = st.columns(2)
        with col3:
            st.subheader('Tagline')
            st.write(movie_details['tagline'] if movie_details['tagline'] else 'N/A')
        with col4:
            st.subheader('Budget')
            st.write(f"${movie_details['budget']:,}" if movie_details['budget'] else 'N/A')

        # Display revenue and production companies
        col5, col6 = st.columns(2)
        with col5:
            st.subheader('Revenue')
            st.write(f"${movie_details['revenue']:,}" if movie_details['revenue'] else 'N/A')
        with col6:
            st.subheader('Production Companies')
            production_companies = ', '.join([company['name'] for company in movie_details['production_companies']])
            st.write(production_companies if production_companies else 'N/A')

        # Display cast information
        if 'credits' in movie_details:
            st.subheader('Cast')
            cast_names = [cast['name'] for cast in movie_details['credits']['cast'][:10]]
            st.write(', '.join(cast_names) if cast_names else 'N/A')

    else:
        st.error("Failed to fetch movie details")

# Function to fetch poster image for a movie
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    return f"https://image.tmdb.org/t/p/w500/{poster_path}"

# Function to recommend movies based on cosine similarity
def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[index]
    movies_found = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_found:
        movie_id = movies_list.iloc[i[0]]['movie_id']
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies, recommended_movies_posters

# Button to trigger movie recommendations
st.header('CLICK ON THE RECOMMEND BUTTON TO GET RECOMMENDATIONS RELATED TO THIS MOVIE')
if st.button('Recommend'):
    Recommendation, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(Recommendation[0])
        st.image(posters[0])
    with col2:
        st.text(Recommendation[1])
        st.image(posters[1])
    with col3:
        st.text(Recommendation[2])
        st.image(posters[2])
    with col4:
        st.text(Recommendation[3])
        st.image(posters[3])
    with col5:
        st.text(Recommendation[4])
        st.image(posters[4])


