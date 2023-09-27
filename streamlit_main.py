import sqlite3
import pandas as pd
import streamlit as st

con = sqlite3.connect("wolf.db")
cur = con.cursor()

st.write("Search for SSSniperWolf quote:")

search = st.text_input("")

if search:
    rows = cur.execute("SELECT id, title, upload_date, timestamp, transcript "
                       "FROM (SELECT * FROM vtranscripts WHERE transcript "
                       "MATCH ?) INNER JOIN videos ON "
                       "video_id = videos.id",
                       [search]).fetchall()

    df = pd.DataFrame(rows, columns=["Video ID", "Video Title", "Upload Date",
                                     "Timestamp (Minutes)", "Transcript"])

    st.write('Found ' + str(len(df)) + ' occurrences.')

    st.dataframe(df)

cur.close()
con.close()
