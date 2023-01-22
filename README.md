https://wawata.deta.dev/
https://github.com/RantaWatari/wawata.deta.dev.git

※注意：本番環境ではDetaのProjectkeyは機密にすること。理由はProjectkeyを使ってデータベースに直接アクセス出来るため。
※注意：（自分用）Flask runが正常に動かない場合はwindows環境変数のpythonバージョンを確認すること。

Memo

(1)
    # (1/11)
    # Detaの.put()はdict,list,str,int,float,bool以外は引数として入れることが出来ない。
    # TypeError: Object of type datetime is not JSON serializable
    # datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))) 

(2)
    # (1/11)
    # urllib.error.HTTPError: HTTP Error 400: Bad Request
    # requestのpayloadがおかしい？パラメータがおかしい？文字化け？
    # 原因：keyはstrかNoneのみ有効。gitのhttps://github.com/orgs/deta/discussions?discussions_q=urllib.error.HTTPError%3A+HTTP+Error+400%3A+Bad+Request+で調べたら答えが見つかった。
    # docsにも書いてあった。

(3)    
    # (2023/1/12)
    # Detaにデプロイしたコードはこのままでも正しく動くけど、ローカル環境では20行目でエラーが出る。
    # ローカル環境ではFetchResponseの.count,.itemsは動くが、
    # デプロイした環境ではAttributeErrorを出す。
    # db.fetchはローカル環境でFetchResponseオブジェクト、デプロイ環境ではgeneratorオブジェクトとして扱われる。
    
 