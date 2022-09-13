from os import stat
from turtle import position
import jconfig
from typing import Any, Callable, Literal, Union
from vk_api.enums import VkUserPermissions
from vk_api import VkApiError, Captcha
from requests import Response

DEFAULT_USER_SCOPE = sum(VkUserPermissions)
NAME_CASE = Literal["nom", "gen", "dat", "acc", "ins", "abl"]
Positive = int


def get_unknown_exc_str(s: Any) -> str: ...


class VkApi:
    def __init__(self, login: str | None = None, password: str | None = None, token: str | None = None,
                 auth_handler: Callable[[str], str] | None = None, captcha_handler: Callable[[Captcha], str] | None = None,
                 config: Callable = jconfig.Config, config_filename: str = 'vk_config.v2.json',
                 api_version: str = '5.92', app_id: int = 6222115, scope: int = DEFAULT_USER_SCOPE,
                 client_secret: str | None = None, session: str | None = None) -> None: ...

    def _sid(self) -> str: ...

    def auth(self, reauth: bool = False, token_only: bool = False) -> None: ...

    def _auth_cookies(self, reauth: bool = False) -> None: ...

    def _auth_token(self, reauth: bool = False) -> None: ...

    def _vk_login(self, captcha_sid: int | None = None, captcha_key: str | int | None = None) -> None: ...

    def _pass_twofactor(self, auth_response: Response) -> str: ...

    def _pass_security_check(self, response: Response | None = None) -> str: ...

    def check_sid(self) -> dict | None: ...

    def _api_login(self) -> None: ...

    def server_auth(self) -> None: ...

    def code_auth(self, code: str, redirect_url: str) -> dict: ...

    def _check_token(self) -> bool: ...

    def captcha_handler(self, captcha: Captcha) -> None: ...

    def need_validation_handler(self, error: Exception) -> None: ...

    def http_handler(self, error: Exception) -> None: ...

    def too_many_rps_handler(self, error: VkApiError): ...

    def auth_handler(self) -> None: ...

    def get_api(self) -> VkApiMethod: ...

    def method(self, method: str, values: dict | None = None, captcha_sid: str | int | None = None, captcha_key: str | None = None,
               raw: bool = False) -> dict: ...


class VkApiGroup(VkApi):
    ...


class VkApiMethod(object):
    def __init__(self, vk: str, method: str | None = None) -> None: ...

    def __getattr__(self, method: str) -> VkApiMethod: ...

    class account:
        @staticmethod
        def owner_id(*, owner_id: int) -> Literal[1]: ...

        @staticmethod
        def changePassword(*, restore_sid: str | None = None, change_password_hash: str | None = None,
                           old_password: str | None = None, new_password: str | None = None) -> dict[Literal["token"], str]: ...

        @staticmethod
        def getActiveOffers(*, offset: Positive | None = None, count: Positive | None = None) -> list[Any]: ...
        @staticmethod
        def getAppPermissions(*, user_id: Positive): ...
        @staticmethod
        def getBanned(*, offset: Positive | None = None, count: Positive | None = None): ...
        @staticmethod
        def getCounters(*, filter: str | None = None, user_id: int | None = None) -> list[Any] | dict[Any, Any]: ...
        @staticmethod
        def getInfo(*, fields: str | None = None) -> dict[Any, Any]: ...
        @staticmethod
        def getProfileInfo() -> dict[Any, Any]: ...
        @staticmethod
        def getPushSettings(*, token: str | None = None, device_id: str | None = None) -> dict[Any, Any]: ...

        @staticmethod
        def lookupContacts(*, service: str, contacts: str | None = None, mycontact: str | None = None,
                           return_all: bool = False, fields: str | None = None): ...

        @staticmethod
        def registerDevice(*, token: str, device_id: str, device_model: str | None = None,
                           device_year: int | None = None, system_version: str | None = None,
                           no_text: bool = False, subscribe: str | None = None,
                           settings: str | None = None, sandbox: bool = False) -> Literal[1]: ...

        @staticmethod
        def saveProfileInfo(*, first_name: str | None = None, last_name: str | None = None,
                            maiden_name: str | None = None, screen_name: str | None = None,
                            cancel_request_id: Positive | None = None,
                            sex: Positive | None = None, relation: Positive | None = None,
                            relation_partner_id: int | None = None, bdate: str | None = None,
                            bdate_visibility: Positive | None = None, home_town: str | None = None,
                            county_id: Positive | None = None, status: str | None = None) -> Literal[0, 1]: ...

        @staticmethod
        def setInfo(*, intro: Positive | None = None, own_posts_default: bool = False,
                    no_wall_replies: bool = False, name: str | None = None, value: str | None = None
                    ) -> Literal[1]: ...

        @staticmethod
        def setNameInMenu(*, user_id: Positive, name: str | None = None) -> Literal[1]: ...
        @staticmethod
        def setOffline() -> Literal[1]: ...
        @staticmethod
        def setOnline(*, voip: bool = False) -> Literal[1]: ...

        @staticmethod
        def setPushSettings(*, device_id: str, settings: str | None = None,
                            key: str | None = None, value: str | None = None) -> Literal[1]: ...

        @staticmethod
        def setSilenceMode(*, token: str | None = None, device_id: str | None = None,
                           time: int | None = None, chat_id: int | None = None,
                           user_id: int | None = None, peer_id: int | None = None,
                           sound: int | None = None) -> Literal[1]: ...

        @staticmethod
        def unban(*, owner_id: int | None = None) -> Literal[1]: ...

        @staticmethod
        def unregisterDevice(*, token: str | None = None,
                             device_id: str | None = None,
                             sandbox: bool = False) -> Literal[1]: ...

    class ads:
        ...

    class appWidgets:
        ...

    class apps:
        ...

    class auth:
        @staticmethod
        def checkPhone(*, phone: str, client_id: int | None = None,
                       client_secret: str | None = None,
                       auth_by_phone: bool = False) -> Literal[1]: ...

        @staticmethod
        def restore(*, phone: str, last_name: str) -> dict[Any, Any]: ...

    class board:
        ...

    class calls:
        @staticmethod
        def start(*, group_id: int|None = None) -> dict[str, Any]: ...
        @staticmethod
        def forceFinish(*, call_id: str) -> Literal[1]: ...

    class database:
        ...

    class docs:
        ...

    class donut:
        ...

    class downloadedGame:
        ...

    class fave:
        ...

    class friends:
        ...

    class gifts:
        ...

    class groups:
        ...

    class leadForms:
        ...

    class likes:
        ...

    class market:
        ...

    class messages:
        ...

    class newsfeed:
        ...

    class notes:
        ...

    class notifications:
        ...

    class orders:
        ...

    class pages:
        ...

    class photos:
        ...

    class places:
        ...

    class podcasts:
        ...

    class polls:
        ...

    class prettycards:
        ...

    class search:
        ...

    class secure:
        ...

    class stats:
        ...

    class status:
        ...

    class storage:
        ...

    class store:
        ...

    class stories:
        ...

    class streaming:
        ...

    class users:
        @staticmethod
        def get(*, user_ids: str = "", fields: str = "",
                name_case: NAME_CASE = "nom"
                ) -> list[dict]:
            """Возвращает расширенную информацию о пользователях."""
        @staticmethod
        def getFollowers(*, user_id: Positive | None = None, offset: Positive = 0,
                         count: Positive = 100, fields: str = "", name_case: NAME_CASE = "nom") -> dict[Any, Any]: ...

        @staticmethod
        def getSubscriptions(*, user_id: Positive | None = None, extended: bool = False,
                             offset: Positive = 0, count: Positive | None = None, fields: str | None = None) -> dict[Any, Any]: ...

        @staticmethod
        def report(*, user_id: Positive, type: Literal["porn", "spam",
                   "insult", "advertisеment"], comment: str = "") -> Literal[1]: ...

        @staticmethod
        def search(*, q: str = "", sort: Literal[0, 1] | None = None, offset: Positive = 0, count: Positive | None = None,
                   fields: str = "", city: Positive | None = None, country: Positive | None = None, hometown: str | None = None,
                   university_country: Positive | None = None, university: Positive | None = None, university_year: Positive | None = None,
                   university_faculty: Positive | None = None, university_chair: Positive | None = None,
                   sex: Literal[0, 1, 2] | None = None, status: Literal[1, 2, 3, 4, 5, 6, 7, 8] | None = None,
                   age_from: Positive | None = None, age_to: Positive | None = None, birth_day: Positive | None = None,
                   birth_month: Positive | None = None, birth_year: Positive | None = None, online: bool | None = None,
                   has_photo: bool | None = None, school_country: Positive | None = None, school_city: Positive | None = None, school_class: Positive | None = None,
                   school: Positive | None = None, school_year: Positive | None = None,
                   religion: str | None = None, company: str | None = None, position: str | None = None,
                   group_id: Positive | None = None, from_list: str | None = None) -> dict[Any, Any]: ...

    class utils:
        ...

    class video:
        ...

    class wall:
        ...

    class widgets:
        ...

    class audio:
        @staticmethod
        def get(*, owner_id: int | None = None, album_id: int | None = None,
                audio_ids: str | None = None, need_user: bool = False,
                offset: Positive | None = None, count: Positive | None = None) -> dict[Any, Any]:
            "Возвращает список аудиозаписей пользователя или сообщества."
        @staticmethod
        def getById(*, audios: str) -> list[dict[Any, Any]]:
            "Возвращает информацию об аудиозаписях."
        @staticmethod
        def getLyrics(*, lyrics_id: int) -> dict[Any, Any]:
            "Возвращает текст аудиозаписи."
        @staticmethod
        def search(*, q: str, auto_complete: bool = False,
                   lyrics: bool = False, performer_only: bool = False,
                   sort: int | None = None, search_own: Literal[0, 1] | None = None,
                   offset: Positive | None = None, count: Positive | None = None) -> dict[Any, Any]:
            "Возвращает список аудиозаписей в соответствии с заданным критерием поиска."
        @staticmethod
        def getUploadServer() -> dict[Literal["upload_url"], str]:
            "Возвращает адрес сервера для загрузки аудиозаписей."
        @staticmethod
        def save(*, server: int, audio: str, hash: str | None = None, artist: str | None = None,
                 title: str | None = None) -> dict[Any, Any]:
            "Сохраняет аудиозаписи после успешной загрузки."
        @staticmethod
        def add(*, audio_id: Positive, owner_id: int, group_id: int | None = None,
                playlist_id: Positive | None = None, ref: str | None = None,
                access_key: str | None = None, track_code: str | None = None) -> int:
            "Копирует аудиозапись на страницу пользователя или группы."
        @staticmethod
        def delete(*, audio_id: Positive, owner_id: int) -> Literal[1]:
            "Удаляет аудиозапись со страницы пользователя или сообщества."
        @staticmethod
        def edit(*, owner_id: int, audio_id: Positive, artist: str | None = None,
                 title: str | None = None, text: str | None = None,
                 genre_id: Positive | None = None, no_search: bool = False) -> int:
            "Редактирует данные аудиозаписи на странице пользователя или сообщества."
        @staticmethod
        def reorder(*, audio_id: Positive, owner_id: int | None = None, before: int | None = None,
                    after: int | None = None) -> Literal[1]:
            "Изменяет порядок аудиозаписи, перенося ее между аудиозаписями, идентификаторы которых переданы параметрами after и before."
        @staticmethod
        def restore(*, audio_id: Positive, owner_id: int | None = None) -> dict[Any, Any]:
            "Восстанавливает аудиозапись после удаления."
        @staticmethod
        def getAlbums(*, owner_id: int | None = None, offset: Positive | None = None,
                      cont: int = 50) -> dict[Any, Any]:
            "Возвращает список альбомов аудиозаписей пользователя или группы."
        @staticmethod
        def addAlbum(*, group_id: Positive | None = None, title: str | None = None) -> int:
            "Создает пустой альбом аудиозаписей."
        @staticmethod
        def editAlbum(*, album_id: Positive, title: str, group_id: Positive | None = None
                      ) -> Literal[1]:
            "Редактирует название альбома аудиозаписей."
        @staticmethod
        def deleteAlbum(*, group_id: Positive | None = None, album_id: Positive | None = None
                        ) -> Literal[1]:
            "Удаляет альбом аудиозаписей."
        @staticmethod
        def moveToAlbum(*, audio_ids: str, group_id: Positive | None = None, album_id: Positive | None = None
                        ) -> Literal[1]:
            "Перемещает аудиозаписи в альбом."
        @staticmethod
        def setBroadcast(*, audio: str | None = None, target_ids: str) -> dict[Any, Any]:
            "Транслирует аудиозапись в статус пользователю или сообществу."
        @staticmethod
        def getBroadcastList(*, filter: Literal["friends", "groups", "all"] | None = None,
                             active: bool = False) -> list[dict[Any, Any]]:
            "Возвращает список друзей и сообществ пользователя, которые транслируют музыку в статус."
        @staticmethod
        def getRecommendations(*, target_audio: str | None = None, user_id: Positive | None = None,
                               offset: Positive | None = None, count: Positive = 100,
                               shuffle: bool = False) -> list[dict[Any, Any]]:
            "Возвращает список рекомендуемых аудиозаписей на основе списка воспроизведения заданного пользователя или на основе одной выбранной аудиозаписи."
        @staticmethod
        def getPopular(*, only_eng: bool = False, genre_id: Positive | None = None,
                       offset: Positive | None = None, count: Positive = 100) -> list[dict[Any, Any]]:
            "Возвращает список аудиозаписей из раздела “Популярное”."
        @staticmethod
        def getCount(*, owner_id: int) -> int:
            "Возвращает количество аудиозаписей пользователя или сообщества."
