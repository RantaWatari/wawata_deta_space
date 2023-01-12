from flask import g,current_app,jsonify
import datetime
from deta import Deta

def get_db():
    db = Deta(project_key="c0h15t2h_R5jA9bTpwsmwSTnZoXgA1p9uHrSFGAEV")
    db = db.Base(name="flask_file")
    return db

def show_db():
    db = get_db()
    fetch_data = db.fetch()
    for i in fetch_data:
        datas = i
    posts = []
    for j in datas:
        posts.append(j)

    return posts

def insert_db(insert_text):
    key = str(len(show_db()))
    # (1/11)
    # Detaの.put()はdict,list,str,int,float,bool以外は引数として入れることが出来ない。
    # TypeError: Object of type datetime is not JSON serializable
    #

    # (1/11)
    # urllib.error.HTTPError: HTTP Error 400: Bad Request
    # requestのpayloadがおかしい？パラメータがおかしい？文字化け？
    # 原因：keyはstrかNoneのみ有効。gitのhttps://github.com/orgs/deta/discussions?discussions_q=urllib.error.HTTPError%3A+HTTP+Error+400%3A+Bad+Request+で調べたら答えが見つかった。
    # docsにも書いてあった。

    get_db().put({ 
        "key": key,
        "text": insert_text,
    })
    
def delete_db(delete_id):
    get_db().delete(delete_id)
    
def update_db(update_id,update_text):
    get_db().update({
        "text": update_text
    },update_id)
    
