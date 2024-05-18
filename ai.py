import streamlit as st
import random

# Dictionary of emotion responses
emotion_responses = {
    "Happy": [
        "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
        "The only way to be happy is to love. - Seneca",
        "Every day is a new day, and you'll never be able to find happiness if you don't move on. - Carrie Underwood",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "I told my computer I needed a break and now it won't stop sending me vacation ads.",
        "Why did the math book look sad? Because it had too many problems."
    ],
    "Sad": [
        "The wound is the place where the Light enters you. - Rumi",
        "The way sadness works is one of the strange riddles of the world. - Lemony Snicket",
        "Sadness flies away on the wings of time. - Jean de La Fontaine",
        "In the midst of winter, I found there was, within me, an invincible summer. - Albert Camus",
        "Grief is the price we pay for love. - Queen Elizabeth II",
        "The way to love anything is to realize that it may be lost. - Gilbert K. Chesterton"
    ],
    "Excited": [
        "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "The best preparation for tomorrow is doing your best today. - H. Jackson Brown Jr.",
        "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence. - Helen Keller",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "You have to expect things of yourself before you can do them. - Michael Jordan",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela"
    ],
    "Angry": [
        "You cannot shake hands with a clenched fist. - Indira Gandhi",
        "Speak when you are angry - and you'll make the best speech you'll ever regret. - Laurence J. Peter",
        "Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured. - Mark Twain",
        "Get mad, then get over it. - Colin Powell",
        "Anger is a wind which blows out the lamp of the mind. - Robert Green Ingersoll",
        "Holding onto anger is like drinking poison and expecting the other person to die. - Buddha",
        "In moments of anger, the mind is the weakest. - Publilius Syrus",
        "Anger, if not restrained, is frequently more hurtful to us than the injury that provokes it. - Lucius Annaeus Seneca",
        "Anger is never without a reason, but seldom with a good one. - Benjamin Franklin",
        "When anger rises, think of the consequences. - Confucius"
    ],
    "Surprised": [
        "The only thing that should surprise us is that there are still some things that can surprise us. - Francois de La Rochefoucauld",
        "Life is full of surprises, but the biggest one of all is learning what it takes to handle them. - Unknown",
        "There is no greater surprise than the surprise of being loved. - Charles Morgan",
        "Surprise is the greatest gift which life can grant us. - Boris Pasternak",
        "The greatest discovery of my generation is that a human being can alter his life by altering his attitudes. - William James",
        "Life is full of surprises, but only the unexpected ones surprise us. - Ivan Klíma",
        "The only thing that should surprise us is that there are still some things that can surprise us. - François de La Rochefoucauld",
        "Surprise is the greatest gift which life can grant us. - Boris Pasternak",
        "Life is full of surprises, but only the unexpected ones surprise us. - Ivan Klíma",
        "The only thing that should surprise us is that there are still some things that can surprise us. - François de La Rochefoucauld"
    ],
    "Bored": [
        "Boredom is the feeling that everything is a waste of time; serenity, that nothing is. - Thomas Szasz",
        "The capacity for delight is the gift of paying attention. - Julia Cameron",
        "There are no uninteresting things, only uninterested people. - G.K. Chesterton",
        "The cure for boredom is curiosity. There is no cure for curiosity. - Dorothy Parker",
        "Boredom is the feeling that everything is a waste of time; serenity, that nothing is. - Thomas Szasz",
        "The capacity for delight is the gift of paying attention. - Julia Cameron",
        "There are no uninteresting things, only uninterested people. - G.K. Chesterton",
        "The cure for boredom is curiosity. There is no cure for curiosity. - Dorothy Parker",
        "Boredom is the feeling that everything is a waste of time; serenity, that nothing is."
    ],
    "Sarcasm": [
        "Oh, because that worked out so well last time...",
        "Well, this day was just perfect... said no one ever.",
        "Wow, you're like a detective, but even better.",
        "Sure, because that's exactly what I wanted to do today...",
        "Well, aren't you just a ray of sunshine?",
        "Of course, because that's the logical solution.",
        "Oh, congratulations! You've reached a whole new level of annoying.",
        "Wow, you must be a mind reader with skills like that.",
        "Because clearly, that's the most efficient way to handle this situation."
    ],
    "Depressed": [
        "Nothing matters anymore...",
        "What's the point? Everything just turns to dust anyway.",
        "Life is just a series of disappointments.",
        "I don't want to get out of bed today... or any day.",
        "Why bother trying when I'll just fail again?",
        "I'm tired... just so tired.",
        "I'm drowning in sadness and there's no way out.",
        "I wish I could disappear and never come back.",
        "Why does everything hurt so much?",
        "There's no light at the end of this tunnel..."
    ]
    # Add more emotions and responses as needed
}

# Function to generate response based on selected emotion
def generate_response(emotion):
    if emotion in emotion_responses:
        return random.choice(emotion_responses[emotion])
    else:
        return "No quotes available for this emotion."

# Streamlit UI components
st.title("CHATTIE 🤖")
st.markdown("### Your emotional assistant")
st.markdown("***Are you ready to go through a rollercoaster of emotions?***")
# Dropdown for selecting emotion
emotion = st.selectbox("Select an Emotion  :) Let's Explore 🚀", options=list(emotion_responses.keys()))

# Button to generate response
if st.button("Generate"):
    if not emotion:
        st.error("Please select an emotion.")
    else:
        response = generate_response(emotion)
        st.text_area("Response:", value=response, height=100)

