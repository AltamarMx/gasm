def hello_kitty():
    """
    Display a random phrase from a list of phrases.

    :param phrases: List of phrases to choose from
    :type phrases: list
    """
    phrases = [
    "Carpe diem.",
    "Hakuna matata.",
    "Keep calm and carry on.",
    "Seize the day.",
    "The sky is the limit.",
    ]

    phrase = random.choice(phrases)
    print(phrase)

]