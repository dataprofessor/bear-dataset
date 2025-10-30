import streamlit as st
import pandas as pd

# Load data from provided URL
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/bear-dataset/refs/heads/master/bear_data.csv")
    IMAGE_BASE_URL = "https://raw.githubusercontent.com/dataprofessor/bear-dataset/refs/heads/master/images/"
    df['images'] = IMAGE_BASE_URL + df['id'] + '.png'

    # Re-order columns to move 'images' to the front
    cols = df.columns.tolist()
    cols.insert(0, cols.pop(cols.index('images')))
    df = df[cols]
    
    return df

# Display the URL as an image
column_config = {
    "images": st.column_config.ImageColumn("Image", width="small"),
    "Image": None
}

# Display the dataframe
st.title("🐻 Bear Data Set")
st.warning("A classification data set comprising of 200 bears belonging to 4 species.")

data = load_data()
st.dataframe(
        data,
        column_config=column_config,
        width="content",
        hide_index=True,
    )
