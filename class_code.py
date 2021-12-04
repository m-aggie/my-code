from typing import List

class Item:
    # def __init__(self, name: str) -> None:
    #     self.name = name
        pass


class ShopListMenu():
    # done b
    def __init__(self, items: List[Item], selected_index: int, type_items: str, cost:float) -> None:
        self.items = items
        self.selected_index = selected_index
        self.type_items = type_items
        self.cost = cost
    
    # done b
    def select_next(self) -> None:
        """Moves the selected index up one item."""
        max_index = len(self.items) - 1
        self.selected_index = min(self.selected_index + 1,max_index)

    # done b
    def select_previous(self) -> None:
        """Moves the selected index down one item."""
        self.selected_index = max(self.selected_index - 1, 0)

    # done b
    def get_selected(self) -> Item:
        """Returns the item that matches the selected index from the list of items.
        Returns:
            The item selected.
        """
        return self.items[self.selected_index]

    def get_cost(self) -> float:
        return self.cost

    # def draw(self, screen):

#maggie
class Player:
    def __init__(self, name, level, gold) -> None:
        self.name = name
        self.level = level
        self.gold = gold
        

#maggie
class Store:
    def __init__(self, item_selected) -> None:
       self.weapons = ShopListMenu(item_selected)
       self.armor = ShopListMenu(item_selected)
       self.consumables = ShopListMenu(item_selected)
       self.price = ShopListMenu()

    def get_price(self) -> float:
        return self.price

    @staticmethod
    def can_purchase_weapon(player, item):
        """Determines if the player can buy a weapon depending if they have enough gold
        Returns"
            does not return anything
        """
        if player.gold < price.get_cost:
            raise Exception("You do not have enough gold to purchase this object") 

    def can_purchase_armor(self):
        """Checks to see if the player can buy armor
        Returns:
            does not return anything
        """
        pass

    def can_purchase_consumable(self):
        """Determines if the player can buy consumables based on how much gold they have
        Returns:
            does not return anything
        """
        pass
