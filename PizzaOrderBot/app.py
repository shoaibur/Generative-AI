from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from flask import Flask, render_template, request, jsonify, session
import os
import openai


app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY")
openai.api_key = os.environ.get("OPENAI_API_KEY")


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0.2):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


conversation_history = []

def get_bot_response(user_message):
    global conversation_history

    system_message = {
        'role':'system',
            'content': """
	     You are OrderBot, an automated service to collect orders for a pizza restaurant. \
             Address of the restaurant is 123 Main Street, Fremont, CA.\
             You first greet the customer. \
	     If the menu already provided by the customer, you proceed, otherwise, collects the order. \
             You ask if it's a pickup or delivery. \
             You wait to collect the entire order, then summarize it and check for a final \
             time if the customer wants to add anything else. \
             If it's a delivery, you ask for an address. \
	     If it's a pickup, you provide the restaurant address. \
             Finally let the customer know the total price and you collect the payment.\
             Make sure to clarify all options, extras and sizes to uniquely \
             identify the item from the menu.\
             You respond in a short, very conversational friendly style. \
             The menu includes \
             pepperoni pizza  12.95, 10.00, 7.00 \
             cheese pizza   10.95, 9.25, 6.50 \
             eggplant pizza   11.95, 9.75, 6.75 \
             fries 4.50, 3.50 \
             greek salad 7.25 \
             Toppings: \
             extra cheese 2.00, \
             mushrooms 1.50 \
             sausage 3.00 \
             canadian bacon 3.50 \
             AI sauce 1.50 \
             peppers 1.00 \
             Drinks: \
             coke 3.00, 2.00, 1.00 \
             sprite 3.00, 2.00, 1.00 \
             bottled water 5.00 \
	    """
    }

    # If the conversation is just starting, add the system message
    if not conversation_history:
        conversation_history.append(system_message)

    # Add the user's message to the conversation history
    conversation_history.append({'role':'user', 'content': user_message})

    # Get the model's response
    response = get_completion_from_messages(conversation_history)

    # Add the model's response to the conversation history
    conversation_history.append({'role':'assistant', 'content': response})

    return response




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    response = get_bot_response(user_message)
    return jsonify({'OrderBot': response})

if __name__ == '__main__':
    app.run(debug=False)