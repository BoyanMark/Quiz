# quiz.py
import random
from string import ascii_lowercase

number_of_quiz_questions = 9
QUESTIONS = {
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
    "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
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
    ]
}

number_of_questions = min(number_of_quiz_questions, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=number_of_questions)
score = 0
for num, (question, choices) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = choices[0]
    labeled_choices = dict(zip(ascii_lowercase, random.sample(choices, k=len(choices))))
    for label, choice in labeled_choices.items():
        print(f"  {label}) {choice}")

    while (answer_label := input("\nChoice? ")) not in labeled_choices:
        print(f"Please answer one of {', '.join(labeled_choices)}")

    answer = labeled_choices.get(answer_label)
    if answer == correct_answer:
        score += 1
        print("⭐ CORRECT! ⭐")
    else:
        print(f" The answer is {correct_answer!r}, not {answer!r}.")

print(f"\nYou got {score} correct out of {num} questions")
