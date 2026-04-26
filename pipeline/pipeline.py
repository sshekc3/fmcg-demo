from news_client import fetch_article, get_newapi_client
import pandas as pd
import streamlit as st
from pipeline.remove_similar_article import remove_similar_article
from pipeline.anaylise_article import score_article
from pipeline.computer_total_score import compute_total_score

@st.cache_data(ttl=86400)
def pipeline():
    news_client =  get_newapi_client()
    response =news_client.get_everything(
    q='(FMCG OR "consumer goods") AND (acquisition OR merger OR deal OR partnership OR investment)',
    page_size=10
) 
    df = pd.DataFrame(response['articles'])
    df = remove_similar_article(df)
    df['full_text'] = df['url'].apply(fetch_article)
    df['full_text'] = df['full_text'].fillna('')
    df['parsed'] = df['full_text'].apply(score_article)
    parsed_df = pd.json_normalize(df['parsed'])
    df = pd.concat([df, parsed_df], axis=1)
    df['total_score'] = df.apply(compute_total_score, axis=1)
    df = df[df['total_score'] != 0]
    df_sorted = df.sort_values(by='total_score', ascending=False)
    
    return df_sorted


    
