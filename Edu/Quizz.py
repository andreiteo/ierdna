#!/usr/local/bin/python3

#o lista de intrebari
question_prompts = [
    "What color are apples?\n(a)Red/Green\n(b)Purple\n(c)Orange\n\n",
    "What color are Bananas?\n(a)Teal\n(b)Magenta\n(c)Yellow\n\n",
    "What color are strawberries?\n(a)Yellow\n(b)Red\n(c)Blue\n\n"
]


#creezi clasa in care sa se incadreze obiectele intrebari
class question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


#creezi o lista sau un array ca nu inteleg in pula mea ce e asta cu indexul din lista din question prompts
questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for i in questions:
        answer = input(i.prompt)
        if answer == i.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)))

run_test(questions)
