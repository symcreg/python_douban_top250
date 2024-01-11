import crawl


def save_movies_to_csv(movies):
    print("saving movies to csv...")
    import csv
    with open("movies.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "score", "people_num", "quote", "description", "url", "pic"])
        for movie in movies:
            writer.writerow([movie.title, movie.score, movie.people_num, movie.quote, movie.description, movie.url, movie.pic])


def read_movies_from_csv():
    print("reading movies from csv...")
    import csv
    movies = []
    with open("movies.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "title":
                continue
            movie = crawl.MovieItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            movies.append(movie)
    return movies


def movie_saved():
    import os
    return os.path.exists("movies.csv")
