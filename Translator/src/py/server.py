from flask import Flask,jsonify,render_template
# from gevent import pywsgi
import json
 
app = Flask(__name__)#实例化app对象
 
testInfo = {}
 
@app.route('/translate_one',methods=['GET','POST'])#路由
def test_post():
    # testInfo['name'] = 'xiaoming'
    # testInfo['age'] = '28'
    # return json.dumps(testInfo)

    json_data = request.json
    logger.info(f"json_data:{json_data}")
    return jsonify(json_data)
 
@app.route('/')
def hello_world():
    return 'Hello World!'
 
@app.route('/index')
def index():
    return render_template('index.html')
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',#任何ip都可以访问
            port=5550,#端口
            debug=True
            )
    
    # server = pywsgi.WSGIServer(('0.0.0.0', 5550), app)
    # server.serve_forever()