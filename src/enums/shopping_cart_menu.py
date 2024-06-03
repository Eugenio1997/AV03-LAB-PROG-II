from enum import Enum


Shopping_Cart_Menu = Enum(
    "Shopping_Cart_Menu",
    [
        ("ADD_ITEM"),
        ("REMOVE_ITEM"),
        ("DISPLAY_CART"),
        ("VIEW_CONFIRMED_ORDERS"),
        ("RETRIEVE_LAST_ORDER"),
        ("FINISH_PURCHASE"),
        ("CANCEL_PURCHASE"),
        ("BACK_TO_MAIN_MENU"),
    ],
)