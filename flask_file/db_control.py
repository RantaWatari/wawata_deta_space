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
    return posts

def insert_db(insert_text):
    post = show_db()
    p = [int(post[i]["key"]) for i in range(len(post))]
    post_max = max(p)
    key = str(post_max+1)

    # (1),(2)
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
    
