from os import stat
from re import L
import jconfig
from typing import Any, Callable, Literal, NewType
from vk_api import VkApiError, Captcha
from requests import Response

DEFAULT_USER_SCOPE = ...
NAME_CASE = Literal["nom", "gen", "dat", "acc", "ins", "abl"]
Positive = NewType("Positive", int)


def get_unknown_exc_str(s: Any) -> str: ...


class VkApi:
    def __init__(self, login: str | None = ..., password: str | None = ..., token: str | None = None,
                 auth_handler: Callable[[str], str] | None = None, captcha_handler: Callable[[Captcha], str] | None = None,
                 config: ... = jconfig.Config, config_filename: str = 'vk_config.v2.json',
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
    def __init__(self, vk: str, method: str = ...) -> None: ...

    def __getattr__(self, method: str) -> VkApiMethod: ...
    def __call__(self, **kwargs: Any) -> Any: ...

    class account:
        @staticmethod
        def owner_id(*, owner_id: int) -> Literal[1]: ...

        @staticmethod
        def changePassword(*, restore_sid: str  = ..., change_password_hash: str = ...,
                           old_password: str = ..., new_password: str = ...) -> dict[Literal["token"], str]: ...

        @staticmethod
        def getActiveOffers(*, offset: Positive = ..., count: Positive = ...) -> list[Any]: ...
        @staticmethod
        def getAppPermissions(*, user_id: Positive): ...
        @staticmethod
        def getBanned(*, offset: Positive = ..., count: Positive = ...): ...
        @staticmethod
        def getCounters(*, filter: str = ..., user_id: int = ...) -> list[Any] | dict[Any, Any]: ...
        @staticmethod
        def getInfo(*, fields: str = ...) -> dict[Any, Any]: ...
        @staticmethod
        def getProfileInfo() -> dict[Any, Any]: ...
        @staticmethod
        def getPushSettings(*, token: str = ..., device_id: str = ...) -> dict[Any, Any]: ...

        @staticmethod
        def lookupContacts(*, service: str, contacts: str  = ..., mycontact: str  = ...,
                           return_all: bool = ..., fields: str  = ...): ...

        @staticmethod
        def registerDevice(*, token: str, device_id: str, device_model: str = ...,
                           device_year: int = ..., system_version: str  = ...,
                           no_text: bool = ..., subscribe: str = ...,
                           settings: str = ..., sandbox: bool = ...) -> Literal[1]: ...

        @staticmethod
        def saveProfileInfo(*, first_name: str = ..., last_name: str = ...,
                            maiden_name: str = ..., screen_name: str  = ...,
                            cancel_request_id: Positive = ...,
                            sex: Positive = ..., relation: Positive = ...,
                            relation_partner_id: int = ..., bdate: str  = ...,
                            bdate_visibility: Positive = ..., home_town: str  = ...,
                            county_id: Positive  = ..., status: str = ...) -> Literal[0, 1]: ...

        @staticmethod
        def setInfo(*, intro: Positive  = ..., own_posts_default: bool = ...,
                    no_wall_replies: bool = ..., name: str  = ..., value: str = ...
                    ) -> Literal[1]: ...

        @staticmethod
        def setNameInMenu(*, user_id: Positive, name: str = ...) -> Literal[1]: ...
        @staticmethod
        def setOffline() -> Literal[1]: ...
        @staticmethod
        def setOnline(*, voip: bool = ...) -> Literal[1]: ...

        @staticmethod
        def setPushSettings(*, device_id: str, settings: str  = ...,
                            key: str = ..., value: str = ...) -> Literal[1]: ...

        @staticmethod
        def setSilenceMode(*, token: str  = ..., device_id: str = ...,
                           time: int = ..., chat_id: int = ...,
                           user_id: int  = ..., peer_id: int = ...,
                           sound: int = ...) -> Literal[1]: ...

        @staticmethod
        def unban(*, owner_id: int = ...) -> Literal[1]: ...

        @staticmethod
        def unregisterDevice(*, token: str = ...,
                             device_id: str = ...,
                             sandbox: bool = ...) -> Literal[1]: ...

    class ads:
        ...

    class appWidgets:
        ...

    class apps:
        ...

    class auth:
        @staticmethod
        def checkPhone(*, phone: str, client_id: int = ...,
                       client_secret: str = ...,
                       auth_by_phone: bool = ...) -> Literal[1]: ...

        @staticmethod
        def restore(*, phone: str, last_name: str) -> dict[Any, Any]: ...

    class board:
        ...

    class calls:
        @staticmethod
        def start(*, group_id: int = ...) -> dict[str, Any]: ...
        @staticmethod
        def forceFinish(*, call_id: str) -> Literal[1]: ...

    class database:
        ...

    class docs:
        ...

    class donut:
        ...

    class downloadedGames:
        @staticmethod
        def getPaidStatus(*, user_id: Positive = ...) -> dict[str, bool]: ...

    class fave:
        ...

    class friends:
        ...

    class gifts:
        @staticmethod
        def get(*, user_id: Positive = ..., count: Positive = ...,
                offset: Positive = ...) -> dict[Any, Any]: ...

    class groups:
        ...

    class leadForms:
        ...

    class likes:
        ...

    class market:
        ...

    class messages:
        @staticmethod
        def addChatUser(*, chat_id: Positive, user_id: Positive = ...,
                        visible_messages_count: Positive = ...)->Literal[1]: ...
        @staticmethod
        def allowMessagesFromGroup(*, group_id: Positive, key: str = ...
                                   )->Literal[1]: ...
        @staticmethod
        def createChat(*, user_ids: str = ..., title: str = ...,
                       group_id: Positive = ...)->int: ...
        @staticmethod
        def delete(*, message_ids: str = ..., spam: bool = ...,
                   group_id: int = ..., delete_for_all: bool = ...,
                   peer_id: int = ..., cmids:str = ...)->dict[str, Literal[0, 1]]: ...
        @staticmethod
        def deleteChatPhoto(*, chat_id: Positive, group_id:Positive = ...
                            )->dict[Any, Any]: ...
        @staticmethod
        def deleteConversation(*, user_id: str = ..., peer_id: int = ...,
                               offset: Positive = ..., count: Positive = ...,
                               group_id: Positive = ...)->dict[Literal["last_deleted_id"], int]: ...
        @staticmethod
        def denyMessagesFromGroup(*, group_id: Positive) -> Literal[1]: ...
        @staticmethod
        def edit(*, peer_id: int, message: str = ..., lat: str = ...,
                 long: str = ..., attachment: str = ...,
                 keep_forward_messages: bool = ..., keep_snippets: bool = ...,
                 group_id: int = ..., dont_parse_links: bool = ...,
                 disable_mentions: bool = ..., message_id: str = ...,
                 conversation_message_id: str = ...,
                 template: str = ..., keyboard: str = ...) -> Literal[1]: ...
        @staticmethod
        def editChat(*, chat_id: Positive, title: str = ...) -> Literal[1]: ...
        @staticmethod
        def forceCallFinish(*, call_id: str) -> Literal[1]: ...
        @staticmethod
        def get(*, offset: Positive = ..., count: Positive = ..., time_offset: Positive = ...,
                filters:Positive = ..., preview_length:Positive = ...,
                last_message_id:Positive = ...) -> dict[Any, Any]: ...
        @staticmethod
        def getByConversationMessageId(*, peer_id:int, conversation_message_ids: str,
                                       extended: bool = ..., fields: str = ..., group_id: Positive = ...
                                       ) -> dict[Any, Any]: ...
        @staticmethod
        def getById(*, message_ids: str, preview_length: Positive = ...,
                    extended: bool = ..., fields: str = ...,
                    group_id: Positive = ...) -> dict[Any, Any]: ...
        @staticmethod
        def getChat(*, chat_id: Positive = ..., chat_ids: str = ...,
                    fields: str = ..., name_case: NAME_CASE = ...) -> dict[Any, Any]: ...
        @staticmethod
        def getChatPreview(*, peer_id: Positive = ..., link: str = ...,
                           fields: str = ...) -> dict[Any, Any]: ...
        @staticmethod
        def getChatUsers(*, chat_id: Positive = ..., chat_ids: str = ...,
                         fields: str = ..., name_case: NAME_CASE = ...
                         ) -> list[dict[Any, Any]]: ...
        @staticmethod
        def getConversationMembers(*, peer_id: int, offset: Positive = ...,
                                   count: Positive = ..., extended: bool = ...,
                                   fields: str = ..., group_id: int = ...
                                   )->dict[Any, Any]: ...
        @staticmethod
        def getConversations(*, offset: Positive = ..., count: Positive = ...,
                             filter: Literal["all", "important", "unanswered", "unread"] = ...,
                             extended: bool = ..., start_message_id: Positive = ...,
                             fields: str = ..., group_id: int = ...) -> dict[Any, Any]: ...
        @staticmethod
        def getConversationsById(*, peer_ids: str, extended: bool = ...,
                                 fields: str = ..., group_id: Positive = ...,
                                 ) -> dict[Any, Any]: ...
        @staticmethod
        def getDialogs(*, offset: int = ..., count: Positive = ...,
                       start_message_id: Positive = ..., preview_length: Positive = ...,
                       unread: bool = ..., important: bool = ..., unanswered: bool = ...,
                       user_id: str = ...) -> dict[Any, Any]: ...
        @staticmethod
        def getHistory(*, offset: int = ..., count: Positive = ...,
                       user_id: str = ..., peer_id: int = ...,
                       start_message_id: int = ..., rev: int = ...,
                       extended: bool = ..., fields: str = ...,
                       group_id: int = ...) -> dict[Any, Any]: ...
        @staticmethod
        def getHistoryAttachments(*, peer_id: int, media_type: str = ...,
                                  start_from: str = ...,
                                  count: Positive = ..., photo_sizes: bool = ...,
                                  fields: str = ..., group_id: Positive = ...,
                                  preserve_order: bool = ..., 
                                  max_forwards_level: Positive = ...) -> dict[Any, Any]: ...
        @staticmethod
        def getImportantMessages(*, count: Positive = ..., offset: Positive = ...,
                                 start_message_id: Positive = ...,
                                 preview_length: Positive = ...,
                                 fields: str = ..., extended: bool = ...,
                                 group_id: Positive = ...) -> Any: ...
        @staticmethod
        def getIntentUsers(*, intent: Literal["promo_newsletter", "non_promo_newsletter", "confirmed_notification"],
                           subscribe_id: Positive = ..., offset: Positive = ...,
                           count: Positive = ..., extended: bool = ...,
                           name_case: NAME_CASE = ..., fields: str = ...,
                           ) -> dict[Any, Any]: ...
        @staticmethod
        def getInviteLink(*, peer_id: Positive, reset: bool = ..., group_id: Positive = ...
                          ) -> dict[Literal["link"], str]: ...
        @staticmethod
        def getLastActivity(*, user_id: int) -> dict[Any, int]: ...
        @staticmethod
        def getLongPollHistory(*, ts: Positive = ..., pts: Positive = ...,
                               preview_length: Positive = ..., onlines: bool = ...,
                               fields: str = ..., events_limit: Positive = ...,
                               msgs_limit: Positive = ..., max_msg_id: Positive = ...,
                               group_id: int = ..., lp_version: Positive = ...,
                               last_n: Positive = ..., credentials: bool = ...,
                               extended: bool = ...) -> dict[Any, Any]: ...
        @staticmethod
        def getLongPollServer(*, need_pts: bool = ..., group_id: int = ...,
                              lp_version: Positive=...) -> dict[Any, Any]: ...
        @staticmethod
        def isMessagesFromGroupAllowed(*, group_id: str, user_id: str) -> dict[Literal["is_allowed"], int]: ...
        @staticmethod
        def joinChatByInviteLink(*, link: str) -> dict[Literal["chat_id"], int]: ...
        @staticmethod
        def markAsAnsweredConversation(*, peer_id: int, answered: bool = ...,
                                       group_id: Positive = ...) -> Literal[1]: ...
        @staticmethod
        def markAsImportant(*, message_ids: str = ..., important: Positive = ...
                            )-> list[int]: ...
        @staticmethod
        def markAsImportantConversation(*, peer_id: int, important: bool = ...,
                                        group_id: Positive = ...) -> Literal[1]: ...
        @staticmethod
        def markAsRead(*, message_ids: str = ..., peer_id: str = ..., 
                       start_message_id: Positive = ..., group_id: int = ...,
                       mark_conversation_as_read: bool = ...,
                       up_to_cmid: Positive = ...) -> Literal[1]: ...
        @staticmethod
        def pin(*, peer_id: int, message_id: Positive = ...,
                conversation_message_id: Positive = ...) -> dict[Any, Any]: ...
        @staticmethod
        def removeChatUser(*, chat_id: Positive, user_id: int = ...,
                           member_id: int = ...) -> Literal[1]: ...
        @staticmethod
        def restore(*, message_id: Positive, group_id: Positive = ...) -> Literal[1]: ...
        @staticmethod
        def search(*, q: str = ..., peer_id: int = ..., date: Positive = ...,
                   preview_length: Positive = ..., offset: Positive = ...,
                   count: Positive = ..., extended: bool = ...,
                   fields: str = ..., group_id: Positive = ...) -> dict[Any, Any]: ...
        @staticmethod
        def searchConversations(*, q: str = ..., count: Positive = ...,
                                extended: bool = ..., fields: str = ...,
                                group_id: Positive = ...) -> dict[Any, Any]: ...
        @staticmethod
        def searchDialogs(*, q: str = ..., limit: Positive = ..., 
                          fields: str = ...) -> dict[Any, Any]: ...
        @staticmethod
        def send(*, user_id: int = ..., random_id: int = ..., peer_id: int = ...,
                 peer_ids: str = ..., domain: str = ..., 
                 chat_id: Positive = ..., user_ids: str = ...,
                 message: str = ..., guid: int = ..., lat: str = ..., long: str = ...,
                 attachment: str = ..., reply_to: int = ..., 
                 forward_messages: str = ..., forward: str = ...,
                 sticker_id: Positive = ..., group_id: Positive = ...,
                 keyboard: str = ..., template: str = ..., payload: str = ...,
                 content_source: str = ..., dont_parse_links: bool = ...,
                 disable_mentions: bool = ..., intent: str = ...,
                 subscribe_id: Positive = ...) -> dict[Any, Any]: ...
        @staticmethod
        def sendMessageEventAnswer(*, event_id: str, user_id: int, peer_id: int,
                                   event_data: str = ...) -> Literal[1]: ...
        @staticmethod
        def setActivity(*, user_id: str = ..., type: Literal["typing", "audiomessage"] = ...,
                        peer_id: int = ..., group_id: Positive = ...) -> Literal[1]: ...
        @staticmethod
        def setChatPhoto(*, file: str) -> dict[Any, Any]: ...
        @staticmethod
        def startCall(*, group_id: int = ...) -> dict[Any, Any]: ...
        @staticmethod
        def unpin(*, peer_id: int, group_id: Positive = ...) -> Literal[1]: ...
        
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
        @staticmethod
        def searchPodcast(*, search_string: str, offset: Positive = ...,
                          count: Positive = ...) -> Any: ...

    class polls:
        ...

    class prettycards:
        ...

    class search:
        @staticmethod
        def getHints(*, q: str = ..., offset: Positive = ...,
                     limit: Positive = ..., filters: str = ...,
                     fields: str = ..., search_global: bool = ...
            ) -> dict[str, Any]: ...

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
        def get(*, user_ids: str = ..., fields: str = ...,
                name_case: NAME_CASE = ...
                ) -> list[dict]:
            """Возвращает расширенную информацию о пользователях."""
        @staticmethod
        def getFollowers(*, user_id: Positive = ..., offset: Positive = ...,
                         count: Positive = ..., fields: str = ..., name_case: NAME_CASE = ...
                         ) -> dict[Any, Any]: ...

        @staticmethod
        def getSubscriptions(*, user_id: Positive = ..., extended: bool = ...,
                             offset: Positive = ..., count: Positive = ..., fields: str = ...) -> dict[Any, Any]: ...

        @staticmethod
        def report(*, user_id: Positive, type: Literal["porn", "spam",
                   "insult", "advertisеment"], comment: str = ...) -> Literal[1]: ...

        @staticmethod
        def search(*, q: str = ..., sort: Literal[0, 1] = ..., offset: Positive = ..., count: Positive = ...,
                   fields: str = ..., city: Positive = ..., country: Positive = ..., hometown: str = ...,
                   university_country: Positive = ..., university: Positive = ..., university_year: Positive = ...,
                   university_faculty: Positive = ..., university_chair: Positive = ...,
                   sex: Literal[0, 1, 2] = ..., status: Literal[1, 2, 3, 4, 5, 6, 7, 8] = ...,
                   age_from: Positive = ..., age_to: Positive = ..., birth_day: Positive = ...,
                   birth_month: Positive = ..., birth_year: Positive  = ..., online: bool = ...,
                   has_photo: bool = ..., school_country: Positive = ..., school_city: Positive = ..., school_class: Positive = ...,
                   school: Positive  = ..., school_year: Positive = ...,
                   religion: str = ..., company: str = ..., position: str = ...,
                   group_id: Positive = ..., from_list: str  = ...) -> dict[Any, Any]: ...

    class utils:
        @staticmethod
        def checkLink(*, url: str) -> dict[str, str]: ...
        @staticmethod
        def deleteFromLastShortened(*, key: str) -> Literal[1]: ...
        @staticmethod
        def getLastShortenedLinks(*, count: Positive=..., offset: Positive = ...
                                  ) -> dict[Any, Any]: ...
        @staticmethod
        def getLinkStats(*, key: str, source: str = ..., access_key: str = ...,
                         interval: Literal["hour", "day", "week", "month", "forever"] = ...,
                         intervals_count: Positive = ..., extended: bool = ...
                         )->dict[Any, Any]: ...
        @staticmethod
        def getServerTime() -> int: ...
        @staticmethod
        def getShortLink(*, url: str, private: bool = ...) -> dict[Any, Any]: ...
        @staticmethod
        def resolveScreenName(*, screen_name: str) -> dict[Any, Any]: ...
        

    class video:
        ...

    class wall:
        ...

    class widgets:
        ...

    class audio:
        @staticmethod
        def get(*, owner_id: int = ..., album_id: int = ...,
                audio_ids: str = ..., need_user: bool = ...,
                offset: Positive = ..., count: Positive = ...) -> dict[Any, Any]:
            "Возвращает список аудиозаписей пользователя или сообщества."
        @staticmethod
        def getById(*, audios: str) -> list[dict[Any, Any]]:
            "Возвращает информацию об аудиозаписях."
        @staticmethod
        def getLyrics(*, lyrics_id: int) -> dict[Any, Any]:
            "Возвращает текст аудиозаписи."
        @staticmethod
        def search(*, q: str, auto_complete: bool = ...,
                   lyrics: bool = ..., performer_only: bool = ...,
                   sort: int = ..., search_own: Literal[0, 1] = ...,
                   offset: Positive = ..., count: Positive = ...) -> dict[Any, Any]:
            "Возвращает список аудиозаписей в соответствии с заданным критерием поиска."
        @staticmethod
        def getUploadServer() -> dict[Literal["upload_url"], str]:
            "Возвращает адрес сервера для загрузки аудиозаписей."
        @staticmethod
        def save(*, server: int, audio: str, hash: str = ..., artist: str = ...,
                 title: str = ...) -> dict[Any, Any]:
            "Сохраняет аудиозаписи после успешной загрузки."
        @staticmethod
        def add(*, audio_id: Positive, owner_id: int, group_id: int = ...,
                playlist_id: Positive = ..., ref: str = ...,
                access_key: str  = ..., track_code: str = ...) -> int:
            "Копирует аудиозапись на страницу пользователя или группы."
        @staticmethod
        def delete(*, audio_id: Positive, owner_id: int) -> Literal[1]:
            "Удаляет аудиозапись со страницы пользователя или сообщества."
        @staticmethod
        def edit(*, owner_id: int, audio_id: Positive, artist: str = ...,
                 title: str = ..., text: str = ...,
                 genre_id: Positive = ..., no_search: bool = ...) -> int:
            "Редактирует данные аудиозаписи на странице пользователя или сообщества."
        @staticmethod
        def reorder(*, audio_id: Positive, owner_id: int = ..., before: int = ...,
                    after: int = ...) -> Literal[1]:
            "Изменяет порядок аудиозаписи, перенося ее между аудиозаписями, идентификаторы которых переданы параметрами after и before."
        @staticmethod
        def restore(*, audio_id: Positive, owner_id: int = ...) -> dict[Any, Any]:
            "Восстанавливает аудиозапись после удаления."
        @staticmethod
        def getPlaylists(*, owner_id: int = ..., offset: Positive = ...,
                      cont: int = 50) -> dict[Any, Any]:
            "Возвращает список альбомов аудиозаписей пользователя или группы."
        @staticmethod
        def addPlaylist(*, group_id: Positive = ..., title: str = ...) -> int:
            "Создает пустой альбом аудиозаписей."
        @staticmethod
        def editPlaylist(*, album_id: Positive, title: str, group_id: Positive = ...
                      ) -> Literal[1]:
            "Редактирует название альбома аудиозаписей."
        @staticmethod
        def deletePlaylist(*, group_id: Positive = ..., album_id: Positive = ...
                        ) -> Literal[1]:
            "Удаляет альбом аудиозаписей."
        @staticmethod
        def moveToPlaylist(*, audio_ids: str, group_id: Positive = ..., album_id: Positive = ...
                        ) -> Literal[1]:
            "Перемещает аудиозаписи в альбом."
        @staticmethod
        def setBroadcast(*, audio: str = ..., target_ids: str) -> dict[Any, Any]:
            "Транслирует аудиозапись в статус пользователю или сообществу."
        @staticmethod
        def getBroadcastList(*, filter: Literal["friends", "groups", "all"] = ...,
                             active: bool = ...) -> list[dict[Any, Any]]:
            "Возвращает список друзей и сообществ пользователя, которые транслируют музыку в статус."
        @staticmethod
        def getRecommendations(*, target_audio: str = ..., user_id: Positive  = ...,
                               offset: Positive  = ..., count: Positive = ...,
                               shuffle: bool = ...) -> list[dict[Any, Any]]:
            "Возвращает список рекомендуемых аудиозаписей на основе списка воспроизведения заданного пользователя или на основе одной выбранной аудиозаписи."
        @staticmethod
        def getPopular(*, only_eng: bool = ..., genre_id: Positive  = ...,
                       offset: Positive = ..., count: Positive = ...) -> list[dict[Any, Any]]:
            "Возвращает список аудиозаписей из раздела “Популярное”."
        @staticmethod
        def getCount(*, owner_id: int) -> int:
            "Возвращает количество аудиозаписей пользователя или сообщества."
