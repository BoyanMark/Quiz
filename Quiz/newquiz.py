# quiz.py
import tomllib
import pathlib
import random
from string import ascii_lowercase


NUMBER_OF_QUESTIONS_ASKED = 9
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())


def prepare_questions(questions, number_of_questions):
    number_of_questions = min(number_of_questions, len(questions))
    return random.sample(list(questions.items()), k=number_of_questions)


def get_answer(question, choices):
    print(f"{question}?")
    lettered_choices = dict(zip(ascii_lowercase, choices))
    for letter, choice in lettered_choices.items():
        print(f"  {letter}) {choice}")
    while (answer_letter := input("\nChoice? ")) not in lettered_choices:
        print(f"Please answer one of {', '.join(lettered_choices)}")
    return lettered_choices[answer_letter]


def ask_question(question, choices):
    correct_answer = choices[0]
    ordered_choices = random.sample(choices, k=len(choices))
    answer = get_answer(question, ordered_choices)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return True
    else:
        print(f"The correct answer is {correct_answer!r}, not {answer!r}")
        return False


def run_test():
    questions = prepare_questions(QUESTIONS, number_of_questions=NUMBER_OF_QUESTIONS_ASKED)
    correct_answers = 0
    for num, (questions, choices) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        correct_answers += ask_question(questions, choices)
    print(f"\nYou have {correct_answers} correct answers from {num} questions.")


if __name__ == "__main__":
    run_test()
