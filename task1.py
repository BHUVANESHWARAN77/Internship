import nltk
import random
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I\'m good, how about you?']),
    (r'what is your name', ['my name is mini.', 'You can call me mini.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Take care!']),
    (r'my name is (.*)', ['Nice to meet you, %1!']),
    (r' i love you', ['i love you too', 'iam not intrested']),
    (r'(.*) (weather|temperature) in (.*)', ['I\'m sorry, I am just a text-based chatbot and I don\'t have real-time information.']),
    # Add more patterns and responses based on your requirements
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Function to start the chat
def start_chat():
    print("Hello! I'm a simple chatbot. You can type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Goodbye Have a nice day!")
            break
        response = chatbot.respond(user_input)
        print("MINI:", response)

if __name__ == "__main__":
    start_chat()

