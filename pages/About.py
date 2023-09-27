import streamlit as st

st.set_page_config(
    page_title="SSSniperWolf-DB"
)

st.title("About")

st.markdown(
    """
    Search for any word or phrase across a span of over 3,000 SSSniperWolf 
    videos.  
      
    Will return every occurrence of the word/phrase along with the video id, 
    title, and timestamp of when it occurs. Also provides a passage of text
    to show the context surrounding the word/phrase.  
      
    This project started as a way to help the community find specific videos
    that SSSniperWolf has reacted to. Just describe the video in the search bar
    and then sift through the results until you find the correct video.  
      
    P.S. In the "Transcript" column on the search results table, you can 
    double-click on a cell to expand the results to see the entire text.  
      
    P.P.S. If you click on the three dots in the upper right hand corner of the
    website, open settings, and enable wide mode, it will make things easier
    to read.  
      
    Last updated: 9/27/23
    """
)
