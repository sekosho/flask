from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/hello")
@app.route("/something")
def hello():
    return "<h2>my Hello World</h2>"


@app.route("/post/<int:post_id>/<post_name>")
def show_post(post_id, post_name):
    # print(type(post_id, post_name))
    return "{}:{}".format(post_id, post_name)


@app.route("/user/<string:user_name>/<int:user_id>")
def show_user(user_name, user_id):
    user_name_id = user_id + user_name
    return "<h1>{}</h1>".format(user_name_id)

# 衝突おきるのか
if __name__ == "__main__":
    app.run(debug=True)
