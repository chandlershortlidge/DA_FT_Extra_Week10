# Case Study: The site for recommendations - "Gnod"

### Scenario

You have been hired as a Data Analyst for "Gnod".

"Gnod" is a site that provides recommendations for music, art, literature and products based on collaborative filtering algorithms. Their flagship product is the _music recommender_, which you can try at [www.gnoosic.com](https://www.gnoosic.com). The site asks users to input 3 bands they like, and computes similarity scores with the rest of the users. Then, they recommend to the user bands that users with similar tastes have picked.

"Gnod" is a small company, and its only revenue stream so far are Ads in the site. In the future, they would like to explore partnership options with music apps (such as _Deezer_, _Soundcloud_ or even _Apple Music_ and _Spotify_). However, for that to be possible, they need to expand and improve their recommendations.

That's precisely where you come in. They have hired you as a Data Analyst, and they expect you to bring a mix of technical expertise and business mindset to the table.

Jane, CTO of Gnod, has sent you an email assigning you with your first task.

### Task(s)

*Subject: Welcome to Gnoosic! Your First Task as a Data Analyst*

Dear Ironhack Student,

We are thrilled to welcome you as a Data Analyst for Gnoosic!

Our goal is to redefine how users discover music—not just based on their listening history but by allowing them to explore songs based on sound, mood, and energy.

To do this, we need your help in designing a new music recommendation system that gives users two powerful ways to find songs:
1. By selecting a type of music they want to listen to (e.g., Rock, High Energy, Calm).
2. By asking for a currently trending song, no matter the genre.

Your First Mission
Your job is to:

1. Scrape the Most Popular Songs Right Now
Your first task is to collect data on globally trending songs.
Look for sources like Billboard Hot 100, Spotify Viral 50, or other global music charts to compile a list of the most popular songs this week.
You may use APIs or web scraping to gather song names, artists, and any available metadata.
Why? This will allow us to recommend trending music if a user says, “I want to hear something popular right now.” These songs will act as an additional "cluster" for recommendations.

2. Explore the Dataset and Identify Song Features
You’ll be working with a dataset of songs and their audio features (such as tempo, loudness, danceability).
Your task is to analyze the data and determine how we can group songs meaningfully.

3. Cluster Songs into Groups
Using unsupervised learning, you will organize songs into 5 to 20 clusters based on their audio characteristics.
Your goal is to find natural groupings of songs that sound similar.

4. Label the Clusters
Once you’ve identified the clusters, listen to a few songs from each and come up with descriptive labels for them.
Examples: Rock, Chill Acoustic, High Energy, Dark & Moody.
These labels will help users select the type of music they want to listen to.

5. Build the First Version of the Recommender
Once the clusters are ready, we will allow users to input their preferred music type (e.g., Jazz Fusion), and your system will return a song from that category.
Additionally, if the user asks for a "currently popular song," your system will recommend one from the trending songs list that you scraped earlier.

The Bigger Picture
This is just the beginning! If we can successfully group and label songs, we could expand our system to:
- Fine-tune recommendations based on user feedback.
- Enhance search options, allowing users to discover new music by describing how they feel.
- Explore additional features, such as analyzing lyrics or integrating external music databases.

Presentation on Friday

On Friday, you’ll present your findings to me and Marek, the CEO & Founder. Be prepared to:

Show how you scraped the trending songs and what sources you used.
Explain how you decided on the number of clusters and why.
Show how you labeled the clusters.
Demonstrate the first version of the recommender in action.
This project is a personal passion of mine, and I need you to bring your best insights to make it successful. If we can get this right, we have the potential to change the way people discover music!

Welcome aboard, and good luck on your first week!

– Jane



