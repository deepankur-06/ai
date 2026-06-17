import random
import string
from utils.config import INTENTS
from utils.preprocessing import preprocess_text, calculate_similarity

class ChatBot:
    def __init__(self):
        """Initialize the chatbot with intents"""
        self.intents = INTENTS
        self.conversation_history = []
    
    def classify_intent(self, user_input):
        """Classify the intent of the user input"""
        processed_input = preprocess_text(user_input)
        
        best_intent = "default"
        best_score = 0.0
        
        for intent_name, intent_data in self.intents.items():
            if intent_name == "default":
                continue
            
            patterns = intent_data["patterns"]
            for pattern in patterns:
                similarity = calculate_similarity(processed_input, preprocess_text(pattern))
                if similarity > best_score:
                    best_score = similarity
                    best_intent = intent_name
        
        # If best score is too low, use default
        if best_score < 0.3:
            best_intent = "default"
        
        return best_intent, best_score
    
    def get_response(self, user_input):
        """Generate a response based on user input"""
        intent, confidence = self.classify_intent(user_input)
        
        intent_data = self.intents.get(intent, self.intents["default"])
        responses = intent_data["responses"]
        response = random.choice(responses)
        
        # Store in conversation history
        self.conversation_history.append({
            "user": user_input,
            "bot": response,
            "intent": intent,
            "confidence": confidence
        })
        
        return response
    
    def get_history(self):
        """Get conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
