#!/usr/bin/env python3
"""
Module: protobot
Description: Basic python chatbot.
"""
import time

USER_INPUT={}
BOT_RESPONSES={}

# data preprocessing
def greetings(src: str) -> [list, list]:
    """Dealing with greetings."""
    f = open(src, mode="r", encoding="utf-8")
    data = f.readlines()
    f.close()
    greetings = []
    for line in data:
        if line.endswith("\n"):
            line = line[:-1]
        line = line.lower()
        greetings.append(line)
    # responses
    f = open(src[:-4]+"_responses.txt", mode="r", encoding="utf-8")
    data = f.readlines()
    f.close()
    responses = []
    for line in data:
        if line.endswith("\n"):
            line = line[:-1]
        responses.append(line)
    return greetings, responses
def questions(src: str) -> [list, list]:
    """Dealing with Qs and As."""
    f = open(src, mode="r", encoding="utf-8")
    data = f.readlines()
    f.close()
    questions = []
    answers = []
    temp = []
    for sent in data:
        word = sent
        if word.endswith("\n"):
            word = word[:-1]
        if word.startswith("-"):
            word = word[1:].strip()
            temp.append(word)
        elif word=="":
            answers.append(temp)
            temp = []
        else:
            word = word.lower()
            questions.append(word)
    return questions, answers
def errors(src: str) -> list:
    f = open(src, mode="r", encoding="utf-8")
    data = f.readlines()
    f.close()
    my_errors = []
    for line in data:
        if line.endswith("\n"):
            line = line[:-1]
        my_errors.append(line)
    return my_errors
def load_database() -> None:
    """Loading the database."""
    g_src = "database/greetings.txt"
    USER_INPUT["greetings"], BOT_RESPONSES["responses"] = greetings(g_src)
    q_src = "database/questions.txt"
    USER_INPUT["questions"], BOT_RESPONSES["answers"] = questions(q_src)
    src_er = "database/errors.txt"
    BOT_RESPONSES["errors"] = errors(src_er)
    return None
def test_greetings():
    return None
def test_questions():
    return None
def intent_classification(sentence: str) -> str:
    return None
def database(intent: str) -> str:
    return None

NAME="Protobot"
def formulate_response(response: str) -> None:
    print("{}: {}".format(NAME, response))
    return None
def user_interact() -> str:
    return input("{}: ".format(NAME))

# load the database
print("Loading database...")
time.sleep(5)
load_database()
print("Done!")
time.sleep(1)

# Introduction
intro_msg = "Hi! my name is {}. How can I help you?".format(NAME)
formulate_response(intro_msg)
#time.sleep(1)

# general workflow
"""
while True:
    Input = user_interact()
    time.sleep(1)  # wait a seconds
    if Input.lower() == "bye":
            msg = "Bye mate :). Until next time..."
            formulate_response(msg)
            break
    intent = intent_classification(Input)
    response = database(intent)
    formulate_response(response)
    """
