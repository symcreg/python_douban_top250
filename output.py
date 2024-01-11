import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar


def render():

    data = pd.read_csv('movies.csv')
    c = (
        Bar()
        .add_xaxis(data['title'].values.tolist()[:20])
        .add_yaxis("评分", data['score'].values.tolist()[:20])
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts(title='电影评价分数'),
            yaxis_opts=opts.AxisOpts(name='片名'),
            xaxis_opts=opts.AxisOpts(name='评分'),
            datazoom_opts=opts.DataZoomOpts(type_='inside'),
        )
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .render('电影评价分数.html')
    )


def histogram(movies):
    sum = [0, 0, 0, 0, 0]
    for movie in movies:
        if float(movie.score) >= 9.5:
            sum[0] += 1
        elif float(movie.score) >= 9:
            sum[1] += 1
        elif float(movie.score) >= 8.5:
            sum[2] += 1
        elif float(movie.score) >= 8:
            sum[3] += 1
        else:
            sum[4] += 1
    from pyecharts import options as opts
    from pyecharts.charts import Bar
    c = (
        Bar()
        .add_xaxis(['9.5以上', '9-9.5', '8.5-9', '8-8.5', '8以下'])
        .add_yaxis("评分", sum)
        .set_global_opts(title_opts=opts.TitleOpts(title="豆瓣电影评分分布"))
        .render("豆瓣电影评分分布histogram.html")
    )


def pie(movies):
    sum = [0, 0, 0, 0, 0]
    for movie in movies:
        if float(movie.score) >= 9.5:
            sum[0] += 1
        elif float(movie.score) >= 9:
            sum[1] += 1
        elif float(movie.score) >= 8.5:
            sum[2] += 1
        elif float(movie.score) >= 8:
            sum[3] += 1
        else:
            sum[4] += 1
    percent = [0, 0, 0, 0, 0]
    for i in range(5):
        percent[i] = sum[i] / 250
    from pyecharts import options as opts
    from pyecharts.charts import Pie
    c = (
        Pie()
        .add("", [list(z) for z in zip(['9.5以上', '9-9.5', '8.5-9', '8-8.5', '8以下'], percent)])
        .set_global_opts(title_opts=opts.TitleOpts(title="豆瓣电影评分分布"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .render("豆瓣电影评分分布pie.html")
    )


def print_movie(movie):
    print(movie.title)
    print(movie.score)
    print(movie.quote)
    print(movie.description)
    print(movie.url)
    print(movie.pic)
    print("=====================================")
