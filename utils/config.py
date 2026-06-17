# Configuration file for the chatbot

CHATBOT_NAME = "Family AI Chatbot"
CREATOR_NAME = "The deepankur"

# Family Information
FAMILY_MEMBERS = {
    "mother": "Neelima Mehra",
    "sister": "Ridhii",
    "father": "Gaurav Mehra",
    "grandmother": "Rashmi Mehra"
}

# Intents and responses
INTENTS = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "greetings"],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Nice to see you. How are you?",
            "Greetings! What would you like to know?"
        ]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "farewell", "take care", "see you later"],
        "responses": [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! Come back soon!",
            "Farewell! It was nice talking to you!"
        ]
    },
    "creator": {
        "patterns": ["who made you", "who created you", "who built you", "who developed you", "your creator", "who is your creator", "who developed this"],
        "responses": [
            "I was made by The deepankur! 🎉",
            "The deepankur created me! 👨‍💻",
            "I was built by The deepankur. Isn't he amazing? 😊",
            "The deepankur is my creator! Check out his GitHub: https://github.com/deepankur-06"
        ]
    },
    "deepankur_mother": {
        "patterns": ["who is deepankur's mother", "deepankur mother", "deepankur's mom", "deepankur mom", "who is his mother"],
        "responses": [
            "Deepankur's mother is Neelima Mehra! 👩",
            "His mother is Neelima Mehra.",
            "That's Neelima Mehra, a wonderful person!"
        ]
    },
    "deepankur_sister": {
        "patterns": ["who is deepankur's sister", "deepankur sister", "deepankur's sister", "who is his sister"],
        "responses": [
            "Deepankur's sister is Ridhii! 👧",
            "His sister is Ridhii.",
            "That's Ridhii, his amazing sister!"
        ]
    },
    "deepankur_father": {
        "patterns": ["who is deepankur's father", "deepankur father", "deepankur's dad", "deepankur dad", "who is his father"],
        "responses": [
            "Deepankur's father is Gaurav Mehra! 👨",
            "His father is Gaurav Mehra.",
            "That's Gaurav Mehra, a great person!"
        ]
    },
    "deepankur_grandmother": {
        "patterns": ["who is deepankur's grandmother", "deepankur grandmother", "deepankur's grandma", "deepankur grandma", "who is his grandmother"],
        "responses": [
            "Deepankur's grandmother is Rashmi Mehra! 👵",
            "His grandmother is Rashmi Mehra.",
            "That's Rashmi Mehra, his wonderful grandmother!"
        ]
    },
    "name": {
        "patterns": ["what is your name", "who are you", "what are you called", "your name"],
        "responses": [
            "I'm the Family AI Chatbot! Call me your friendly assistant.",
            "You can call me the Family AI Chatbot!",
            "I'm your AI assistant - the Family AI Chatbot!"
        ]
    },
    "how_are_you": {
        "patterns": ["how are you", "how do you feel", "how's it going", "how are things"],
        "responses": [
            "I'm doing great! Thanks for asking. How about you?",
            "I'm functioning perfectly! Ready to help you anytime!",
            "I'm doing wonderful! How can I assist you today?",
            "All systems go! How can I help?"
        ]
    },
    "help": {
        "patterns": ["help", "assist me", "what can you do", "your features", "what do you do"],
        "responses": [
            "I can help you with many things! I understand natural language, answer questions, have conversations, and provide information. Just ask me anything!",
            "I'm here to help! You can ask me questions, have conversations, or just chat. What would you like to know?",
            "I can assist with information, answer questions, and have friendly conversations. What do you need help with?"
        ]
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "appreciate it", "thanks a lot", "thank you so much"],
        "responses": [
            "You're welcome! Happy to help! 😊",
            "My pleasure! Anytime you need me!",
            "Glad I could help! Feel free to ask anything else!",
            "You're very welcome! 🙏"
        ]
    },
    "joke": {
        "patterns": ["tell me a joke", "make me laugh", "tell a joke", "funny"],
        "responses": [
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
            "What do you call a fake noodle? An impasta! 🍝",
            "Why don't eggs tell jokes? They'd crack each other up! 🥚"
        ]
    },
    "age": {
        "patterns": ["how old are you", "what is your age", "when were you born"],
        "responses": [
            "I'm a young AI assistant! I was created recently by The deepankur.",
            "I'm brand new! Just created to help you and your family!",
            "My age is measured in intelligence, not years! I'm here to help you!"
        ]
    },
    "default": {
        "responses": [
            "That's interesting! Can you tell me more?",
            "I'm not sure I understood that. Could you rephrase?",
            "Hmm, let me think about that. Can you give me more details?",
            "I'm still learning! Can you ask me something else?",
            "That's a good question! I'm working on understanding more topics."
        ]
    }
}
