import requests
import random

API_KEY="86eaa4531888785f2538a3b6e2bb7cb5"
GENRE_URL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US"
MOVIE_URL = "https://api.themoviedb.org/3/discover/movie"



def get_genres():
    response = requests.get(GENRE_URL)
    if response.status_code == 200:
        data = response.json()
        return {genre["name"].lower(): genre["id"] for genre in data["genres"]}
    else:
        print("Error fetching genres:", response.status_code)
        return {}

def get_movies_by_genre(genre_id):
    params = {
        "api_key": API_KEY,
        "with_genres": genre_id,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "page": 1
    }
    response = requests.get(MOVIE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return [movie["title"] for movie in data["results"]]
    else:
        print("Error fetching movies:", response.status_code)
        return []
# Main function to recommend a movie
def recommend_movie():
    genres = get_genres()
    if not genres:
        print("Could not fetch genres. Exiting.")
        return

    print("\nAvailable genres:", ", ".join(genres.keys()))
    user_genre = input("\nEnter a movie genre: ").strip().lower()

    if user_genre not in genres:
        print("Genre not found. Please try again.")
        return

    movies = get_movies_by_genre(genres[user_genre])
    if movies:
        print("\n Recommended Movie:", random.choice(movies))
    else:
        print("No movies found for this genre.")

# Run the program
if __name__ == "__main__":
    recommend_movie()