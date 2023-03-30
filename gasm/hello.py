import random
def hello_kitty():
    """
    Display a random phrase from a list of phrases.

    :param phrases: List of phrases to choose from
    :type phrases: list
    """
    sanrio_phrases = [
    "Small Gift, Big Smile",
    "The smallest of things can have a great impact",
    "Our goal is to contribute to society by creating products that make people happy",
    "When we create a product, we think about the happiness it will bring to the person who receives it",
    "Our mission is to bring smiles to people all around the world",
    "We believe in the power of friendship and the importance of nurturing relationships",
    "Friendship is the greatest treasure",
    "Spread love everywhere you go",
    "Happiness is best shared with friends",
    "Kindness is a gift everyone can afford to give",
    "Believe in the power of your dreams",
    "A smile can brighten even the darkest day",
    "The best things in life are not things, but moments",
    "When you're feeling down, lift someone else up",
    "Kind hearts are the gardens of happiness",
    "Let your heart guide your way",
    "Share your joy with the world",
    "Every day is a chance to make someone smile",
    "Together, we can create a world filled with happiness",
    "Always choose kindness and love",
    ]
    
    hello_kitty_facts = [
    "Hello Kitty's full name is Kitty White",
    "Hello Kitty is a British citizen",
    "Hello Kitty was born on November 1st",
    "Hello Kitty's favorite color is red",
    "Hello Kitty's favorite food is apple pie",
    "Hello Kitty's height is described as five apples tall",
    "Hello Kitty's weight is said to be equal to three apples",
    "Hello Kitty has a twin sister named Mimmy",
    "Hello Kitty's parents are named George and Mary White",
    "Hello Kitty's zodiac sign is Scorpio",
    "Hello Kitty's blood type is A",
    "Hello Kitty lives in the suburbs of London",
    "Hello Kitty's favorite word is 'friendship'",
    "Hello Kitty's favorite subject in school is English",
    "Hello Kitty has a pet cat named Charmmy Kitty",
    "Hello Kitty's bow is on her left ear",
    "There's a Hello Kitty themed airplane",
    "Hello Kitty has appeared on over 50,000 different products",
    "Hello Kitty was originally designed without a mouth",
    "There's a Hello Kitty theme park in Japan called Sanrio Puroland"]

    lista = [sanrio_phrases,hello_kitty_facts]
    selected = random.choice(lista)
    
    phrase = random.choice(selected)
    print(phrase)