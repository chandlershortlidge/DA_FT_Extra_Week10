import streamlit as st
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Page config
st.set_page_config(
    page_title="Music Recommender",
    page_icon="🎵",
    layout="centered"
)

# Load data
@st.cache_data
def load_data():
    clustered_df = pd.read_csv('data/clustered_songs.csv')
    billboard_df = pd.read_csv('data/billboard_hot100.csv')
    return clustered_df, billboard_df

clustered_df, billboard_df = load_data()

# Initialize Spotify client
@st.cache_resource
def get_spotify_client():
    return spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=st.secrets["spotify"]["client_id"],
            client_secret=st.secrets["spotify"]["client_secret"]
        )
    )

sp = get_spotify_client()

# App UI
st.title("🎵 Music Recommender")
st.markdown("Discover new music based on genre clusters or trending songs!")

# Category selection
categories = ["Trending (Billboard Hot 100)"] + sorted(clustered_df['cluster_label'].unique().tolist())
selected_category = st.selectbox("Choose a music category:", categories)

# Recommend button
if st.button("Get Recommendation", type="primary"):
    with st.spinner("Finding the perfect song..."):
        try:
            if selected_category == "Trending (Billboard Hot 100)":
                song = billboard_df.sample(1).iloc[0]
                query = f"{song['song_title']} {song['artist']}"
                st.info(f"🔥 Trending: **{song['song_title']}** by {song['artist']}")
            else:
                cluster_songs = clustered_df[clustered_df['cluster_label'] == selected_category]
                song = cluster_songs.sample(1).iloc[0]
                query = f"{song['track_name']} {song['artists']}"
                st.info(f"🎶 From **{selected_category}**: **{song['track_name']}** by {song['artists']}")

            # Search Spotify
            result = sp.search(q=query, limit=1, market="GB")

            if result["tracks"]["items"]:
                track_id = result["tracks"]["items"][0]["id"]

                # Embed Spotify player
                st.components.v1.iframe(
                    src=f"https://open.spotify.com/embed/track/{track_id}",
                    width=400,
                    height=160
                )
            else:
                st.warning("Could not find this song on Spotify.")

        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit & Spotify API*")
