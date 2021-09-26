from flask import Flask

app = Flask(__name__)
counter = 0

@app.route("/")
def get_counter():
    return f"Current value of counter is {counter}"

@app.route("/stat")
def get_counter_and_increment():
    global counter
    message = f"Current value of counter is {counter}. Incremented"
    counter += 1
    return message

@app.route("/about")
def get_about_page():
    return "<h3>Hello, Pavel Shumilin</h3>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)