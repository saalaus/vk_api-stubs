from enum import Enum
from typing import Literal


class VkKeyboardColor(Enum):
    PRIMARY: Literal["primary"]
    SECONDARY: Literal["secondary"]
    NEGATIVE: Literal["negative"]
    POSITIVE: Literal["positive"]


class VkKeyboard:
    def __init__(self, one_time: bool=False, inline: bool=False) -> None: ...
    
    def get_keyboard(self) -> str: ...
    
    @classmethod
    def get_empty_keyboard(cls) -> str: ...
    
    def add_button(self, label: str, color: VkKeyboardColor | Literal["primary", "secondary", "negative", "positive"]=VkKeyboardColor.SECONDARY,
                   payload: str| list| dict| None=None) -> None: ...
    
    def add_callback_button(self, label: str, color: VkKeyboardColor | Literal["primary", "secondary", "negative", "positive"]=VkKeyboardColor.SECONDARY,
                            payload: str | list | dict| None=None) ->None: ... 
    
    def add_location_button(self, payload: str | list | dict|None=None) -> None: ...
    
    def add_vkpay_button(self, hash: str, payload: str | list | dict|None=None) -> None: ...   
    
    
    def add_vkapps_button(self, app_id: int, owner_id: int, label: str, hash: str,
                          payload: str|dict|list|None=None) -> None: ...
    
    def add_openlink_button(self, label: str, link: str, payload: str|dict|list|None=None) -> None: ...
    
    def add_line(self) -> None: ... 