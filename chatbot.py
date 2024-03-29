import random

# Define a list of conversation patterns and corresponding responses
conversations = [
    {"patterns": ["hi", "hello", "hey"], "responses": ["Hello!", "Hi there!", "Hey!"]},
    {"patterns": ["how are you", "how are you doing"], "responses": ["I'm good, thank you!", "I'm doing well, how about you?"]},
    {"patterns": ["bye", "goodbye", "see you later"], "responses": ["Goodbye!", "See you later!", "Take care!"]},
    # Add more patterns and responses as needed
]

def get_response(user_input):
    for pattern_set in conversations:
        for pattern in pattern_set["patterns"]:
            if pattern in user_input.lower():
                return random.choice(pattern_set["responses"])
    return "I'm sorry, I didn't understand that."

# Now the chatbot is ready to respond to user input
while True:
    user_input = input("You: ").lower()
    
    if user_input == 'exit':
        break
    
    response = get_response(user_input)
    print(f"Bot: {response}")
