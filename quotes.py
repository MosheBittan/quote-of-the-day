import random

QUOTES = [
    ("Talk is cheap. Show me the code.", "Linus Torvalds"),
    ("Programs must be written for people to read, and only incidentally for machines to execute.", "Harold Abelson"),
    ("Premature optimization is the root of all evil.", "Donald Knuth"),
    ("Simplicity is the soul of efficiency.", "Austin Freeman"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
]


def get_random_quote():
    return random.choice(QUOTES)


def format_quote(quote, author):
    return f'"{quote}" - {author}'


if __name__ == "__main__":
    quote, author = get_random_quote()
    print(format_quote(quote, author))
