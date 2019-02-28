#!/usr/bin/env python3

from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
        <p>姓名:<input name="username"></p>
        <p>密码:<input name="password"></p>
        <p><button type="submit">登录</p>
        </form>'''

@app.route("/signin",methods=["POST"])
def signin():
    # 需要从request对象读取表单内容
    if request.form['username'] == 'admin' and request.form['password']=='password':
        return '<h3>Welcome to here.</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ =='__main__':
    app.run()