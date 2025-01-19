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
        'E': 40,
        'F': 10
    }

    # Special offers
    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)]    
    }

    bonus_offers = {
        'E': ('B', 2),  # Buy 2E get one B free
        'F': ('F', 3)  # Buy 2F get one F free
        }

    # Checking for invalid input - if the input `skus` is not a string or contains invalid characters
    if not isinstance(skus, str) or not all(c in prices for c in skus):
        return -1
    
    # Counting the occurences of each SKU
    counts = Counter(skus)

    total_price = 0

    # Applying bonus offers
    for item, (bonus_item, required_quantity) in bonus_offers.items():
        if item in counts and bonus_item in counts:
            free_items = counts[item] // required_quantity  # Calculating how many bonuses to apply
            
            counts[bonus_item] = max(0, counts[bonus_item] - free_items)  # Reducing the count of free items (B in this case)

    # Applying special offers and calculating the total price
    for item, count in counts.items():
        if item in special_offers:
            for offer_quantity, offer_price in sorted(special_offers[item], reverse=True):  # Applying the best offers in descending order of quantity
                total_price += (count // offer_quantity) * offer_price  # Applying the offer
                count %= offer_quantity
        
            # Adding the remaining items at their regular price
            total_price += count * prices[item]
        else:
            total_price += count * prices[item]  # No special offer, regular price

    return total_price


