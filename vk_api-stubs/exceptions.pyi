from typing import Callable
from requests import Response

from vk_api.vk_api import VkApi

class VkApiError(Exception):...


class AccessDenied(VkApiError):...


class AuthError(VkApiError):...


class LoginRequired(AuthError):...


class PasswordRequired(AuthError):...


class BadPassword(AuthError):...


class AccountBlocked(AuthError):...


class TwoFactorError(AuthError):...


class SecurityCheck(AuthError):
    def __init__(self, phone_prefix: str|None=None, phone_postfix: str|None=None, response: Response | None=None) -> None:...
    
class ApiError(VkApiError):
    def __init__(self, vk: VkApi, method: Callable, values: dict, raw: dict, error: dict) -> None: ...
    
class ApiHttpError(VkApiError): ...

class Captcha(VkApiError): ...

class VkAudioException(Exception): ...
class VkToolsException(VkApiError): ...
class VkRequestsPoolException(Exception): ...