import nltk
from nltk.chat.util import Chat, reflections
# Ensure you have the necessary NLTK data
nltk.download('punkt')
# Define pairs of patterns and responses
pairs = [
[r"my name is (.*)",["Hello %1, How are you today ?",]],
[r"hi|hey|hello",["Hello", "Hey there",]],
[r"what is your name ?",["I am a chatbot created using NLTK",]],
[r"how are you ?",["I'm doing good. How about You ?",]],
[r"sorry (.*)",["Its alright", "Its OK, never mind",]],
[r"I am (.*) (good|well|okay|ok)",["Nice to hear that", "Alright, great !",]],
[r"(.*) age?",["I am a computer program, I do not have an age",]],
[r"what (.*) want ?",["Make me an offer I can't refuse",]],
[r"(.*) created ?",["I was created using NLTK library in Python", "Some smart person",]],
[r"(.*) (location|city) ?",["I am based in the cloud",]],
[r"how is the weather in (.*)?",["Weather in %1 is amazing like always", "It's too hot here in %1", 
                            "It's too cold here in %1", "I have never heard about %1"]],
[r"quit",["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]],
[r"(.*)",["I didn't understand that. Can you rephrase?", "I'm not sure I understand."]],
]
# Create the chatbot
chatbot = Chat(pairs, reflections)
# Start the conversation
print("Hi, I'm your chatbot. Type 'quit' to exit.")
while True:
    user_input = input(">you:- ")
    if user_input.lower() == "quit":
        print("Bye for now. See you soon :)")
        break
    response = chatbot.respond(user_input)
    print(f"chatbot:-{response}")