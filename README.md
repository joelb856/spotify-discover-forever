# spotify-discover-forever

I set out to create a tool to enhance my music discovery and listening experience using my Spotify library. This is typically done by analyzing [the audio features that Spotify provides via their API](https://developer.spotify.com/documentation/web-api/reference/get-audio-features). There have been plenty of interesting attempts to develop custom song recommendation algorithms from scratch *(see [here](https://towardsdatascience.com/part-iii-building-a-song-recommendation-system-with-spotify-cf76b52705e7), [here](https://machinelearninggeek.com/spotify-song-recommender-system-in-python/), and [here](https://dev.to/kuvambhardwaj/how-i-built-a-song-recommendation-system-with-python-scikit-learn-pandas-11ok), for example)*, but I attempt to solve a more niche problem based on my own listening habits:

1. I already find plenty of new songs and artists through friends, blogs, social media, and exisitng algorithms. While this search could certainly be more efficient and it could be worth developing a reccomendation algorithm specifically tailored to my interests, I enjoy the hunt and don't necessarily view this as a problem to be solved.
2. The thing I value the most is the experience of listening through an entire album.
3. I often times save a handful of songs from an artist with the intention of "getting into them" which end up getting buried in my library.

From the above, it is clear that I need a tool to suggest albums with at least one song I have already saved.
