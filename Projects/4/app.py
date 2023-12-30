from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Assume you have a DataFrame 'df' with movie titles and genres
df = pd.DataFrame({
    'title': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'genres': ['Action,Adventure,Sci-Fi', 'Comedy,Romance', 'Comedy,Drama', 'Drama,Mystery,Sci-Fi', 'Action,Adventure,Sci-Fi']
})

count = CountVectorizer()
count_matrix = count.fit_transform(df['genres'])

cosine_sim = cosine_similarity(count_matrix, count_matrix)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()  # Get JSON data from the request
    movie = data['title']  # Get the movie title from the JSON data
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    idx = indices[movie]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    recommended_movies = df['title'].iloc[movie_indices].tolist()
    return jsonify(recommended_movies)  # Return the recommended movies as JSON

if __name__ == "__main__":
    app.run(debug=True)
