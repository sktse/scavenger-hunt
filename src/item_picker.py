import random

from typing import List

KITCHEN_ITEMS = [
    "Can Opener",
    "Butter Knife",
    "Chef's Knife",
    "A Cup with a Logo",
    "A Cup with Text",
    "Pot",
    "Pan",
    "Sponge",
    "Coffee or Tea",
    "Dish Soap",
    "Cooking Appliance",
    "Bottled or Canned Beverage",
    "Spatula",
    "Hot Sauce",
    "Spice",
    "Reusable Container",
    "Serrated Knife",
    "Alcohol",
    "A Single Peppercorn",
    "An egg",
    "Flour",
    "Spice blend",
]

OFFICE_ITEMS = [
    "Blue Pen",
    "Black Pen",
    "Coloured Writing Device (not Blue or Black)",
    "Mouse",
    "USB Cable",
    "Scissors",
    "Sharpie",
    "Notebook or Notepad",
    "Headphones",
    "Something Mailed",
    "Box Cutter",
    "A Piece of Paper with Your Name on it",
    "A Phone",
    "Memory Card or USB Stick",
    "USB Hub",
    "Tape",
]

LIVING_ITEMS = [
    "Hat",
    "Coat",
    "Fitness Equipment",
    "Pet or Plant",
    "Photo in Frame",
    "Disinfectant Wipes",
    "Matching Pair of Socks",
    "Fiction Book",
    "Non-Fiction Book",
    "Magazine",
    "Board Game",
    "Hardware Tool",
    "Skin Care",
    "Reusable Grocery Bag",
    "Sun Glasses",
    "Gloves",
    "Keys",
    "Remote Control",
    "Pillow",
    "Hand Sanitizer",
    "Toilet Paper",
    "A Piece of a Puzzle",
]


def pick_items() -> List[str]:
    kitchen_items = random.sample(KITCHEN_ITEMS, k=5)
    office_items = random.sample(OFFICE_ITEMS, k=5)
    living_items = random.sample(LIVING_ITEMS, k=5)
    combined_items = kitchen_items + office_items + living_items
    random.shuffle(combined_items)

    return combined_items
