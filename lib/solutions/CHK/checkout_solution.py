

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Price table
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    # Special offers
    offers = {
        'A': (3, 130),
        'B': (2, 45)    
    }

    # Checking for invalid input - if the input `skus` is not a string or contains invalid characters
    if not isinstance(skus, str) or not all()

