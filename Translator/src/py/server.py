from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import translator
# from gevent import pywsgi
import json

app = Flask(__name__)  # 实例化app对象
# CORS(app, supports_credentials=True)
CORS(app)

testInfo = {}


@app.route('/translate_one', methods=['GET', 'POST'])  # 路由
def translate_one():
    if request.method == 'POST':
        # testInfo['name'] = '毛晓彤'
        # testInfo['age'] = '28'
        # return json.dumps(testInfo)

        print("reqeust: {}".format(request.json))
        json_data = request.json
        print("translate_one->data: {}".format(json_data))

        data = translator.translate_one(
            content=json_data['content'], src=json_data['src'], dest=json_data['dest'])
        print("json_data: {}".format(data))
        return jsonify(data)

    # else:
    #     testInfo['name'] = '白冰'
    #     testInfo['age'] = '29'
    #     return json.dumps(testInfo)

        # print(request.json)
        # return render_template('index.html')


@app.route('/translate_multi', methods=['GET', 'POST'])  # 路由
def translate_multi():
    if request.method == 'POST':
        print("reqeust: {}".format(request.json))
        json_data = request.json
        print("translate_multi->data: {}".format(json_data))

        data = translator.translate_multi(
            words=json_data['content'], src=json_data['src'], dest=json_data['dest'])
        print("json_data: {}".format(data))
        return jsonify(data)
    # else:
    #     testInfo['name'] = '白冰'
    #     testInfo['age'] = '29'
    #     return json.dumps(testInfo)


@app.route('/')
def default():
    # return 'Hello World!'
    testInfo['name'] = 'xiaoming'
    testInfo['age'] = '28'
    return json.dumps(testInfo)


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='192.168.0.102',
            # host='192.168.180.142',
            # host='0.0.0.0',  # 任何ip都可以访问
            port=5550,  # 端口
            debug=True
            )

    # server = pywsgi.WSGIServer(('0.0.0.0', 5550), app)
    # server.serve_forever()
