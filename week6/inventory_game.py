# --- Game State ---
# in this game users wander through a misty magical forest and need to find a well which is a portal back home, on their way they collect several objects that help them find the way
import time
import sys

inventory = []
items_glade= [
    {"name": "berries🫐", "type": "food", "description": "Strenghtens you for the journey."},
    {"name": "acorn🌰", "type": "plant", "description": "Food for animals."},
    {"name": "squirrel🐿", "type": "animal", "description": "May have some clues for you."},
    {"name": "lense🔎", "type": "tool", "description": "Helps you see animal traces."},
    {"name": "bottle🍶", "type": "tool", "description": "Stores water."},
    {"name": "lemon🍋", "type": "tool", "description": "Reveals paint on the map."},
    {"name": "magicmap🗺", "type": "tool", "description": "Overview of the magical forest."}
]


MAX_INVENTORY_SIZE = 5

# --- Functions ---

#function for typewriter style of print() functions
def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)


#function for listing all items in the inventory
def show_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("You have...:")
        for item in inventory:
            print(f"{item['name']} ({item ['type']})")

#function for listing all items in current setting
def show_glade_items():
    print("Glade items:")
    for item in items_glade:
        time.sleep(1)
        print(f"{item['name']} ({item ['type']})")

#function for picking up an item from the setting if inventory limit is not met yet
def pick_up(item_name):
    for item in items_glade:
        if item_name.lower() in item['name'].lower():
            if len(inventory) < MAX_INVENTORY_SIZE:
                inventory.append(item)
                items_glade.remove(item)
                print(f"You picked up the {item['name']}.")
            else:
                print("Your inventory is full.")
            return
    print(f"There is no {item_name} here.")

#function for dropping an item from user's inventory
def drop(item_name):
    for item in inventory:
        if item_name.lower() in item['name'].lower():
            inventory.remove(item)
            items_glade.append(item)
            print(f"You have dropped {item ['name']}.")
            return
    print(f"You don't have {item_name} in your inventory.")

#function for usage of the item
def use(item_name):
   for item in inventory:
     if item_name.lower() in item['name'].lower():
         if item ["type"] == "food":
             print("You have gained strenght for your journey.")
         elif item ["type"] == "animal":
             print("You met a helpful forest inhabitant, listen closely to him (he likes acorns;)).")
         elif item ["type"] == "plant":
             print("You made your companion happy and eager to help you find the well💦.")
        #specific effect for the different tools
         elif item ["type"] == "tool":
            if "lense" in item["name"]:
                print("You used the magnifying glass and discovered animal traces that lead you to the well💦.")
            elif "bottle" in item["name"]:
                print("Nothing special happens.")
            elif "lemon" in item["name"]:
                print("If you have the map, you take it and squeeze the lemon on top of it. A path reveals. ")
            elif "magicmap" in item["name"]:
                print("Also take the lemon and you'll be able to see the path to the well💦")

         return

#function for examining an item
def examine(item_name):
    for item in inventory:
        if item_name.lower() in item['name'].lower():
            print(f"{item['name']}: {item['description']}")
            return

    for item in items_glade:
        if item_name.lower() in item['name'].lower():
            print(f"{item['name']}: {item['description']}")
            return
    print(f"There is no {item_name} here.")


# --- Game Loop ---

def game_loop():
    print("🌳🌳🌳🌳🌳🌳✨🍁🍃🐿💦🐿🍃🍁✨🌳🌳🌳🌳🌳🌳")
    time.sleep(1)
    print("Welcome to the Inventory Game!")
    time.sleep(1)
    typing("You wake up....Your head still hurts and as you open your eyes you see the sunbeams shining through tree crowns. You seem to be on a glade. Where are you ? How have you come here? And how will you find home???")
    time.sleep(1)
    print()
    print("Type 'help' for a list of actions.")

    while True:
        action = input("\n> ").strip().lower()

        match action.split():
            case ["help"]:
                print("Actions: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
            case ["inventory"]:
                show_inventory()
            case ["look"]:
                show_glade_items()
            case ["pickup", item_name]:
                pick_up(item_name)
            case ["drop", item_name]:
                drop(item_name)
            case ["use", item_name]:
                use(item_name)
            case ["examine", item_name]:
                examine(item_name)
            case ["quit"]:
                print("Thanks for playing!")
                break
            case _: # else
                print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
