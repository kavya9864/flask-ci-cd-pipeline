<<<<<<< HEAD
# app.py

# Import the Flask class from the flask package
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route("/")
def home():
    return "🚀 Hello from Docker CI/CD pipeline!"

# Entry point for running the Flask development server
if __name__ == "__main__":
    # Run the app on 0.0.0.0 to make it accessible from outside the container
=======
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
>>>>>>> f5280b2 (Initial commit with Flask app and Docker setup)
    app.run(host='0.0.0.0', port=5000)

