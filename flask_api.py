from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def welcome():
    if request.method == 'GET':
        return "Hello World!"
    elif request.method == 'POST':
        print(type(str(request.data)))
        res = str(request.data ,"utf-8")
       
        #res = res.encode().decode("utf-8")
        print(type(res))
        return res

if __name__ == '__main__':
    app.run()

