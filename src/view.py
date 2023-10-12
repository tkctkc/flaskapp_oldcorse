#coding: utf-8

from flask import Flask,render_template

#appという名前でFlaskオブジェクトをインスタンス化
app = Flask(__name__)

#---view側の設定---
#ルートディレクトリにアクセスした場合の挙動
@app.route("/")
def index():
    #return "hello world"
    return render_template("index.html")

#エントリーポイントの設定
if __name__ == "__main__":
    app.run()

