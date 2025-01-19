from collections import Counter

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
    if not isinstance(skus, str) or not all(c.isalpha() and c.isupper() for c in skus):
        return -1
    
    # Counting the occurences of each SKU
    counts = Counter(skus)

    #  Calculating the total price
    total_price = 0
    for item, count in counts.items():
        if item not in prices:  # Unkown SKU
            return -1
        
        # Checking ig there is a specia offer for the 

