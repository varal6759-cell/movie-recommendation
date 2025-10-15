# movie-recommendation
What i built ?
CineMatch Telugu Buddy is an interactive movie recommendation system tailored for Telugu movie enthusiasts. It suggests highly-rated Telugu movies based on user rating behavior similarity, helping users discover new films they are likely to enjoy. The tool includes clickable IMDb links to learn more about recommended movies.

Why i built it ?
Finding good Telugu movies can sometimes be overwhelming due to the sheer number of options available. This project helps users by leveraging collaborative filtering to recommend movies based on preferences of similar users, making movie discovery easier, personalized, and more enjoyable.

How i built it ?
Data Collection: Built a small sample dataset of Telugu movies with IMDb URLs and simulated user ratings.

User-Item Matrix: Created a pivot table from user ratings where rows are users, columns are movies, and values are ratings.

Similarity Computation: Calculated cosine similarity between users based on their movie ratings to find users with similar tastes.

Recommendation Logic: For a given user, identified top similar users and recommended movies highly rated by them but not yet watched by the user.

Interactive Interface: Implemented a simple command-line interface for users to input their user ID, display recommendations with star ratings, and optionally open the corresponding IMDb pages in the browser using Python’s webbrowser module.

Libraries Used: Pandas for data handling, scikit-learn for cosine similarity, webbrowser for URL launching.

This system demonstrates a basic collaborative filtering recommender focusing on Telugu movies, providing a foundation that could be extended to larger datasets, other languages, or additional features like rating prediction and personalized user profiles.
