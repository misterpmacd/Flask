from flask import Flask, render_template, request
import openai_secret_manager
import openai

# Initialize the Flask app
app = Flask(__name__)

# Load your OpenAI API key from the environment variables
secrets = openai_secret_manager.get_secret("openai")

# Set up the OpenAI API client
openai.api_key = secrets["api_key"]

# Define the home page route
@app.route("/")
def home():
    return render_template("index.html")

# Define the chatbot route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    # Get the user's message from the request data
    message = request.form["message"]

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"User: {message}\nBot:",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the response text from the API response
    response_text = response.choices[0].text.strip()

    # Return the response text to the user
    return response_text

if __name__ == "__main__":
    app.run(debug=True)

