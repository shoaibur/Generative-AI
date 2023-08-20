# AskURL Documentation

## Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [Usage](#usage)
- [Features](#features)
- [Methods](#methods)
- [Limitations](#limitations)
- [Conclusion](#conclusion)

# Overview
**`URLChat`** is a Python-based chatbot that interacts with users based on the content of a specified webpage. By leveraging the capabilities of the OpenAI model, it provides answers derived from the webpage's content, ensuring contextually relevant and accurate responses.

# Purpose
The primary objectives of **URLChat** are to:
* Allow users to query specific details or topics from a webpage without having to read the entire content.
* Offer an interactive medium for users to extract insights or information from the content of the webpage.
* Serve as a research or informational tool, especially beneficial when dealing with extensive or dense webpages.

# Usage
To utilize URLChat, follow these steps:
* Create an instance of the class with the desired webpage URL.
* Invoke the interactive_chat() method to initiate the chat session.
* Example:
    ```
    webpage_url = "https://example.com"
    url_chat = URLChat(webpage_url)
    url_chat.interactive_chat()
    ```

# Features
* **Webpage Content Extraction**: Uses the `requests` library to fetch and process the content of the provided webpage URL.

* **Dynamic Interaction**: Users can interact with the chatbot in a session format. The chatbot retains previous interactions, ensuring context-aware answers.

* **Verbose & Detailed Responses**: Crafted to deliver comprehensive answers. If a constraint regarding answer length is set, it adheres to it.*

# Methods
* **fetch_content_from_url(url)**: Retrieves and processes the content of the specified webpage URL.

* **get_response_from_query(query)**: Accepts a user query and returns a response based on the webpage content. Also maintains chat history for context.

* **interactive_chat()**: Starts an interactive chat session. Users can continue posing questions, and to conclude the session, they can type 'exit'.

# Limitations
* The chatbot's performance is directly tied to the clarity and accuracy of the webpage content. If the content is ambiguous or lacks clarity, the chatbot's responses might not be as precise.

* While the model is designed to provide verbose and detailed answers, the accuracy remains contingent on the model's interpretation and the content of the webpage.

# Conclusion
**`URLChat`** presents a novel approach to interact with webpage content, simplifying the process for users to extract and comprehend information. Whether for research purposes, quick summaries, or detailed insights from a webpage, it stands as an invaluable tool.
