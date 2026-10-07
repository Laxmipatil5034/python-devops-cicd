from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Python DevOps CI/CD Project</h1>
    <p>Application is running successfully!</p>
    <p>Built with Python and Flask.</p>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "python-devops-cicd"
    })


@app.route("/about")
def about():
    return jsonify({
        "project": "Python DevOps CI/CD Automation",
        "version": "1.0",
        "technology": "Python Flask"
    })


if __name__  == "__main__":
    app.run(host="0.0.0.0", port=5000)
