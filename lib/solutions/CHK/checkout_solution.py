from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Price table
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    # Special offers
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)]    
    }

    bonus_offers = {
        'E': ('B', 2)  # Buy 2E get one B free
        }

    # Checking for invalid input - if the input `skus` is not a string or contains invalid characters
    if not isinstance(skus, str) or not all(c in prices for c in skus):
        return -1
    
    # Counting the occurences of each SKU
    counts = Counter(skus)

    #  Calculating the total price
    total_price = 0
    for item, count in counts.items():
        if item not in prices:  # Unkown SKU
            return -1
        
        # Checking if there is a special offer for the current item
        if item in offers:
            offer_quantity, offer_price = offers[item]
            total_price += (count // offer_quantity) * offer_price  # Applying the offer
            total_price += (count % offer_quantity) * prices[item]  # Adding the remaining items at their regular price
        else:
            total_price += count * prices[item]  # No special offer, regular price

    return total_price
