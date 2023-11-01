import streamlit as st
import pickle
import difflib
import pandas as pd
import numpy as np

st.title("Movie Recommendatation system")
#movie_df=pd.read_csv('D:\movies.csv')
movie_df=pickle.load(open("D:\movie_recm_1.pkl","rb"))
similarity=pickle.load(open("D:\similarity_1.pkl","rb"))
list_movie=np.array(movie_df["title"])
#option = st.selectbox("Select Movie ",(list_movie))
option = st.text_input("Enter Movie Title")
def show_url(movie):
     x=[]
     index = movie_df[movie_df['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     for i in distances[1:11]:

       #   x.append(movie_df.iloc[i[0]].homepage)
        homepage = movie_df.iloc[i[0]].homepage
        if not pd.isna(homepage):
            x.append(homepage)
        else:
            x.append("Not found")
     return(x)
def movie_recommend(movie):
     index = movie_df[movie_df['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     l=[]
     for i in distances[1:11]:
          l.append("{}".format(movie_df.iloc[i[0]].title))
          # return("{} {}".format(movie_df.iloc[i[0]].title, movie_df.iloc[i[0]].urls))
     return(l)
if st.button('Recommend Me'):
     find_close_match = difflib.get_close_matches(option,list_movie)
     option = find_close_match[0]
     st.write('Movies Recomended for you are:')
     recommended_movies = movie_recommend(option)
     movie_urls = show_url(option)
    # st.write(movie_recommend(option),'Movie Url:',show_url(option))
     df = pd.DataFrame({   'Movie Recommended': recommended_movies,     'Movie Url':movie_urls  })

     st.table(df)