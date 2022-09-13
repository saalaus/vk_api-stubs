from typing import Any, Callable, Iterator
from .vk_api import VkApi
from .execute import VkFunction


class VkTools:
    def __init__(self, vk: VkApi) -> None: ...
    def get_all_iter(self, method: str, max_count: int, values:dict|None=None, key: str='items',
                     limit: int|None=None, stop_fn: Callable[[Any], bool]|None=None, negative_offset:bool=False) -> Iterator[Any]: ...
    
    def get_all(self, method: str, max_count: int, values:dict|None=None, key: str='items', limit: int|None=None,
                stop_fn: Callable[[Any], bool]|None=None, negative_offset: bool=False) -> list[Any]:...
    
    def get_all_slow_iter(self, method: str, max_count: int, values: dict|None=None, key: str='items',
                          limit: int|None=None, stop_fn: Callable[[Any], bool] | None=None, negative_offset: bool=False) -> Iterator[Any]: ...
    
    def get_all_slow(self, method: str, max_count: int, values: dict|None=None, key: str='items',
                          limit: int|None=None, stop_fn: Callable[[Any], bool] | None=None, negative_offset: bool=False) -> list[Any]: ...
    
    
vk_get_all_items: VkFunction