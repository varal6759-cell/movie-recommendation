import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import webbrowser

# Sample Telugu movies data
movies = [
    {'movieId':101, 'title':'Mayabazar', 'url':'https://www.imdb.com/title/tt0050783/'},
    {'movieId':102, 'title':'Jersey', 'url':'https://www.imdb.com/title/tt8948790/'},
    {'movieId':103, 'title':'Sita Ramam', 'url':'https://www.imdb.com/title/tt20850406/'},
    {'movieId':104, 'title':'Baahubali 2: The Conclusion', 'url':'https://www.imdb.com/title/tt4849438/'},
    {'movieId':105, 'title':'Rangasthalam', 'url':'https://www.imdb.com/title/tt7398180/'},
    {'movieId':106, 'title':'Bommarillu', 'url':'https://www.imdb.com/title/tt0843326/'},
    {'movieId':107, 'title':'Sankarabharanam', 'url':'https://www.imdb.com/title/tt0081554/'},
]

movie_info = {m['movieId']: m for m in movies}

# Sample user ratings (userId, movieId, rating)
data = [
    (1, 101, 5), (1, 102, 4), (1, 103, 5),
    (2, 101, 3), (2, 104, 5), (2, 105, 4),
    (3, 106, 4), (3, 103, 5), (3, 107, 5),
]
df = pd.DataFrame(data, columns=['userId', 'movieId', 'rating'])

# 1. Build user-item matrix
user_item_matrix = df.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

# 2. Compute cosine similarity
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# 3. Recommend movies interactively

def print_recommendations(recommendations):
    print("\n🌟 Highly Recommended Telugu Movies For You! 🌟")
    for idx, movie_id in enumerate(recommendations.index, 1):
        title = movie_info[movie_id]['title']
        url = movie_info[movie_id]['url']
        stars = '⭐' * int(round(recommendations[movie_id]))
        print(f"{idx}. {title} [{stars}] - More info: {url}")
    print()

def recommend_movies(user_id, user_item_matrix, user_similarity_df, movie_info, top_n=3):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:3]
    similar_users_ratings = user_item_matrix.loc[similar_users]
    mean_ratings = similar_users_ratings.mean().sort_values(ascending=False)
    user_movies = user_item_matrix.loc[user_id]
    recommendations = mean_ratings[user_movies == 0].head(top_n)
    print_recommendations(recommendations)
    return recommendations

def interactive_session():
    print("🎬 Welcome to CineMatch Telugu Buddy! 🎬")
    print("\nAvailable user IDs:", list(user_item_matrix.index))
    user_id = int(input("Enter your user ID (from above): "))
    recommendations = recommend_movies(user_id, user_item_matrix, user_similarity_df, movie_info, top_n=3)
    if not recommendations.empty:
        print("Enter the number of the movie to open its IMDb page, or 0 to skip:")
        choice = int(input("Your choice: "))
        if 1 <= choice <= len(recommendations):
            movie_id = recommendations.index[choice - 1]
            url = movie_info[movie_id]['url']
            print(f"Opening {movie_info[movie_id]['title']} 🍿 ...")
            webbrowser.open(url)
        else:
            print("No movie selected. Have a great day!")
    else:
        print("No new recommendations found!")

if __name__ == "__main__":
    interactive_session()