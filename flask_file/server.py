from flask import render_template,request,Blueprint,redirect,session
from db_control import show_db,insert_db,delete_db,update_db
import os

bp =Blueprint("server",__name__)

@bp.route("/",methods=["GET","POST"])
def index():
    #print(f"##heders##\n{request.headers}")
    print(f"##referrer##:\n{request.referrer}")
    #print(f"##access_root##:\n{request.access_route}")
    # print(os.system("dir"))

    if request.referrer == None:
        session["select"] = False
        session["log"] = None


    if request.method == "GET":
        select = request.args.get("select")
        if select:
            session["select"] = True
        return render_template("index.html",select=select,log=session["log"],posts=show_db())

    # ブラウザバック後にリロードを行うと処理が出来てしまう。
    if request.method == "POST" and session["select"]: 
        sql_cmd = request.form.get("sql_cmd")

        if sql_cmd == "insert":
            insert_text = request.form.get("insert_text")
            insert_db(insert_text)
            
        elif sql_cmd == "delete":
            delete_id = request.form.getlist("delete_id")
            [delete_db(i) for i in delete_id]

        elif sql_cmd == "update":
            update_texts = request.form.getlist("update_texts")
            update_id = request.form.getlist("update_id")

            db_items = show_db().copy()
            for i in range(len(update_texts)):
                if db_items[i]["key"] == update_id[i] and db_items[i]["text"] != update_texts[i]:
                    update_db(update_id[i],update_texts[i])

        session["select"] = False
        session["log"] = "True"
        return redirect(location="/")
    else:
        session["select"] = False
        session["log"] = "Error"
        return redirect(location="/")

