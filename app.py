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

col1, col2 = st.columns([2, 1])
with col1:
    selected_category = st.selectbox("Choose a music category:", categories)
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    use_text_input = st.checkbox("Or type your own")

# Text input for custom genre search
if use_text_input:
    user_genre = st.text_input("Enter a genre or mood:", placeholder="e.g., chill, rock, latin")

# Recommend button
if st.button("Get Recommendation", type="primary"):
    with st.spinner("Finding the perfect song..."):
        try:
            query = None

            # Check if user typed a custom genre
            if use_text_input and user_genre:
                # Search for matching cluster labels
                cluster_songs = clustered_df[
                    clustered_df['cluster_label'].str.lower().str.contains(user_genre.lower())
                ]
                if len(cluster_songs) > 0:
                    song = cluster_songs.sample(1).iloc[0]
                    query = f"{song['track_name']} {song['artists']}"
                    st.info(f"🎶 Matched **{song['cluster_label']}**: **{song['track_name']}** by {song['artists']}")
                else:
                    st.warning(f"No category matched '{user_genre}'. Try: chill, rock, latin, pop, country, holiday...")
            elif selected_category == "Trending (Billboard Hot 100)":
                song = billboard_df.sample(1).iloc[0]
                query = f"{song['song_title']} {song['artist']}"
                st.info(f"🔥 Trending: **{song['song_title']}** by {song['artist']}")
            else:
                cluster_songs = clustered_df[clustered_df['cluster_label'] == selected_category]
                song = cluster_songs.sample(1).iloc[0]
                query = f"{song['track_name']} {song['artists']}"
                st.info(f"🎶 From **{selected_category}**: **{song['track_name']}** by {song['artists']}")

            # Search Spotify (only if we have a query)
            if query:
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
