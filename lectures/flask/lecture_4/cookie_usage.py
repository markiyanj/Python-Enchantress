from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    if 'username' not in request.cookies:
        resp = make_response({'hello': 'unknown'})
        resp.set_cookie('username', 'Dude')
    else:
        resp = make_response({'hello': request.cookies['username']})
    return resp


if __name__ == '__main__':
    app.run(debug=True)
