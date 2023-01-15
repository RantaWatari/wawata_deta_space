from flask import g,current_app,jsonify
import datetime
from deta import Deta
import os

def get_db():
    db = Deta(project_key="c0h15t2h_R5jA9bTpwsmwSTnZoXgA1p9uHrSFGAEV")
    db = db.Base(name="flask_file")
    return db

def show_db():
    db = get_db()
    fetch_data = db.fetch()
    
    #(3)
    try:  
        ## Usefull only deploy enviroment
        for i in fetch_data:
            datas = i
        posts = []
        for j in datas:
            posts.append(j)
    except TypeError:
        ## Usefull Only local enviroment
        posts = fetch_data.items

    posts = posts.copy()

    # データ確認用
    #[print(i) for i in posts]
    
    return posts

def now_time():
    now_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))) 
    now_time_tuple = now_time.timetuple()
    now = []
    for i in now_time_tuple[:6]:
        now.append(i)
    # year~microsecond
    now.append(now_time.microsecond)
    return now



def insert_db(insert_text):
    post = show_db()
    p = [int(post[i]["key"]) for i in range(len(post))]
    post_max = max(p)
    key = str(post_max+1)

    time = now_time()

    # (1),(2)
    get_db().put({ 
       "key": key,
       "time": time,
       "text": insert_text,
    })
    
def delete_db(delete_id):
    get_db().delete(delete_id)
    
def update_db(update_id,update_text):

    # 今のままだと全ての時間が更新されてしまう。
    # 元のデータと更新後のデータを比較して、テキストが異なるものだけテキストと時間を更新するアルゴリズムを考えていたが、全数探索だから計算時間が掛かる。
    # もっと良い方法はないだろうか？
    # 方法１：全数探索、方法２：一度に更新出来るデータを一個だけにする。、方法３：
    time = now_time()
    get_db().update({
        "time": time,
        "text": update_text
    },update_id)
    #print(update_id)
