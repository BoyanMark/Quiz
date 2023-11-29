# quiz.py
import random
from string import ascii_lowercase

NUMBER_OF_QUESTIONS_ASKED = 9
QUESTIONS = {
    "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
    ],
    "When does __name__ == '__main__' equal True in a Python file": [
        "When the file is run as a script",
        "When the file is imported as a module",
        "When the file has a valid name",
        "When the file only has one function",
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
    "What's the official name of the := operator": [
        "Assignment expression",
        "Named expression",
        "Walrus operator",
        "Colon equals operator",
    ],
    "What does dict.get(key) return if key isn't found in dict": [
        "None", "key", "True", "False",
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "Which built-in function can get information from the user": [
        "input", "get", "print", "write"
    ],
    "When was the first known use of the word 'quiz'": [
        "1781", "1771", "1871", "1881"
    ],
    "How do you iterate over both indices and elements in an iterable": [
        "enumerate(iterable)",
        "enumerate(iterable, start=1)",
        "range(iterable)",
        "range(iterable, start=1)",
    ],

}


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
