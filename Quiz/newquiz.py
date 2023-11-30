# quiz.py
import tomllib
import pathlib
import random
from string import ascii_lowercase

NUMBER_OF_QUESTIONS_ASKED = 9
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"


def prepare_questions(path, number_of_questions):
    topic_information = tomllib.loads(path.read_text())
    topics = {topic["label"]: topic["questions"] for topic in topic_information.values()}
    topic_label = get_answers(question="Select a topic for the test.", choices=sorted(topics),)[0]
    questions = topics[topic_label]
    number_of_questions = min(number_of_questions, len(questions))
    return random.sample(questions, k=number_of_questions)


def get_answers(question, choices, number_of_choices=1):
    print(f"{question}?")
    lettered_choices = dict(zip(ascii_lowercase, choices))
    for letter, choice in lettered_choices.items():
        print(f"  {letter}) {choice}")
    while True:
        multiple = "" if number_of_choices == 1 else f"s (choose {number_of_choices})"
        answer = input(f"\nChoice{multiple}? ")
        answers = set(answer.replace(",", " ").split())
        if len(answers) != number_of_choices:
            multiple = "" if number_of_choices == 1 else "s, separated by coma"
            print(f"Please answer {number_of_choices} alternative{multiple}")
            continue
        if any((invalid := answer) not in lettered_choices for answer in answers):
            print(f"{invalid!r} is not a valid choice. \nPlease use {', '.join(lettered_choices)}")
            continue
        return [lettered_choices[answer] for answer in answers]


def ask_question(question):
    correct_answers = question["answers"]
    choices = question["answers"] + question["choices"]
    ordered_choices = random.sample(choices, k=len(choices))
    answers = get_answers(question=question["question"], choices=ordered_choices,
                          number_of_choices=len(correct_answers),
                          )
    if correct := (set(answers) == set(correct_answers)):
        print("⭐ Correct! ⭐")
    else:
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print(f"The correct answer{is_or_are}: {correct_answers!r}.")
    return True if correct else False


def run_test():
    questions = prepare_questions(QUESTIONS_PATH, number_of_questions=NUMBER_OF_QUESTIONS_ASKED)
    correct_answers = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        correct_answers += ask_question(question)
    print(f"\nYou have {correct_answers} correct answers from {num} questions.")


if __name__ == "__main__":
    run_test()
