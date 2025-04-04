import streamlit as st
import pickle
import requests
st.set_page_config(page_title="Movie Recommender System")
def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

predictor = pickle.load(open('predictor.pkl','rb'))
movies = pickle.load(open('movies.pkl','rb'))
movie_titles = movies['title'].values
st.subheader("Movie Recommender System")
st.header("Welcome to my site :)")
selected = st.selectbox("Select the movie you like",movie_titles)

def recommend(choice):
    index=movies[movies['title']==choice].index[0]
    distance = sorted(list(enumerate(predictor[index])), reverse=True, key=lambda vector:vector[1])
    recommandations = []
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommandations.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommandations,recommend_poster

if st.button("Recommend"):
    with st.spinner('Recommending...'):
        suggest,suggest_poster = recommend(selected)
        col1,col2,col3,col4,col5 = st.columns(5)
        with col1:
            st.write(suggest[0])
            st.image(suggest_poster[0])
        with col2:
            st.write(suggest[1])
            st.image(suggest_poster[1])
        with col3:
            st.write(suggest[2])
            st.image(suggest_poster[2])
        with col4:
            st.write(suggest[3])
            st.image(suggest_poster[3])
        with col5:
            st.write(suggest[4])
            st.image(suggest_poster[4])