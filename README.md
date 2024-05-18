![sat_hack_img](https://github.com/Meenakshimkumar/sat-hack/assets/118379816/dc1a8917-609d-49ce-a430-50aeba656f28)
# Chattie 
### Your Emotional Assistance
This project is a simple emotion-based chatbot implemented using Streamlit, a popular framework for building web applications with Python. The chatbot allows users to select an emotion from a dropdown menu, and upon clicking a button, it generates a response corresponding to that emotion.

The emotions supported by the chatbot include "Happy," "Sad," "Excited," "Angry," "Surprised," "Bored," "Sarcasm," and "Depressed." Each emotion category contains a set of predefined responses tailored to evoke or reflect that particular emotion.

The chatbot's purpose is to demonstrate how different language models or response sets can be utilized to create conversational experiences that vary in tone and sentiment. By selecting an emotion, users can interact with the chatbot and receive responses that align with their chosen emotional state.

The project showcases how Streamlit can be used to create interactive and engaging applications with minimal code. It also highlights the importance of considering user experience and emotional context when designing conversational interfaces.

## Team members
1. [Aleena Bino](https://github.com/aleena24bino)
2. [Meenakshi Pramod](https://github.com/MeenakshiPramod)
3. [Meenakshi M Kumar](https://github.com/Meenakshimkumar)
## Link to product walkthrough

![Img1](https://github.com/Meenakshimkumar/sat-hack/assets/118379816/46b7b9d5-bc23-4661-818b-fe027dc1596b)
![Img2](https://github.com/Meenakshimkumar/sat-hack/assets/118379816/f3591841-5f68-4777-9f08-714dda5ed969)

## How it works?

**1)Setup and Import Libraries:**

The project begins by importing the necessary libraries, particularly Streamlit for building the web interface and the random module for selecting random responses.

**2)Define Emotion Responses:**

A dictionary is created to store predefined responses for each emotion. Each key in the dictionary corresponds to an emotion, and the value is a list of responses related to that emotion.

**3)Create Streamlit User Interface (UI):**

**Title**: The title of the chatbot is displayed using st.title().
**Emotion Selection**: A dropdown menu is provided for users to select an emotion. This is done using st.selectbox(), which takes a list of emotions as options.
**Generate Button**: A button is created with st.button(). When clicked, it triggers the response generation.

**4)Generate and Display Response:**

When the button is clicked, the selected emotion is checked. If an emotion is selected, a random response from the corresponding list in the dictionary is chosen.
The selected response is then displayed in a text area using st.text_area().


## Libraries used 

1. Streamlit
2. Random


## How to configure
Instructions for setting up project
## How to Run
Instructions for running
