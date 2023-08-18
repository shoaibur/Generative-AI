# LLM-Experiments: PizzaOrderBot

Welcome to the `PizzaOrderBot` project, part of the `LLM-Experiments` repository. This bot facilitates automated order collection for a fictional pizza restaurant using the power of OpenAI's GPT models.

## Getting Started

**Clone the Repository**:

    git clone https://github.com/shoaibur/LLM-Experiments.git

    cd LLM-Experiments/PizzaOrderBot

**Set Up a Virtual Environment** (Recommended):

    python -m venv env

    source env/bin/activate # On Windows: .\env\Scripts\activate

**Install Required Packages**:

    pip install -r requirements.txt

**Environment Variables**:

The `app.py` file relies on environment variables for security reasons. Create a `.env` file in the `PizzaOrderBot` directory and add the following:

    FLASK_SECRET_KEY=your_secret_key

    OPENAI_API_KEY=your_openai_api_key

**Run the Application**:

    python app.py

Open a web browser and navigate to `http://127.0.0.1:5000/` to interact with the `PizzaOrderBot`.

## Features

- **Friendly Interaction**: The bot engages users in a friendly, conversational manner to collect pizza orders.

- **Menu Overview**: The bot can provide a detailed menu to users, ensuring they understand all available options.

- **Order Summarization**: After collecting the order details, the bot provides a comprehensive summary for user confirmation.

- **Delivery or Pickup**: The bot handles both delivery and pickup options, gathering relevant information for each.

- **Secure**: Uses environment variables to keep API and secret keys confidential.

## User Interface

The `PizzaOrderBot` provides a clean, web-based UI for users to interact with:

- A chat history box displays the conversation.

- Users can type their messages into a text input box and send them using a button.

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

- [OpenAI](https://www.openai.com/) for providing the powerful GPT models.
- And all contributors who help in enhancing this project!
