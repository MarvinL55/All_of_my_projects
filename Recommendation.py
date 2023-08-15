import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Load rating data
ratings = pd.read_csv("C:\\Users\\marvi\\Downloads\\ml-latest-small\\ml-latest-small\\ratings.csv")

# Load movies data
movies = pd.read_csv("C:\\Users\\marvi\\Downloads\\ml-latest-small\\ml-latest-small\\movies.csv")

# Merge rating and movies data
data = pd.merge(ratings, movies, on='movieId')

# Convert rating to sparse matrix
ratings_matrix = data.pivot_table(index='userId', columns='title', values='rating')
ratings_matrix = ratings_matrix.fillna(0)
matrix = csr_matrix(ratings_matrix.values)

# Compute pairwise cosine similarities between movies
similarities = cosine_similarity(matrix)
similarities_df = pd.DataFrame(similarities, index=ratings_matrix.index, columns=ratings_matrix.index)

# Function to get movie recommendations for a user
def get_recommendations(user_id, num_recommendations):
    # Get movies the user has rated
    user_ratings = ratings_matrix.loc[user_id].values.reshape(1, -1)
    # Compute similarity between user's rating and all movies
    similarities = cosine_similarity(user_ratings, ratings_matrix)
    similarities_df = pd.DataFrame(similarities.reshape(-1), index=ratings_matrix.index, columns=['similarity'])
    # Get top similar user
    similar_user = similarities_df.sort_values(by='similarity', ascending=False)[1:num_recommendations+1]
    # Get movies rated highly by similar users
    recommendations = pd.DataFrame(columns=['title', 'score'])
    for user in similar_user.index:
        rated_movies = ratings_matrix.loc[user].where(ratings_matrix.loc[user] > 0).dropna()
        for movie in rated_movies.index:
            if movie not in ratings_matrix.loc[user_id]:
                score = rated_movies[movie] * similar_user.loc[user, 'similarity']
                recommendations = recommendations.append({'title': movie, 'score': score}, ignore_index=True)
    return recommendations.index.tolist()

user_id = 1
num_recommendations = 5
recommendations = get_recommendations(user_id, num_recommendations)
print('Recommendation movies for user {}'.format(user_id))
for movie in recommendations:
    print(movie)
