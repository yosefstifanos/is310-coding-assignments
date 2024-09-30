favorite_movies = [
    {
        "name": "The Matrix",
        "release_year": 1999,
        "sequels": ["The Matrix Reloaded", "The Matrix Revolutions", "The Matrix Resurrections"]
    },
    {
        "name": "Inception",
        "release_year": 2010,
    },
    {
        "name": "Interstellar",
        "release_year": 2014,
    },
    {
        "name": "Back to the Future",
        "release_year": 1985,
        "sequels": ["Back to the Future Part II", "Back to the Future Part III"]
    }
]

def check_movie_release(movie):
    if movie['release_year'] < 2000:
        print(f"{movie['name']} was released before 2000")
    else:
        print(f"{movie['name']} was released after 2000")
        return movie['name']

recent_movies = []

for movie in favorite_movies:
    result = check_movie_release(movie)
    if result is not None:
        recent_movies.append(result)

print("\nMovies released after 2000:")
print(recent_movies)

# Get user input for a new movie
print("\nEnter details for your favorite movie:")
new_movie_name = input("Movie name: ")
new_movie_year = int(input("Release year: "))

new_movie = {
    "name": new_movie_name,
    "release_year": new_movie_year
}

# Check the new movie and potentially add it to recent_movies
result = check_movie_release(new_movie)
if result is not None:
    recent_movies.append(result)

print("\nUpdated list of movies released after 2000:")
print(recent_movies)