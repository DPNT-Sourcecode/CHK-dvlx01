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
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        'Y': 20,
        'Z': 21
    }

    # Mu;ti-pricing and bulk offers
    multi_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
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

    # Group discount offer
    group_offer_items = ['S', 'T', 'X', 'Y', 'Z']
    group_offer_price = 45
    group_offer_quantity = 3

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
            if bonus_item == item:  # Handling "self-bonus"
                counts[item] -= free_items
            elif bonus_item in counts:
                counts[bonus_item] = max(0, counts[bonus_item] - free_items)

    # Applying group discount offer
    group_count = sum(counts[item] for item in group_offer_items)
    while group_count >= group_offer_quantity:
        total_price += group_offer_price
        group_count -= group_offer_quantity
        for item in sorted(group_offer_items, key=lambda x: prices[x], reverse=True):  # Using items for the group discount, prioritising higher-priced items
            if counts[item] >0:
                used = min(counts[item], group_offer_quantity)  # Using as many needed for  that group
                counts[item] -= used  # Deducting the used items from counts
                group_offer_quantity -= used
                if group_offer_quantity == 0:  # Exiting once enough items have been used
                    break
        group_offer_quantity = 3  # Resetting for next group

    # Applying multi-offers and calculating the total price
    for item, count in counts.items():
        if item in multi_offers:
            for offer_quantity, offer_price in sorted(multi_offers[item], reverse=True):
                total_price += (count // offer_quantity) * offer_price
                count %= offer_quantity
            total_price += count * prices[item]
        else:
            total_price += count * prices[item]

    return total_price




