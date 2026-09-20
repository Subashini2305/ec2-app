from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from AWS EC2! 🚀</h1>
    <p>second test after workflow My Python Flask application is running on an EC2 instance. </p>
    """

@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <p>This testttt application was pushed to GitHub and deployed on EC2.</p>
    """

@app.route("/suba")
def suba():
    return """
    <h1>Suba</h1>
    <p>This is the Suba page.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)