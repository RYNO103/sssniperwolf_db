import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="SSSniperWolf-DB"
)

st.write("Search SSSniperWolf quote:")

search = st.text_input("")

con = sqlite3.connect("wolf.db")
cur = con.cursor()

if search:
    # remove special characters from string. must follow these rules:
    # Non-ASCII range characters (i.e. unicode codepoints greater than 127), or
    # One of the 52 upper and lower case ASCII characters, or
    # One of the 10 decimal digit ASCII characters, or
    # The underscore character (unicode codepoint 96).
    # The substitute character (unicode codepoint 26).
    filtered_search = ''.join(letter for letter in search if letter.isalnum() or
                      letter == 96 or letter == 26)

    search_data = (filtered_search,)
    rows = cur.execute("SELECT id, title, upload_date, timestamp, transcript "
                       "FROM (SELECT * FROM transcripts WHERE transcript "
                       "MATCH ?) INNER JOIN videos ON "
                       "video_id = videos.id",
                       search_data).fetchall()

    df = pd.DataFrame(rows, columns=["Video ID", "Video Title", "Upload Date",
                                     "Timestamp (Minutes)", "Transcript"])
    df = df.sort_values(["Upload Date", "Timestamp (Minutes)"],
                        ascending=[False, True]).reset_index()

    st.write('Found ' + str(len(df)) + ' occurrences.')

    st.dataframe(df)

cur.close()
con.close()
