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
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
    }

    # Mu;ti-pricing and bulk offers
    multi_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)] 
    }

    # Bonus items offers (conditional free items)
    bonus_offers = {
        'E': ('B', 2),  # 2E get one B free
        'F': ('F', 3),  # 3F means 2F prices, 1F free
        'N': ('M', 3),  # 3N get one M free
        'R': ('Q', 3),  # 3R get one Q free
        'U': ('U', 4)   # 3U get one U free (4 total U considered for pricing)
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
            if bonus_item == item:  # Handling "self-bonus" (like for 'F')
                counts[item] -= free_items  # Each £Fs count as 2F prices, 1F free
            elif bonus_item in counts:
                counts[bonus_item] = max(0, counts[bonus_item] - free_items)  # Reducing the count of free items (B in this case)

    # Applying multi-offers and calculating the total price
    for item, count in counts.items():
        if item in multi_offers:
            for offer_quantity, offer_price in sorted(multi_offers[item], reverse=True):  # Applying the best offers in descending order of quantity
                total_price += (count // offer_quantity) * offer_price  # Applying the offer
                count %= offer_quantity
            # Adding the remaining items at their regular price
            total_price += count * prices[item]
        else:
            total_price += count * prices[item]  # No special offer, regular price

    return total_price

