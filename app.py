import pickle
import streamlit as st 
import requests 

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=97d0da879098b9b52206f2294762507b&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster
    
    

st.header('AI Based Movies Recommender System')
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

movies_list = movies['title'].values
selected_movie = st.selectbox(
    'Select or type a movie name  to get recommendation',
    movies_list 
)



if st.button('Show Recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(f"<div class='fade-in-out'>{recommended_movies_name[0]}</div>", unsafe_allow_html=True)
        st.image(recommended_movies_poster[0], width=100)

    with col2:
        st.markdown(f"<div class='fade-in-out'>{recommended_movies_name[1]}</div>", unsafe_allow_html=True)
        st.image(recommended_movies_poster[1], width=100)

    with col3:
        st.markdown(f"<div class='fade-in-out'>{recommended_movies_name[2]}</div>", unsafe_allow_html=True)
        st.image(recommended_movies_poster[2], width=100)

    with col4:
        st.markdown(f"<div class='fade-in-out'>{recommended_movies_name[3]}</div>", unsafe_allow_html=True)
        st.image(recommended_movies_poster[3], width=100)

    with col5:
        st.markdown(f"<div class='fade-in-out'>{recommended_movies_name[4]}</div>", unsafe_allow_html=True)
        st.image(recommended_movies_poster[4], width=100)
