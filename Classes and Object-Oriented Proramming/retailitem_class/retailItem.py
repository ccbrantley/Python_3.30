#retailItem
import retailItem_class
def main():
    item_1 = 'Jacket', 12, 59.95
    item_2 = 'Designer Jeans', 40, 34.95
    item_3 = 'Shirt', 20, 24.95
    retailItems = [item_1, item_2, item_3]
    for key in retailItems:
        display_output(key)
def display_output(retailItems):
    description = retailItems[0]
    inventory = retailItems[1]
    price = retailItems[2]
    retailItem = retailItem_class.RetailItem(description, inventory, price)
    print('Description: ', retailItem.get_description(), sep='')
    print('Inventory: ', retailItem.get_inventory(), sep='')
    print('Price: $', format(retailItem.get_price()), sep='')
    print()
main()
