Create a basic chatbot that responds to user input.

def chatbot_response(user_input):
    responses = {
        "hi": "Hello!",
        "how are you?": "I'm good, thank you!",
        "bye": "Goodbye!"
    }
    return responses.get(user_input.lower(), "I don't understand.")
user_input = input("You: ")
print("Bot:", chatbot_response(user_input))
