from flask import Flask


app = Flask(__name__)


app.config.from_object('default_config')
app.config.from_envvar('AMAZONE_KILLER_SETTINGS')


@app.route('/')
def hello():
    return (
        f"hello db_host:{app.config['DB_HOST']} "
        f"db_port: {app.config['DB_PORT']}"
    )


if __name__ == "__main__":
    app.run(debug=True)
