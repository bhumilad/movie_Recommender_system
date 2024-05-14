import pickle
import streamlit as st
import pandas as pd
import requests

def fetch_posters(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=18d7b4647a53c76504330442b04fc2d6".format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = similarity[index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]
    recommend_movies = []
    recommendation_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommendation_posters.append(fetch_posters(movie_id))
    return recommend_movies, recommendation_posters
    

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = movies_list['title'].values

st.title("MOVIE RECOMMENDER SYSTEM")

option = st.selectbox('Select your taste in movie :)', movies_list)

if st.button('Recommend'):
    movies_name, posters = recommend(option)
    # for i in movies_name:
    #     st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movies_name[0])
        st.image(posters[0])
    with col2:
        st.text(movies_name[1])
        st.image(posters[1])
    with col3:
        st.text(movies_name[2])
        st.image(posters[2])
    with col4:
        st.text(movies_name[3])
        st.image(posters[3])
    with col5:
        st.text(movies_name[4])
        st.image(posters[4])
        