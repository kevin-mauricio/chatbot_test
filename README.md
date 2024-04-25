Asistente Virtual
Overview

This program implements a simple virtual assistant using natural language processing (NLP) techniques. It interacts with users through a Streamlit web interface, understanding their queries and providing appropriate responses. The assistant is trained on a dataset of intents and responses using a neural network model.
Components

    front.py: This file contains the Streamlit application code responsible for the front-end interface of the virtual assistant. It handles user inputs, displays chat messages, and interacts with the backend for processing.

    training.py: Here, the training data is prepared and used to train a neural network model. It preprocesses text data, generates bag-of-words representations, and trains the model to classify intents based on user queries.

    chatbot.py: This module contains functions for predicting intents of user queries and generating responses using the trained neural network model. It preprocesses user input, predicts the intent, and retrieves a suitable response from the dataset.

Usage

To use the virtual assistant:

    Ensure all required dependencies are installed.
    Run front.py to start the Streamlit application.
    Interact with the virtual assistant by typing queries into the input field provided.
    The assistant will respond with appropriate answers based on the trained model.

Files

    intents.json: Contains predefined intents and responses used for training and inference.
    Roles.py: Defines roles for the assistant and user.
    words.pkl: Pickled file containing the preprocessed word vocabulary.
    classes.pkl: Pickled file containing the classes of intents.
    chatbot_model.h5: Trained neural network model for intent classification.

Dependencies

    Streamlit
    NLTK
    Keras
    NumPy
    Click