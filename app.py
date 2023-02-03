from urllib import response
from flask import Flask, make_response, request


app = Flask(__name__)


@app.route('/')
def index():
    response = make_response([{'id':1, 'title': 'Title'}])
    response.headers['Content-Type'] = 'application/json'
    # print(request.headers)
    # print(request.headers['Authorization'])
    # print(request.headers['Content-Type'])
    # print(request.json['name'])
    # print(request.json.get('name'))
    # print(request.method)
    # print(request.path)
    # print(request.url)
    return response


if __name__ == '__main__':
    app.run(debug=True)

