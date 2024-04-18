import streamlit as st
import pickle
import requests
import requests
# from flask import Flask, render_template, request4
import omdb


st.title('MOVIEFLIX- MOVIES INFORMATION AND RECOMMENDATION SITE')

movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


selected_movie_name = st.selectbox(
    ' Please select a movie from the dropdown',
    movies_list['title'].values)
# if selected_movie_name:
#     st.write('Some information about the movie:')
#     selected_movie_tags = movies_list[movies_list['title'] == selected_movie_name]['tags'].values[0]
#     st.write(selected_movie_tags)

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=2f035bc6cbd12e40afac033493a0ab48&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        movie_details = response.json()
        return movie_details
    else:
        st.error("Error fetching movie details")


def fetch_omdb_ratings(imdb_id):
    omdb_url = f"http://www.omdbapi.com/?i={imdb_id}&apikey=93327a3a"
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
# Main UI
# selected_movie_name = st.selectbox(
#     'Please select a movie from the dropdown',
#     movies_list['title'].values)

# Fetch movie details when a movie is selected
if selected_movie_name:
    movie_id = movies_list[movies_list['title'] == selected_movie_name]['movie_id'].iloc[0]
    # api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual TMDB API key
    movie_details = fetch_movie_details(movie_id)

    if movie_details:
        # Title and poster
        st.header(movie_details['title'])
        st.image(f"https://image.tmdb.org/t/p/w500/{movie_details['poster_path']}", use_column_width=True)

        # Overview and release year
        col1, col2 = st.columns([2, 1])
        st.subheader('Overview')
        st.write(movie_details['overview'])

        st.subheader('Release Year')
        st.write(movie_details['release_date'][:4])

        # Genres and runtime
        col3, col4 = st.columns(2)
        with col3:
            st.subheader('Genres')
            genres = ', '.join([genre['name'] for genre in movie_details['genres']])
            st.write(genres)
        with col4:
            st.subheader('Runtime')
            st.write(f"{movie_details['runtime']} minutes")

        # Tagline and budget
        col5, col6 = st.columns(2)
        with col5:
            st.subheader('Tagline')
            st.write(movie_details['tagline'] if movie_details['tagline'] else 'N/A')
        with col6:
            st.subheader('Budget')
            st.write(f"${movie_details['budget']:,}" if movie_details['budget'] else 'N/A')

        # Revenue and production companies
        col7, col8 = st.columns(2)
        with col7:
            st.subheader('Revenue')
            st.write(f"${movie_details['revenue']:,}" if movie_details['revenue'] else 'N/A')
        with col8:
            st.subheader('Production Companies')
            production_companies = ', '.join([company['name'] for company in movie_details['production_companies']])
            st.write(production_companies if production_companies else 'N/A')

            # Fetch movie ratings and reviews from OMDb API



        # Cast
        if 'credits' in movie_details:
            st.subheader('Cast')
            cast_names = [cast['name'] for cast in movie_details['credits']['cast'][:10]]
            st.write(', '.join(cast_names) if cast_names else 'N/A')



    else:
        st.error("Failed to fetch movie details")

def fetch_poster(movie_id):
    # response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2f035bc6cbd12e40afac033493a0ab488&language=en-US%27'.format(movie_id))
    # data = response.json()
    # response=requests.get('https: // api.themoviedb.org / 3 / search / movie?query = {} & api_key =api_key=2f035bc6cbd12e40afac033493a0ab488&language=en-US%27'.format(movie_id))
    # data = response.json()

    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path
    # return "http://image.tmdb.org/t/p/w500/"+ data['poster_path']
def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[index]
    movies_found = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies= []
    recommended_movies_posters=[]
    for i in movies_found:
        movie_id = movies_list.iloc[i[0]]['movie_id']
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies, recommended_movies_posters


st.header('CLICK ON THE RECOMMEND BUTTON TO GET RECOMMENDATIONS RELATED TO THIS MOVIE')


if st.button('Recommend'):
    Recommendation,posters = recommend(selected_movie_name)
    col1 ,col2, col3, col4, col5= st.columns(5)
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


