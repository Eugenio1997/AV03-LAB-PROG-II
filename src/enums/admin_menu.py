from enum import Enum


Admin_Menu = Enum(
    "Admin_Menu",
    [
        "REGISTRY_NEW_CAR",
        "DISPLAY_ALL_CARS",
        "DISPLAY_CAR_BY_ID",
        "DELETE_CAR_BY_ID",
        "EDIT_CAR_BY_ID",
        "EXIT",
    ],
)
