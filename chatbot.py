# chatbot.py
#reply based on keyword like fever,java etc (custom logic)
def generate_reply_for_user(user_question):
    if "fever" in user_question.lower():
        return "Please consult a doctor. It might be a viral fever. Take rest and drink water.", "Health"
    elif "java" in user_question.lower():
        return "Java is a programming language.Java is an object oriented programming language.", "Programming"
    else:
        return "Sorry, I don't understand.", "Unknown"
