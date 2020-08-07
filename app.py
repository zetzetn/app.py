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

# 返すレスポンスを設定
def hello():
    return "<h2>hello world</h2>"

# アプリケーションのルート
@app.route('/post/<post_name>')

# 返すレスポンスを設定
def show_post(post_name):
    print(type(post_name))
    return 'Post {}' .format(post_name)

if __name__ == '__main__':
    app.run() 