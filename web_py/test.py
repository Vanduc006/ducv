from flask import Flask

n = input('name:')
app = Flask(__name__)

@app.route("/fuck")
def home():
    return f"Hello, {n}"

if __name__ == "__main__":
    app.run()
