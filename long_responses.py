import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "Yes, Artificial Intelligence is the ability of a digital computer or computer-controlled robot to perform tasks commonly associated with intelligent beings."
R_ADVICE2 = "Alan Turing"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
