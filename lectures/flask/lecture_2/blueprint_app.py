from configure_amazone_killer import hello, another_hello
from flask import Flask


app = Flask(__name__)

app.register_blueprint(hello, url_prefix='/blah')
app.register_blueprint(another_hello)

app.run(debug=True)
