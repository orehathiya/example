from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world() -> dict[str, str]:
    return {"message": "Hello, World!"}

@app.route("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(debug=True)
