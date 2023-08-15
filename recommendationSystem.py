import pandas as pd
from surprise import SVD
from surprise import Dataset
from surprise import Reader

# Load data into a Pandas dataframe
df = pd.read_csv('ratings.csv')

# Define the reader for the Surprise library
reader = Reader(rating_scale=(1, 5))

# Load data into the Surprise dataset format
data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)

# Define the algorithm for collaborative filtering
algo = SVD()

# Train the model on the data
trainset = data.build_full_trainset()
algo.fit(trainset)

# Generate recommendations for a user
user_id = 1
items_to_recommend = []
for item_id in range(1, 100):
    if not df[(df['user_id'] == user_id) & (df['item_id'] == item_id)].empty:
        continue
    predicted_rating = algo.predict(user_id, item_id).est
    if predicted_rating >= 4.0:
        items_to_recommend.append((item_id, predicted_rating))

# Sort the recommendations by predicted rating
items_to_recommend.sort(key=lambda x: x[1], reverse=True)

# Print the top 5 recommendations
for item in items_to_recommend[:5]:
    print("Item ID:", item[0], "Predicted Rating:", item[1])
