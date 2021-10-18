import streamlit as st
import pickle
import pandas as pd
import requests
movies_list = pickle.load(open('C:\\Users\Dell\Downloads\website\Movie recommend\con_mov\movie_list_dic.pkl','rb'))
movies=pd.DataFrame(movies_list)

similarity= pickle.load(open('C:\\Users\Dell\Downloads\website\Movie recommend\con_mov\similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=507aa853ae902f61c5ac921503091e63&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path ##tmdb complete path
    return full_path



##convert dataframe to dictionary
def recommend(movie):
    m_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[m_index])),reverse=True,key = lambda x: x[1])
    
    recommended_movies=[]
    recommended_movies_posters=[]

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters


st.title('Movie Recommender System')
option =st.selectbox(
'Enter the name of your FAVOURITE movie to find similar movies!!!!',
        (movies['title'].values)
)
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(option)
    col1 ,col2, col3 ,col4, col5  = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
   

    
   