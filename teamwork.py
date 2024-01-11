import crawl
import csv_operate
import output
import gui
if __name__ == "__main__":

    # movies = get_top250_movies()
    if not csv_operate.movie_saved():
        movies = crawl.get_top250_movies_with_thread()
        csv_operate.save_movies_to_csv(movies)
    else:
        movies = csv_operate.read_movies_from_csv()

    output.render()
    output.pie(movies)
    output.histogram(movies)
    crawl.get_top_20_img(movies, "img/")
    gui.show_top_movies(movies)
    # for movie in movies:
    #     output.print_movie(movie)
