from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = 'add api key'

def get_api_response(message):
    # Prepend the prompt to the message
    prompt = "give an ayurvedic solution for the following problem"
    message = prompt + " " + message

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": message},
                {"role": "user", "content": message }
            ]
        )
        if completion.choices[0].message != None:
            return completion.choices[0].message
        else:
            return 'Failed to generate response!'
    except Exception as e:
        return f"Failed to generate response: {str(e)}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")
    response = get_api_response(message)
    return response

if __name__ == "__main__":
    app.run(debug=True)
