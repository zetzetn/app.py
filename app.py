# app.py 起点となるファイル

from flask import Flask
 
#  flaskインスタンスを作成
# 　
app = Flask(__name__)

# アプリケーションのルート
@app.route('/')

# 返すレスポンスを設定
def index():
    return "<h1>hello world</h1>"

# アプリケーションのルート
@app.route('/hello')
@app.route('/something')

# 返すレスポンスを設定
def hello():
    return "<h2>hello world</h2>"

# アプリケーションのルート
@app.route('/post/<int:post_id>/<post_name>')

# 返すレスポンスを設定
def show_post(post_id,post_name):
    # print(type(post_id))
    return '{}: {}' .format(post_name,post_id)

if __name__ == '__main__':
    app.run() 