
import tkinter as tk


def mouse_event(cv, event):
    number = int(-event.delta / 12)
    cv.yview_scroll(number * 2, 'units')


def show_top_movies(movies):
    from PIL import Image, ImageTk
    if not movies:
        return
    root = tk.Tk()
    root.title("豆瓣Top250电影")
    root.geometry('800x500')
    frame = tk.Frame(root)
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    cv = tk.Canvas(frame, height=450, width=400, bg='white')
    cv.pack()
    cv.config(yscrollcommand=scrollbar.set)
    cv.config(scrollregion=(0, 0, 0, 500 * 20))
    scrollbar.config(command=cv.yview)
    frame.pack()
    cv.config(yscrollincrement=1)
    cv.bind("<MouseWheel>", lambda event: mouse_event(cv, event))
    # 创建一个画布来显示电影海报
    photos = []
    titles = []
    scores = []
    quotes = []
    for i in range(20):
        img = Image.open("./img/" + movies[i].title + ".jpg")
        photo = ImageTk.PhotoImage(img)
        photos.append(photo)
        titles.append(movies[i].title)
        scores.append(movies[i].score)
        quotes.append(movies[i].quote)
    text_y = 0
    quote_y = 0
    img_y = 0
    bg_list = ['#eea2a4', '#5c2223', '#f07c82', '#ed5a65', '#f0a1a8', '#7a7374', '#e77c8e', '#73575c', '#2b73af', '#bacf65']
    for i in range(20):
        cv.create_rectangle(0, img_y, 400, img_y + photos[i].height() + 50, fill=bg_list[i % 10])
        cv.create_image(0, img_y, anchor='nw', image=photos[i])
        text_y = photos[i].height() + img_y + 10
        quote_y = text_y + 20
        img_y += photos[i].height() + 70
        cv.create_text(0, text_y, anchor='nw', text=f"{titles[i]} - 评分：{scores[i]}")
        cv.create_text(0, quote_y, anchor='nw', text=f"{quotes[i]}")
        cv.create_line(0, quote_y + 20, 400, quote_y + 20, fill='black')
        # cv.create_image(20, 50 + i * 20, image=movies.iloc[i]['pic'])

    button = tk.Button(root, text="关闭", command=root.destroy)
    button.pack()

    root.mainloop()


