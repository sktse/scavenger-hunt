from src.item_picker import (
    pick_items,
    KITCHEN_ITEMS,
    LIVING_ITEMS,
    OFFICE_ITEMS,
)


def test_pick_items():
    results = pick_items()

    kitchen_items_count = 0
    living_items_count = 0
    office_items_count = 0
    for item in results:
        if item in KITCHEN_ITEMS:
            kitchen_items_count += 1
        elif item in LIVING_ITEMS:
            living_items_count += 1
        elif item in OFFICE_ITEMS:
            office_items_count += 1
        else:
            raise AssertionError(f"Found an item not in any category: {item}")

    assert kitchen_items_count == 5
    assert living_items_count == 5
    assert office_items_count == 5

