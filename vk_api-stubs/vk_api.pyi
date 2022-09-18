import jconfig
from typing import Any, Callable, Literal, TypeAlias, TypedDict
from vk_api import VkApiError, Captcha
from requests import Response

DEFAULT_USER_SCOPE = ...
NAME_CASE: TypeAlias = Literal["nom", "gen", "dat", "acc", "ins", "abl"]
Positive: TypeAlias =  int
Text: TypeAlias = dict[Any, Any] | str | list[dict[Any, Any]]
VkObject: TypeAlias = dict[Any, Any]
ListOfVkObjects: TypeAlias = list[VkObject]
ResponseOfItems: TypeAlias = TypedDict("ResponseOfItems", {
    "count": int,
    "items": ListOfVkObjects
})
ExtendedResponseOfItems: TypeAlias = TypedDict("ResponseOfItems", {
    "count": int,
    "items": ListOfVkObjects,
    "profiles": ListOfVkObjects,
    "groups": ListOfVkObjects,
    "poll": VkObject,
    "default_order": int,
    "can_add_topics": int
})


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

    def check_sid(self) -> dict[Any, Any] | None: ...

    def _api_login(self) -> None: ...

    def server_auth(self) -> None: ...

    def code_auth(self, code: str, redirect_url: str) -> dict[Any, Any]: ...

    def _check_token(self) -> bool: ...

    def captcha_handler(self, captcha: Captcha) -> None: ...

    def need_validation_handler(self, error: Exception) -> None: ...

    def http_handler(self, error: Exception) -> None: ...

    def too_many_rps_handler(self, error: VkApiError): ...

    def auth_handler(self) -> None: ...

    def get_api(self) -> VkApiMethod: ...

    def method(self, method: str, values: dict[Any, Any] | None = None, captcha_sid: str | int | None = None, captcha_key: str | None = None,
               raw: bool = False) -> Any: ...


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
                           old_password: str = ..., new_password: str = ...
                           ) -> dict[Literal["token"], str]: ...

        @staticmethod
        def getActiveOffers(*, offset: Positive = ..., count: Positive = ...
                            ) -> ResponseOfItems: ...
        @staticmethod
        def getAppPermissions(*, user_id: Positive
                              ) -> int: ...
        @staticmethod
        def getBanned(*, offset: Positive = ..., count: Positive = ...
                      ) -> ResponseOfItems: ...
        @staticmethod
        def getCounters(*, filter: str = ..., user_id: int = ...
                        ) -> VkObject: ...
        @staticmethod
        def getInfo(*, fields: str = ...
                    ) -> VkObject: ...
        @staticmethod
        def getProfileInfo() -> VkObject: ...
        @staticmethod
        def getPushSettings(*, token: str = ..., device_id: str = ...
                            ) -> VkObject: ...

        @staticmethod
        def lookupContacts(*, service: str, contacts: str  = ..., mycontact: str  = ...,
                           return_all: bool = ..., fields: str  = ...
                           ) -> ListOfVkObjects: ...

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
                            county_id: Positive  = ..., status: str = ...
                            ) -> Literal[0, 1]: ...

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
        @staticmethod
        def getAccounts() -> ListOfVkObjects: ...
        @staticmethod
        def getClients(*, account_id: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def createClients(*, data: Text, account_id: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def updateClients(*, data: Text, account_id: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def deleteClients(*, ids: str, account_id: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def getCampaigns(*, account_id: str = ..., client_id: int = ...,
                         include_deleted: bool = ..., campaign_ids: str = ...,
                         fields: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def createCampaigns(*, data: str, account_id: str = ...)->ListOfVkObjects: ...
        @staticmethod
        def updateCampaigns(*, data: str, account_id: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def deleteCampaigns(*, ids: str, account_id: str = ...)->ListOfVkObjects: ...
        @staticmethod
        def getAds(*, account_id: str = ..., client_id: int = ...,
                   include_deleted: bool = ..., only_deleted: bool = ...,
                   campaign_ids: Text = ..., ad_ids: Text = ...,
                   limit: int = ..., offset: int = ...)->ListOfVkObjects: ...
        @staticmethod
        def getAdsLayout(*, account_id: str = ..., client_id: int = ...,
                         include_deleted: bool = ..., only_deleted: bool = ...,
                         campaign_ids: Text = ..., ad_ids: Text = ...,
                         limit: int = ..., offset: int = ...) -> ListOfVkObjects: ...
        @staticmethod
        def getAdsTargeting(*, account_id: str = ..., client_id: int = ...,
                            include_deleted: bool = ..., only_deleted: bool = ...,
                            campaign_ids: Text = ..., ad_ids: Text = ...,
                            limit: int = ..., offset: int = ...) -> ListOfVkObjects: ...
        @staticmethod
        def createAds(*, data: Text, account_id: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def updateAds(*, data: Text, account_id: str = ...) -> ListOfVkObjects:...
        @staticmethod
        def deleteAds(*, ids: str, account_id: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def checkLink(*, account_id: str = ..., 
                      link_type: Literal["community", "post", "application", "video", "site"],
                      link_url: str = ..., campaign_id: int = ...) -> VkObject: ...
        @staticmethod
        def getStatistics(*, account_id: str = ...,
                          ids_type: Literal["ad", "campaign", "client", "office"] = ...,
                          ids: str = ...,
                          period: Literal["day", "week", "month", "year", "overall"] = ...,
                          date_from: str = ..., date_to: str = ..., stats_fields: str = ...
                          ) -> ListOfVkObjects: ...
        @staticmethod
        def getDemographics(*, account_id: str = ...,
                            ids_type: Literal["ad", "campaign"] = ...,
                            ids: str = ...,
                            period: Literal["day", "month", "overall"] = ...,
                            date_from: str = ..., date_to: str = ...
                            ) -> ListOfVkObjects: ...
        @staticmethod
        def getPostsReach(*, account_id: str = ...,
                          ids_type: Literal["ad", "campaign"] = ...,
                          ids: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def getBudget(*, account_id: str = ...)->int: ...
        @staticmethod
        def getOfficeUsers(*, account_id: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def addOfficeUsers(*, data: Text, account_id: str = ...)->ListOfVkObjects: ...
        @staticmethod
        def updateOfficeUsers(*, data: Text, account_id: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def removeOfficeUsers(*, ids: str, account_id: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def getTargetingStats(*, link_url: str, account_id: int = ..., client_id: int = ...,
                              criteria: Text = ..., ad_id: int = ...,
                              ad_format: int = ..., ad_platform: str = ...,
                              ad_platform_no_wall: str = ...,
                              ad_platform_no_ad_network: str = ...,
                              link_domain: str = ..., need_precise: bool = ...,
                              impressions_limit_period: int = ...) -> VkObject: ...
        @staticmethod
        def getSuggestions(*, section: str, ids: str = ..., q: str = ...,
                           country: int = ..., cities: str = ...,
                           lang: Literal["ru", "ua", "en"] = ...) -> ListOfVkObjects: ...
        @staticmethod
        def getCategories(*, lang: str = ...) -> dict[Literal["v1", "v2"], VkObject]: ...
        @staticmethod
        def getUploadURL(*, ad_format: int = ..., icon: int = ...) -> str: ...
        @staticmethod
        def getVideoUploadURL() -> str: ...
        @staticmethod
        def getFloodStats(*, account_id: str = ...) -> VkObject: ...
        @staticmethod
        def getRejectionReason(*, account_id: str = ..., ad_id: str = ...) -> VkObject: ...
        @staticmethod
        def createTargetGroup(*, account_id: str = ..., client_id: int = ...,
                              name: str = ..., lifetime: int = ...,
                              target_pixel_id: int = ..., target_pixel_rules: Text,
                              ) -> VkObject: ...
        @staticmethod
        def updateTargetGroup(*, account_id: str = ..., client_id: int = ...,
                              target_group_id: str = ..., name: str = ...,
                              domain: str = ..., lifetime: int = ...,
                              target_pixel_id: int = ..., target_pixel_rules: Text = ...
                              ) -> Literal[1]: ...
        @staticmethod
        def deleteTargetGroup(*, target_group_id: str, account_id: str = ...,
                              client_id: int = ...) -> Literal[1]: ...
        @staticmethod
        def shareTargetGroup(*, target_group_id: str, account_id: str = ...,
                             client_id: int = ..., share_with_client_id: int = ...
                             )->VkObject: ...
        @staticmethod
        def getTargetGroups(*, account_id: str = ..., client_id: int = ...,
                            extended: bool = ...) -> ListOfVkObjects: ...
        @staticmethod
        def importTargetContacts(*, target_group_id: str, account_id: str = ...,
                                 client_id: int = ..., contacts: str = ...) -> int: ...
        @staticmethod
        def removeTargetContacts(*, target_group_id: str, account_id: str = ...,
                                 client_id: int = ..., contacts: str = ...) -> Literal[1]: ...
        @staticmethod
        def createTargetPixel(*, category_id: str, account_id: str = ...,
                              client_id: int = ..., name: str = ...,
                              domain: str = ...) -> VkObject: ...
        @staticmethod
        def updateTargetPixel(*, category_id: str, account_id: str = ...,
                              client_id: int = ..., target_pixel_id: str,
                              name: str = ..., domain: str = ...) -> VkObject: ...
        @staticmethod
        def deleteTargetPixel(*, account_id: str = ..., client_id: int = ...,
                              target_pixel_id: str) -> Literal[1]: ...
        @staticmethod
        def getTargetPixels(*, account_id: str = ..., client_id: int = ...)->ListOfVkObjects: ...
        @staticmethod
        def getLookalikeRequests(*, account_id: str = ..., client_id: int = ...,
                                 requests_ids: str = ..., offset: int = ...,
                                 limit: int = ...,
                                 sort_by: Literal["id", "update_time"] = ...) -> VkObject: ...
        @staticmethod
        def getMusicians(*, artist_name: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def getMusiciansByIds(*, ids: str) -> ListOfVkObjects: ...
        @staticmethod
        def createLookalikeRequest(*, account_id: str = ..., client_id: int = ...,
                                   source_type: str = ..., retargeting_group_id: int = ...,
                                   ) -> VkObject: ...
        @staticmethod
        def saveLookalikeRequestResult(*, account_id: str = ..., client_id: int = ...,
                                       request_id: str = ..., level:str = ...,
                                       ) -> VkObject: ...
        @staticmethod
        def getAdsPostsReach(*, account_id: str = ..., ads_ids: str = ...
                             ) -> ListOfVkObjects: ...        
    class appWidgets:
        @staticmethod
        def getAppImageUploadServer(*, image_type: Literal["24x24", "50x50", "160x160", "160x240", "510x128"] = ...
                                    ) -> dict[Literal["upload_url"], str]: ...
        @staticmethod
        def getAppImages(*, offset: int = ..., count: int = ...,
                         image_type: Literal["24x24", "50x50", "160x160", "160x240", "510x128"] = ...
                         ) -> ResponseOfItems: ...
        @staticmethod
        def getGroupImageUploadServer(*,
                                      image_type: Literal["24x24", "50x50", "160x160", "160x240", "510x128"] = ...
                                      ) -> dict[Literal["upload_url"], str]: ...
        @staticmethod
        def getGroupImages(*, offset: int = ..., count: int = ...,
                         image_type: Literal["24x24", "50x50", "160x160", "160x240", "510x128"] = ...
                         ) -> ResponseOfItems: ...
        @staticmethod
        def getImagesById(*, images: str = ...) -> VkObject: ...
        @staticmethod
        def saveAppImage(*, image: str = ...) -> VkObject: ...
        @staticmethod
        def saveGroupImage(*, hash: str = ..., image: str = ...) -> VkObject: ...
        @staticmethod
        def update(*, code: str, type: str) -> Literal[1]: ...
    class apps:
        @staticmethod
        def addUsersToTestingGroup(*, user_ids: str, group_id: int
                                   ) -> Literal[0, 1]: ...
        @staticmethod
        def deleteAppRequests() -> Literal[1]: ...
        @staticmethod
        def get(*, app_id: Positive = ..., app_ids: str = ...,
                platform: Literal["ios", "android", "winphone", "web"] = ...,
                extended: bool = ..., return_friends: bool = ...,
                fields: str = ..., name_case: NAME_CASE = ...) -> VkObject: ...
        @staticmethod
        def getCatalog(*,
                       sort: Literal["popular_today", "visitors", "create_date", "growth_rate", "popular_week"] = ...,
                       offset: Positive = ..., count: Positive,
                       platform: Literal["ios", "android", "winphone", "web", "html5"] = ...,
                       extended: bool = ..., return_friends: bool = ...,
                       fields: str = ..., name_case: NAME_CASE = ...,
                       q: str = ..., genre_id: Positive = ...,
                       filter: Literal["installed", "featured"] = ...
                       ) -> ResponseOfItems: ...
        @staticmethod
        def getFriendsList(*, extended: bool = ..., count: Positive = ...,
                           offset: Positive = ...,
                           type: Literal["invite", "request"] = ...,
                           fields: str = ...) -> ResponseOfItems: ...
        @staticmethod
        def getLeaderboard(*, type: Literal["level", "points", "score"], # TODO: global option
                           extended: bool = ...) -> ResponseOfItems: ...
        @staticmethod
        def getMiniAppPolicies(*, app_id: Positive
                               ) -> dict[Literal["privacy_policy", "terms"], str]: ...
        @staticmethod
        def getScopes(*, type: str = ...) -> ResponseOfItems: ...
        @staticmethod
        def getScore(*, user_id: Positive) -> int: ...
        @staticmethod
        def getTestingGroups(*, group_id: int = ...) -> ListOfVkObjects: ...
        @staticmethod
        def isNotificationsAllowed(*, user_id: Positive
                                   ) -> dict[Literal["is_allowed"], bool]: ...
        
        @staticmethod
        def promoHasActiveGift(*, promo_id: Positive,
                               user_id: Positive = ...) -> Literal[0, 1]: ...
        @staticmethod
        def promoUseGift(*, promo_id: Positive, user_id: Positive = ...
                         ) -> Literal[0, 1]: ...
        @staticmethod
        def removeTestingGroup(*, group_id: int) -> Literal[1]: ...
        @staticmethod
        def removeUsersFromTestingGroups(*, user_ids: str) -> Literal[1]: ...
        @staticmethod
        def sendRequest(*, user_id: Positive,
                        type: Literal["invite", "request"] = ...,
                        name: str = ..., key: str = ...,
                        separate: bool = ...) -> int: ...
        @staticmethod
        def updateMetaForTestingGroup(*, group_id: int, webview: str,
                                      name: str, platforms: str,
                                      user_ids: str = ...
                                      ) -> dict[Literal["group_id"], int]: ...
    class auth:
        @staticmethod
        def checkPhone(*, phone: str, client_id: int = ...,
                       client_secret: str = ...,
                       auth_by_phone: bool = ...) -> Literal[1]: ...

        @staticmethod
        def restore(*, phone: str, last_name: str) -> VkObject: ...
    class board:
        @staticmethod
        def addTopic(*, group_id: Positive, title: str, text: str = ...,
                     from_group: bool = ..., attachments: str = ...) -> int: ...
        @staticmethod
        def closeTopic(*, group_id: Positive, topic_id: Positive) -> Literal[1]: ...
        @staticmethod
        def createComment(*, group_id: Positive, topic_id: Positive,
                          message: str = ..., attachments: str = ...,
                          from_group: bool = ..., sticker_id: Positive= ...,
                          guid: str = ...)->int: ...
        @staticmethod
        def deleteComment(*, group_id: Positive, topic_id: Positive,
                          commnet_id: Positive) -> Literal[1]: ...
        @staticmethod
        def deleteTopic(*, group_id: Positive, topic_id: Positive) -> Literal[1]: ...
        @staticmethod
        def editComment(*, group_id: Positive, topic_id: Positive,
                        comment_id: Positive,
                        message: str = ..., attachments: str = ...) -> Literal[1]: ...
        @staticmethod
        def editTopic(*, group_id: Positive, topic_id: Positive, title: str) -> Literal[1]: ...
        @staticmethod
        def fixTopic(*, group_id: Positive, topic_id: Positive) -> Literal[1]: ...
        @staticmethod
        def getComments(*, group_id: Positive, topic_id: Positive, need_likes: bool = ...,
                        start_comment_id: Positive = ..., offset: int = ...,
                        count: Positive = ..., extended: bool = ...,
                        sort: Literal["asc", "desc"] = ...
                        ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getTopics(*, group_id: Positive, topic_ids: str = ...,
                      order: int = ..., offset: Positive = ...,
                      count: Positive = ..., extended: bool = ...,
                      preview: int = ..., preview_length: Positive = ...
                      ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def openTopic(*, group_id: Positive, topic_id: Positive) -> Literal[1]: ...
        @staticmethod
        def restoreComment(*, group_id: Positive, topic_id: Positive,
                           comment_id: Positive) -> Literal[1]: ...
        @staticmethod
        def unfixTopic(*, group_id: Positive, topic_id: Positive) -> Literal[1]: ...
    class calls:
        @staticmethod
        def start(*, group_id: int = ...) -> VkObject: ...
        @staticmethod
        def forceFinish(*, call_id: str) -> Literal[1]: ...
    class database:
        @staticmethod
        def getChairs(*, faculty_id: Positive, offset: Positive = ...,
                      count: Positive = ...) -> ResponseOfItems: ...
        @staticmethod
        def getCities(*, country_id: Positive, region_id: Positive = ...,
                      q: str = ..., need_all: bool = ...,
                      offset: Positive = ..., count: Positive = ...
                      ) -> ResponseOfItems: ...
        @staticmethod
        def getCitiesById(*, city_ids: str = ...
                          ) -> ListOfVkObjects: ...
        @staticmethod
        def getCountries(*, need_all: bool = ..., code: str = ...,
                         offset: Positive = ..., count: Positive = ...
                         ) -> ResponseOfItems: ...
        @staticmethod
        def getCountriesById(*, country_ids: str = ...
                             ) -> ListOfVkObjects: ...
        @staticmethod
        def getFaculties(*, university_id: Positive, offset: Positive = ...,
                         count: Positive = ...) -> ResponseOfItems: ...
        @staticmethod
        def getMetroStations(*, city_id: Positive, offset: Positive = ...,
                             count: Positive = ..., extended: bool = ...
                             )->ResponseOfItems: ...
        @staticmethod
        def getMetroStationsById(*, station_ids: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def getRegions(*, county_id: Positive, q: str = ...,
                       offset: Positive = ..., count: Positive = ...
                       ) -> ResponseOfItems: ...
        @staticmethod
        def getSchoolClasses(*, country_id: Positive) -> list[list[int|str]]: ...
        @staticmethod
        def getSchools(*, q: str = ..., city_id: Positive,
                       offset: Positive = ..., count: Positive = ...
                       ) -> ResponseOfItems: ...
        @staticmethod
        def getUniversities(*, q: str = ..., country_id: Positive = ...,
                            city_id: Positive = ..., offset: Positive = ...,
                            count: Positive = ...) -> ResponseOfItems: ...
    class docs:
        @staticmethod
        def add(*, owner_id: int, doc_id: Positive, access_key: str = ...) -> int: ...
        @staticmethod
        def delete(*, owner_id: int, doc_id: Positive) -> Literal[1]: ...
        @staticmethod
        def edit(*, owner_id: int, doc_id: Positive,
                 title: str = ..., tags: str = ...) -> Literal[1]: ...
        @staticmethod
        def get(*, count: Positive = ..., offset: Positive = ...,
                type: Positive = ..., owner_id: int = ...,
                return_tags: bool = ...) -> ResponseOfItems: ...
        @staticmethod
        def getById(*, docs: str = ..., return_tags: bool = ...
                    ) -> ListOfVkObjects: ...
        @staticmethod
        def getMessagesUploadServer(*,
                                    type: Literal["doc", "audio_message"] = ...,
                                    peer_id: int = ...
                                    ) -> dict[Literal["upload_url"], str]: ...
        @staticmethod
        def getTypes(*, owner_id: int) -> ResponseOfItems: ...
        @staticmethod
        def getUploadServer(*, group_id: Positive = ...
                            ) -> dict[Literal["upload_url"], str]: ...
        @staticmethod
        def getWallUploadServer(*, group_id: Positive = ...
                                ) -> dict[Literal["upload_url"], str]: ...
        @staticmethod
        def save(*, file: str, title: str = ..., tags: str = ...,
                 return_tags: bool = ...) -> ListOfVkObjects: ...
        @staticmethod
        def search(*, q: str = ..., search_own: bool = ...,
                   count: Positive = ..., offset: Positive = ...,
                   return_tags: bool = ...) -> ResponseOfItems: ...
    class donut:
        @staticmethod
        def getFriends(* owner_id: int, offset: Positive = ...,
                       count: Positive = ..., fields: str = ...
                       ) -> ResponseOfItems: ...
        @staticmethod
        def getSubscription(*, owner_id: int) ->VkObject: ...
        @staticmethod
        def getSubscriptions(*, fields: str = ..., offset: Positive = ...,
                             count: Positive = ...) -> VkObject: ...
        @staticmethod
        def isDon(*, owner_id: int) -> Literal[0, 1]: ...
    class downloadedGames:
        @staticmethod
        def getPaidStatus(*, user_id: Positive = ...
                          ) -> dict[Literal["is_paid"], bool]: ...
    class fave:
        @staticmethod
        def addArticle(*, url: str) -> Literal[1]: ...
        @staticmethod
        def addLink(*, link: str) -> Literal[1]: ...
        @staticmethod
        def addPage(*, user_id: Positive = ...,
                    group_id: Positive = ...)->Literal[1]: ...
        @staticmethod
        def addPost(*, owner_id: int, id: int, access_key: str = ...,
                    ref: str = ..., track_code: str = ...,
                    source: str = ...) -> Literal[1]: ...
        @staticmethod
        def addProduct(*, owner_id: int, id: int,
                       access_key: str = ...) -> Literal[1]: ...
        @staticmethod
        def addTag(*, name: str = ...,
                   position: Literal["front", "back"] = ...) -> VkObject: ...
        @staticmethod
        def addVideo(*, owner_id: int, id: int, access_key: str = ...
                     ) -> Literal[1]: ...
        @staticmethod
        def editTag(*, id: int, name: str) -> Literal[1]: ...
        @staticmethod
        def get(*, extended: bool = ...,
                item_type: Literal["post", "video", "product", "article",
                                   "link"] = ...,
                tag_id: int = ..., offset: Positive = ..., count: Positive = ...,
                fields: str = ..., is_from_snackbar: bool = ...
                ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getPages(*, offset: Positive = ..., count: Positive = ...,
                     type: Literal["users", "groups", "hints"] = ...,
                     fields: str = ..., tag_id: int = ...
                     ) -> ResponseOfItems: ...
        @staticmethod
        def getTags() -> ResponseOfItems: ...
        @staticmethod
        def markSeen() -> Literal[1]: ...
        @staticmethod
        def removeArticle(*, owner_id: int, article_id: Positive,
                          ref: str = ...) -> Literal[1]: ...
        @staticmethod
        def removeLink(*, link_id: str = ...) -> Literal[1]: ...
        @staticmethod
        def removePage(*, user_id: int = ..., group_id: int = ...) -> Literal[1]: ...
        @staticmethod
        def removePost(*, owner_id: int, id: int) -> Literal[1]: ...
        @staticmethod
        def removeProduct(*, owner_id: int, id: int) -> Literal[1]: ...
        @staticmethod
        def removeTag(*, id: int) -> Literal[1]: ...
        @staticmethod
        def removeVideo(*, owner_id: int, id: int) -> Literal[1]: ...
        @staticmethod
        def reorderTags(*, ids: str) -> Literal[1]: ...
        @staticmethod
        def setPageTags(*, user_id: Positive = ...,
                        group_id: Positive = ...,
                        tag_ids: str = ...) -> Literal[1]: ...
        @staticmethod
        def setTags(*, item_type: Literal["post", "video", "product",
                                          "article", "link"] = ...,
                    item_owner_id: int = ..., item_id: int = ...,
                    tag_ids: str = ..., link_id: str = ...,
                    link_url: str = ...) -> Literal[1]: ...
        @staticmethod
        def trackPageInteraction(*, user_id: Positive = ...,
                                 group_id: Positive = ...) -> Literal[1]: ...
    class friends:
        @staticmethod
        def add(*, user_id: Positive = ..., text: str = ...,
                follow: bool = ...) -> Literal[1, 2, 4]: ...
        @staticmethod
        def addList(*, name: str, user_ids: str = ...
                    ) -> dict[Literal["list_id"], int]: ...
        @staticmethod
        def areFriends(*, user_ids: str, need_sign: bool = ...,
                       extended: bool = ...) -> ListOfVkObjects: ...
        @staticmethod
        def delete(*, user_id: Positive = ...) -> VkObject: ...
        @staticmethod
        def deleteAllRequests() -> Literal[1]: ...
        @staticmethod
        def deleteList(*, list_id: Positive) -> Literal[1]: ...
        @staticmethod
        def edit(*, user_id: Positive, list_ids: str = ...) -> Literal[1]: ...
        @staticmethod
        def editList(*, name: str = ..., list_id: Positive,
                     user_ids: str = ..., add_user_ids: str = ...,
                     delete_user_ids: str = ...) -> Literal[1]: ...
        @staticmethod
        def get(*, user_id: int = ...,
                order: Literal["hints", "random", "name"] = ...,
                list_id: Positive = ..., count: Positive = ...,
                offset: Positive = ..., fields: str = ...,
                name_case: NAME_CASE = ..., ref: str = ...,
                ) -> ResponseOfItems: ...
        @staticmethod
        def getAppUsers() -> list[int]: ...
        @staticmethod
        def getAvailableForCall(*, fields: str = ...,
                                name_case: NAME_CASE = ...) -> ResponseOfItems: ...
        @staticmethod
        def getByPhones(*, phones: str = ..., fields: str = ...
                        ) -> ListOfVkObjects: ...
        @staticmethod
        def getLists(*, user_id: Positive = ...,
                     return_system: bool = ...) -> ResponseOfItems: ...
        @staticmethod
        def getMutual(*, source_uid: Positive = ...,
                      target_uid: Positive = ...,
                      target_uids: str = ...,
                      order: str = ...,
                      count: Positive = ...,
                      offset: Positive = ...) -> list[list[int]]: ...
        @staticmethod
        def getOnline(*, user_id: Positive = ..., list_id: Positive = ...,
                      online_mobile: bool = ..., order: str = ...,
                      count: Positive = ..., offset: Positive = ...
                      ) -> VkObject: ...
        @staticmethod
        def getRecent(*, count:Positive = ...) -> list[int]: ...
        @staticmethod
        def getRequests(*, offset: Positive = ..., count: Positive = ...,
                        extended: bool = ..., need_mutual: bool = ...,
                        out: bool = ..., sort: Positive = ...,
                        need_viewed: bool = ..., suggested: bool = ...,
                        ref: str = ..., fields: str = ...
                        ) -> ResponseOfItems: ...
        @staticmethod
        def getSuggestions(*, filter: str = ..., count: Positive = ...,
                           offset: Positive = ...,fields: str = ...,
                           name_case: NAME_CASE = ...): ResponseOfItems: ...
        @staticmethod
        def search(*, user_id: Positive, q: str = ..., fields: str = ...,
                   name_case: NAME_CASE = ..., offse: Positive = ...,
                   count: Positive = ...) -> ResponseOfItems: ...
    class gifts:
        @staticmethod
        def get(*, user_id: Positive = ..., count: Positive = ...,
                offset: Positive = ...) -> ResponseOfItems: ...
    class groups:
        @staticmethod
        def addAddress(*, group_id: Positive, title: str,
                       adress: str, additional_address: str = ...,
                       country_id: Positive, city_id: Positive,
                       metro_id: Positive = ..., latitude: str,
                       longitude: str, phone: str = ...,
                       work_info_status: Literal["no_information",
                                                 "temporarily_closed",
                                                 "always_opened",
                                                 "forever_closed",
                                                 "timetable"] = ...,
                       timetable: Text = ..., is_main_address: bool = ...
                       ) -> VkObject: ...
        @staticmethod
        def addCallbackServer(*, group_id: Positive, url: str,
                              title: str, secret_key: str
                              ) -> dict[Literal["server_id"], int]: ...
        @staticmethod
        def addLink(*, group_id: Positive, link: str, text: str = ...
                    ) -> VkObject: ...
        @staticmethod
        def approveRequest(*, group_id: Positive, user_id: Positive
                           ) -> Literal[1]: ...
        @staticmethod
        def ban(*, group_id: Positive, owner_id: int = ...,
                end_date: Positive = ..., reason: Positive = ...,
                comment: str = ...,
                comment_visible: bool = ...) -> Literal[1]: ...
        @staticmethod
        def create(*, title: str, description: str = ...,
                   type: Literal["group", "event", "public"] = ...,
                   public_category: Positive = ...,
                   public_subcategory: Positive = ...,
                   subtype: Positive = ...) -> VkObject: ...
        @staticmethod
        def deleteAddress(*, group_id: Positive, adress_id: Positive
                          ) -> Literal[1]: ...
        @staticmethod
        def deleteCallbackServer(*, group_id: Positive, server_id: Positive
                                 ) -> Literal[1]: ... 
        @staticmethod
        def deleteLink(*, group_id: Positive, link_id: Positive
                       ) -> Literal[1]: ...
        @staticmethod
        def disableOnline(*, group_id: Positive) -> Literal[1]: ...
        @staticmethod
        def edit(*, group_id: int, title: str = ..., description: str = ...,
                 screen_name: str = ..., access: Positive = ...,
                 website: str = ..., subject: str = ...,
                 email: str = ..., phone: str = ..., rss: str = ...,
                 event_start_date: bool = ..., event_finish_date: bool = ...,
                 event_group_id: int = ..., public_category: Positive = ...,
                 public_subcategory: Positive = ..., public_date: str = ...,
                 wall: Positive = ..., topics: Positive = ...,
                 photos: Positive = ..., video: Positive = ...,
                 audio: Positive = ...,links: bool = ...,
                 events: bool = ..., places: bool = ...,
                 contacts: bool = ..., docs: Positive = ...,
                 wiki: Positive = ..., messages: bool = ...,
                 articles: bool = ..., addresses: bool = ...,
                 age_limits: Positive = ..., market: bool = ...,
                 market_buttons: str = ..., market_comments: bool = ...,
                 market_country: str = ..., market_city: str = ...,
                 market_currency: Positive = ..., market_contact: Positive = ...,
                 market_wiki: Positive = ..., obscene_filter: bool = ...,
                 obscene_stopwords: bool = ..., obscene_words: str = ...,
                 main_section: Positive = ..., secondary_section: Positive = ...,
                 country: Positive = ..., city: Positive = ...
                 ) -> Literal[1]: ...
        @staticmethod
        def editAddress(*, group_id: Positive, address_id: Positive,
                        title: str = ..., address: str = ...,
                        additional_address: str = ..., country_id: Positive = ...,
                        city_id: Positive = ..., metro_id: Positive = ...,
                        latitude: str = ..., longitude: str = ...,
                        phone: str = ...,
                        work_info_status: Literal["no_information",
                                                  "temporarily_closed",
                                                  "always_opened",
                                                  "forever_closed",
                                                  "timetable"] = ...,
                        timetable: Text = ..., is_main_address: bool = ...
                        ) -> VkObject: ...
        @staticmethod
        def editCallbackServer(*, group_id: Positive,
                               server_id: Positive, url: str,
                               title: str, secret_key: str = ...
                               ) -> Literal[1]: ...
        @staticmethod
        def editLink(*, group_id: Positive, link_id: Positive,
                     text: str = ...) -> Literal[1]: ...
        @staticmethod
        def editManager(*, group_id: Positive, user_id: Positive,
                        role: Literal["moderator", "editor",
                                      "administrator",
                                      "advertiser"] = ...,
                        is_contact: bool = ...,
                        contact_position: str = ...,
                        contact_phone: str = ...,
                        contact_email: str = ...) -> Literal[1]: ...
        @staticmethod
        def editPlace(*, group_id: Positive, title: str = ...,
                      address: str = ..., country_id: Positive = ...,
                      city_id: Positive = ..., latitude: str = ...,
                      longitude: str = ...) -> VkObject: ...
        @staticmethod
        def enableOnline(*, group_id: Positive) -> Literal[1]: ...
        @staticmethod
        def get(*, user_id: int = ..., extended: bool = ...,
                filter: str = ..., fields: str = ..., offset: Positive = ...,
                count: Positive = ...) -> ResponseOfItems: ...
        @staticmethod
        def getAddresses(*, group_id: Positive, address_ids: str = ...,
                         latitude: str = ...,longitude:str = ...,
                         offset: Positive = ..., count: Positive = ...,
                         fields: str = ...) -> ResponseOfItems: ...
        @staticmethod
        def getBanned(*, group_id: Positive, offset: Positive = ...,
                      count: Positive = ..., fields: str = ...,
                      owner_id: int = ...) -> ResponseOfItems: ...
        @staticmethod
        def getById(*, group_ids: str = ..., group_id: str = ...,
                    fields: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def getCallbackConfirmationCode(*, group_id: Positive) -> str: ...
        @staticmethod
        def getCallbackServerSettings(*, group_id: Positive) -> VkObject: ...
        @staticmethod
        def getCallbackServers(*, group_id: Positive, server_ids: str = ...
                               ) -> ResponseOfItems: ...
        @staticmethod
        def getCallbackSettings(*, group_id: Positive, server_id: Positive = ...,
                                ) -> VkObject: ...
        @staticmethod
        def getCatalog(*, category_id: Positive = ...,
                       subcategory_id: Positive = ...) -> ResponseOfItems: ...
        @staticmethod
        def getCatalogInfo(*, extended: bool, subcategories: bool
                           ) -> VkObject: ...
        @staticmethod
        def getInvitedUsers(*, group_id: Positive, offset: Positive = ...,
                            count: Positive = ..., fields: str = ...,
                            name_case: NAME_CASE = ...
                            ) -> ResponseOfItems: ...
        @staticmethod
        def getInvites(*, offset: Positive = ..., count: Positive = ...,
                       extende: bool = ...) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getLongPollServer(*, group_id: Positive) -> VkObject: ...
        @staticmethod
        def getLongPollSettings(*, group_id: Positive
                                ) -> VkObject: ...
        @staticmethod
        def getMembers(*, group_id: str = ...,
                       sort: Literal["id_asc", "id_desc",
                                     "time_asc", "time_desc"] = ...,
                       offset: Positive = ..., count: Positive = ...,
                       fields: str = ...,
                       filter: Literal["friends", "unsure",
                                       "managers", "donus"] = ...
                       ) -> ResponseOfItems: ...
        @staticmethod
        def getOnlineStatus(*, group_id: Positive) -> VkObject: ...
        @staticmethod
        def getRequests(*, group_id: Positive, offset: Positive = ...,
                        count: Positive = ..., fields: str = ...,
                        ) -> ResponseOfItems: ...
        @staticmethod
        def getSettings(*, group_id: Positive) -> VkObject: ...
        @staticmethod
        def getTagList(*, group_id: Positive) -> ListOfVkObjects: ...
        @staticmethod
        def getTokenPermissions() -> VkObject: ...
        @staticmethod
        def invite(*, group_id: Positive, user_id: Positive
                   ) -> Literal[1] : ...
        @staticmethod
        def isMember(*, group_id: Positive, user_id: Positive = ...,
                     user_ids: str = ..., extended: bool = ...,
                     ) -> dict[Literal["member", "can_invite"], int]: ...
        @staticmethod
        def join(*, group_id: Positive = ..., not_sure: str = ...,
                 ) -> Literal[1]: ...
        @staticmethod
        def leave(*, group_id: Positive) -> Literal[1]: ...
        @staticmethod
        def removeUser(*, group_id: Positive, user_od: Positive
                       ) -> Literal[1]: ...
        @staticmethod
        def reorderLink(*, group_id: Positive, link_id: Positive,
                        after: Positive = ...) -> Literal[1]: ...
        @staticmethod
        def search(*, q: str, type: Literal["group", "page", "event"] = ...,
                   country_id: Positive = ..., city_id: Positive = ...,
                   future: bool =..., market: bool = ..., sort: int = ...,
                   offset: Positive = ..., count: Positive = ...,
                   )-> ResponseOfItems: ...
        @staticmethod
        def setCallbackSettings(*, group_id: Positive,
                                server_id: Positive = ...,
                                api_version: str = ...,
                                message_new: bool = ...,
                                message_reply: bool = ...,
                                message_allow: bool = ...,
                                message_edit: bool = ...,
                                message_deny: bool = ...,
                                message_typing_state: bool = ...,
                                photo_new: bool = ...,
                                audio_new: bool = ...,
                                video_new: bool = ...,
                                wall_reply_new: bool = ...,
                                wall_reply_edit: bool = ...,
                                wall_reply_delete: bool = ...,
                                wall_reply_restore: bool = ...,
                                wall_post_new: bool = ...,
                                wall_repost: bool = ...,
                                board_post_new: bool = ...,
                                board_post_edit: bool = ...,
                                board_post_restore: bool = ...,
                                board_post_delete: bool = ...,
                                photo_comment_new: bool = ...,
                                photo_comment_edit: bool = ...,
                                photo_comment_delete: bool = ...,
                                photo_comment_restore: bool = ...,
                                video_comment_new: bool = ...,
                                video_comment_edit: bool = ...,
                                video_comment_delete: bool = ...,
                                video_comment_restore: bool = ...,
                                market_comment_new: bool = ...,
                                market_comment_edit: bool = ...,
                                market_comment_delete: bool = ...,
                                market_comment_restore: bool = ...,
                                market_order_new: bool = ...,
                                market_order_edit: bool = ...,
                                poll_vote_new: bool = ...,
                                group_join: bool = ...,
                                group_leave: bool = ...,
                                group_change_settings: bool = ...,
                                group_change_photo: bool = ...,
                                group_officers_edit: bool = ...,
                                user_block: bool = ...,
                                user_unblock: bool = ...,
                                lead_forms_new: bool = ...,
                                like_add: bool = ...,
                                like_remove: bool = ...,
                                message_event: bool = ...,
                                donut_subscription_create: bool = ...,
                                donut_subscription_prolonged: bool = ...,
                                donut_subscription_cancelled: bool = ...,
                                donut_subscription_price_changed: bool = ...,
                                donut_subscription_expired: bool = ...,
                                donut_money_withdraw: bool = ...,
                                donut_money_withdraw_error: bool = ...
                                ) -> Literal[1]: ...
        @staticmethod
        def setLongPollSettings(*, group_id: Positive, enabled: bool = ...,
                                api_version: str = ...,
                                message_new: bool = ...,
                                message_reply: bool = ...,
                                message_allow: bool = ...,
                                message_edit: bool = ...,
                                message_deny: bool = ...,
                                message_typing_state: bool = ...,
                                photo_new: bool = ...,
                                audio_new: bool = ...,
                                video_new: bool = ...,
                                wall_reply_new: bool = ...,
                                wall_reply_edit: bool = ...,
                                wall_reply_delete: bool = ...,
                                wall_reply_restore: bool = ...,
                                wall_post_new: bool = ...,
                                wall_repost: bool = ...,
                                board_post_new: bool = ...,
                                board_post_edit: bool = ...,
                                board_post_restore: bool = ...,
                                board_post_delete: bool = ...,
                                photo_comment_new: bool = ...,
                                photo_comment_edit: bool = ...,
                                photo_comment_delete: bool = ...,
                                photo_comment_restore: bool = ...,
                                video_comment_new: bool = ...,
                                video_comment_edit: bool = ...,
                                video_comment_delete: bool = ...,
                                video_comment_restore: bool = ...,
                                market_comment_new: bool = ...,
                                market_comment_edit: bool = ...,
                                market_comment_delete: bool = ...,
                                market_comment_restore: bool = ...,
                                market_order_new: bool = ...,
                                market_order_edit: bool = ...,
                                poll_vote_new: bool = ...,
                                group_join: bool = ...,
                                group_leave: bool = ...,
                                group_change_settings: bool = ...,
                                group_change_photo: bool = ...,
                                group_officers_edit: bool = ...,
                                user_block: bool = ...,
                                user_unblock: bool = ...,
                                lead_forms_new: bool = ...,
                                like_add: bool = ...,
                                like_remove: bool = ...,
                                message_event: bool = ...,
                                donut_subscription_create: bool = ...,
                                donut_subscription_prolonged: bool = ...,
                                donut_subscription_cancelled: bool = ...,
                                donut_subscription_price_changed: bool = ...,
                                donut_subscription_expired: bool = ...,
                                donut_money_withdraw: bool = ...,
                                donut_money_withdraw_error: bool = ...
                                ) -> Literal[1]: ...
        @staticmethod
        def setSettings(*, group_id: Positive, messages: bool = ...,
                        bots_capabilities: bool = ...,
                        bots_start_button: bool = ...,
                        bots_add_to_chat: bool = ...) -> Literal[1]: ...
        @staticmethod
        def setUserNote(*, group_id: Positive, user_id: Positive,
                        note: str = ...) -> Any: ...
        @staticmethod
        def tagAdd(*, group_id: Positive, tag_name: str,
                   tag_color: str = ...) -> Any: ...
        @staticmethod
        def tagBind(*, group_id: Positive, tag_id: Positive,
                    user_id: Positive, act: Literal["bind", "unbind"]
                    ) -> Any: ...
        @staticmethod
        def tagDelete(*, group_id: Positive, tag_id: Positive
                      ) -> Any: ...
        @staticmethod
        def tagUpdate(*, group_id: Positive, tag_id: Positive,
                      tag_name: str) -> Any: ...
        @staticmethod
        def toggleMarket(*, group_id: Positive, state: Literal["none", "basic", "advanced"],
                         ref: str = ..., utm_source: str = ...,
                         utm_medium: str = ..., utm_campaign: str = ...,
                         utm_content: str = ..., utm_term: str = ...,
                         promocode: str = ...) -> Any: ...
        @staticmethod
        def unban(*, group_id: Positive, owner_id: int = ...
                  ) -> Literal[1]: ...
    class leadForms:
        @staticmethod
        def create(*, group_id: str, name: str, title: str, description: str,
                   questions: Text, policy_link_url: str, photo: str = ...,
                   confirmation: str = ..., site_link_url: str = ...,
                   active: bool = ..., once_per_user: bool = ...,
                   pixel_code: str = ..., notify_admins: str = ...,
                   notify_emails: str = ...) -> VkObject: ...
        @staticmethod
        def delete(*, group_id: str, form_id: str) -> int: ...
        @staticmethod
        def get(*, group_id: str, form_id: str) -> VkObject: ...
        @staticmethod
        def getLeads(*, group_id: str, form_id: str, limin: Positive = ...,
                     next_page_token: str = ...) -> ListOfVkObjects: ...
        @staticmethod
        def getUploadURL() -> str: ...
        @staticmethod
        def list(*, group_id: str) -> ListOfVkObjects: ...
        @staticmethod
        def update(*, group_id: str, form_id: str, name: str, title: str,
                   description: str, questions: Text, policy_link_url: str,
                   photo: str = ..., confirmation: str = ...,
                   site_link_url: str = ..., active: bool = ...,
                   once_per_user: bool = ..., pixel_code: str = ...,
                   notify_admins: str = ..., notify_emails: str = ...
                   ) -> VkObject: ...
    class likes:
        @staticmethod
        def add(*, type: Literal["post", "comment", "photo", "audio",
                                 "video", "note", "market", "photo_comment",
                                 "video_comment", "topic_comment", "market_comment"],
                owner_id: int = ..., item_id: Positive = ..., access_key: str = ...,
                action: str = ...) -> dict[Literal["likes"], int]: ...
        @staticmethod
        def delete(*, type: Literal["post", "comment", "photo", "audio",
                                    "video", "note", "market", "photo_comment",
                                    "video_comment", "topic_comment",
                                    "market_comment", "sitepage"],
                   owner_id: int = ..., item_id: Positive = ...,
                   access_key: str = ...) -> dict[Literal["likes"], int]: ...
        @staticmethod
        def getList(*, type: Literal["post", "comment", "photo", "audio",
                                     "video", "note", "market", "photo_comment",
                                     "video_comment", "topic_comment",
                                     "market_comment", "sitepage"],
                    owner_id: int = ..., item_id: int = ..., page_url: str = ...,
                    filter: Literal["likes", "copies"] = ...,
                    friends_only: int = ..., extended: bool = ...,
                    offset: Positive = ..., count: Positive = ...,
                    skip_own: bool = ...) -> ExtendedResponseOfItems: ...
        @staticmethod
        def isLiked(*, user_id: Positive = ...,
                    type: Literal["post", "comment", "photo", "audio",
                                  "video", "note", "market", "photo_comment",
                                  "video_comment", "topic_comment"],
                    owner_id: int = ..., item_id: Positive) -> VkObject: ...
    class market:
        @staticmethod
        def add(*, owner_id: int, name: str, description: str,
                category_id: Positive = ..., price: str = ...,
                old_price: str = ..., deleted: bool = ...,
                main_photo_id: Positive = ..., photo_ids: str = ...,
                url: str = ..., dimension_width: Positive = ...,
                dimension_height: Positive = ...,
                dimension_length: Positive = ..., weight: Positive = ...,
                sku: str = ...) -> int: ...
        @staticmethod
        def addAlbum(*, owner_id: int, title: str, photo_id: Positive = ...,
                    main_album: bool = ..., is_hidden: bool = ...
                    ) -> dict[Literal["market_album_id"], int]: ...
        @staticmethod
        def addToAlbum(*, owner_id: int, item_id: Positive = ...,
                       item_ids: str = ..., album_ids: str = ...
                       ) -> Literal[1]: ...
        @staticmethod
        def createComment(*, owner_id: int, item_id: Positive, message: str = ...,
                          attachments: str = ..., from_group: bool = ...,
                          reply_to_comment: Positive = ...,
                          sticker_id: Positive = ..., guid: str = ...
                          ) -> Literal[1]: ...
        @staticmethod
        def delete(*, owner_id: int, item_id: Positive
                   ) -> Literal[1]: ...
        @staticmethod
        def deleteAlbum(*, owner_id: int, album_id: Positive
                        ) -> Literal[1]: ...
        @staticmethod
        def deleteComment(*, owner_id: int, comment_id: Positive
                          ) -> Literal[0, 1]: ...
        @staticmethod
        def edit(*, owner_id: int, item_id: Positive, name: str =  ...,
                 description: str = ..., category_id: Positive = ...,
                 price: str = ..., old_price: str = ..., deleted: bool = ...,
                 main_photo_id: Positive = ..., photo_ids: str = ...,
                 url: str = ..., dimension_width: Positive = ...,
                 dimension_height: Positive = ..., dimension_length: Positive = ...,
                 weight: Positive = ..., sku: str = ...
                 ) -> Literal[1]: ...
        @staticmethod
        def editAlbum(*, owner_id: int, album_id: Positive, title: str,
                      photo_id: Positive = ..., main_album : bool = ...,
                      is_hidden: bool = ...
                      ) -> Literal[1]: ...
        @staticmethod
        def editComment(*, owner_id: int, comment_id: Positive,
                        message: str = ..., attachments: str = ...
                        ) -> Literal[1]: ...
        @staticmethod
        def editOrder(*, user_id: int, order_id: Positive,
                      merchant_comment: str = ..., status: Positive = ...,
                      track_number: str = ...,
                      payment_status: Literal["not_paid", "paid", "returned"] = ...,
                      delivery_price: Positive = ..., width: Positive = ...,
                      length: Positive = ..., height: Positive = ...,
                      weight: Positive = ..., comment_for_user: str = ...,
                      receipt_link: str = ...
                      ) -> Literal[1]: ...
        @staticmethod
        def get(*, owner_id: int, album_id: str = ..., count: Positive = ...,
                offset: Positive = ..., extended: bool = ..., date_from: str = ...,
                date_to: str = ..., need_variants: bool = ...,
                with_disabled: bool = ...) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getAlbumById(*, owner_id: int, album_ids: str, 
                         need_all_item_ids: bool = ...,
                         ) -> ResponseOfItems: ...
        @staticmethod
        def getAlbums(*, owner_id: int, offset: Positive = ...,
                      count: Positive = ...
                      ) -> ResponseOfItems: ...
        @staticmethod
        def getById(*, item_ids: str, extended: bool = ...
                    ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getCategories(*, count: Positive = ..., offset: Positive = ...
                          ) -> ResponseOfItems: ...
        @staticmethod
        def getComments(*, owner_id: int, item_id: Positive, need_likes: bool = ...,
                        start_comment_id: Positive = ..., offset: Positive = ...,
                        count: Positive = ...,
                        sort: Literal["asc", "desc"] = ..., 
                        extended: bool = ..., fields: str = ...
                        ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getGroupOrders(*, group_id: int, offset: Positive = ...,
                           count: Positive = ...
                           ) -> VkObject: ...
        @staticmethod
        def getOrderById(*, user_id: Positive = ..., order_id: Positive,
                         extended: bool = ...
                         ) -> VkObject: ...
        @staticmethod
        def getOrderItems(*, user_id: Positive = ..., order_id: Positive,
                         offset: Positive = ..., count: Positive = ...
                         ) -> ResponseOfItems: ...
        @staticmethod
        def getOrders(*, offset: Positive = ..., count: Positive = ...,
                      extended: bool = ..., date_from: str = ...,
                      date_to: str = ...) -> ExtendedResponseOfItems: ...
        @staticmethod
        def removeFromAlbum(*, owner_id: int, item_id: Positive,
                            album_ids: str) -> Literal[1]: ...
        @staticmethod
        def reorderAlbums(*, owner_id: int, album_id: int,
                          before: Positive = ..., after: Positive = ...
                          ) -> Literal[1]: ...
        @staticmethod
        def reorderItems(*, owner_id: int, album_id: int = ...,
                         item_id: Positive, before: Positive = ...,
                         after: Positive = ...
                         ) -> Literal[1]: ...
        @staticmethod
        def report(*, owner_id: int, item_id: Positive,
                   reason: Positive) -> Literal[1]: ...
        @staticmethod
        def reportComment(*, owner_id: int, comment_id: Positive,
                          reason: Positive = ...
                          ) -> Literal[1]: ...
        @staticmethod
        def restore(*, owner_id: int, item_id: Positive
                    ) -> Literal[1, 0]: ...
        @staticmethod
        def restoreComment(*, owner_id: int, comment_id: Positive
                           ) -> Literal[1, 0]: ...
        @staticmethod
        def search(*, owner_id: int, album_id: Positive = ...,
                   q: str = ..., price_from: Positive = ...,
                   price_to: Positive = ..., sort: int = ...,
                   rev: Positive = ..., offset: Positive = ...,
                   count: Positive = ..., extended: bool = ...,
                   status: str = ..., need_variants: bool = ...
                   ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def searchItems(*, q: str, offset: int = ..., count: Positive = ...,
                        category_id: Positive = ..., price_from: Positive = ...,
                        price_to: Positive = ..., sort_by: int = ...,
                        sort_direction: int = ..., country: Positive = ...,
                        city: Positive = ...) -> ResponseOfItems: ...
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
                   peer_id: int = ..., cmids:str = ...
                   )->dict[str, Literal[0, 1]]: ...
        @staticmethod
        def deleteChatPhoto(*, chat_id: Positive, group_id:Positive = ...
                            )->VkObject: ...
        @staticmethod
        def deleteConversation(*, user_id: str = ..., peer_id: int = ...,
                               offset: Positive = ..., count: Positive = ...,
                               group_id: Positive = ...
                               )->dict[Literal["last_deleted_id"], int]: ...
        @staticmethod
        def denyMessagesFromGroup(*, group_id: Positive) -> Literal[1]: ...
        @staticmethod
        def edit(*, peer_id: int, message: str = ..., lat: str = ...,
                 long: str = ..., attachment: str = ...,
                 keep_forward_messages: bool = ..., keep_snippets: bool = ...,
                 group_id: int = ..., dont_parse_links: bool = ...,
                 disable_mentions: bool = ..., message_id: str = ...,
                 conversation_message_id: str = ...,
                 template: Text = ..., keyboard: Text = ...) -> Literal[1]: ...
        @staticmethod
        def editChat(*, chat_id: Positive, title: str = ...) -> Literal[1]: ...
        @staticmethod
        def forceCallFinish(*, call_id: str) -> Literal[1]: ...
        @staticmethod
        def get(*, offset: Positive = ..., count: Positive = ..., 
                time_offset: Positive = ...,
                filters:Positive = ..., preview_length:Positive = ...,
                last_message_id:Positive = ...) -> ResponseOfItems: ...
        @staticmethod
        def getByConversationMessageId(*, peer_id:int, conversation_message_ids: str,
                                       extended: bool = ..., fields: str = ...,
                                       group_id: Positive = ...
                                       ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getById(*, message_ids: str, preview_length: Positive = ...,
                    extended: bool = ..., fields: str = ...,
                    group_id: Positive = ...) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getChat(*, chat_id: Positive = ..., chat_ids: str = ...,
                    fields: str = ..., name_case: NAME_CASE = ...) -> VkObject: ...
        @staticmethod
        def getChatPreview(*, peer_id: Positive = ..., link: str = ...,
                           fields: str = ...) -> VkObject: ...
        @staticmethod
        def getChatUsers(*, chat_id: Positive = ..., chat_ids: str = ...,
                         fields: str = ..., name_case: NAME_CASE = ...
                         ) -> ListOfVkObjects: ...
        @staticmethod
        def getConversationMembers(*, peer_id: int, offset: Positive = ...,
                                   count: Positive = ..., extended: bool = ...,
                                   fields: str = ..., group_id: int = ...
                                   )->ExtendedResponseOfItems: ...
        @staticmethod
        def getConversations(*, offset: Positive = ..., count: Positive = ...,
                             filter: Literal["all", "important", "unanswered", "unread"] = ...,
                             extended: bool = ..., start_message_id: Positive = ...,
                             fields: str = ..., group_id: int = ...
                             ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getConversationsById(*, peer_ids: str, extended: bool = ...,
                                 fields: str = ..., group_id: Positive = ...,
                                 ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getDialogs(*, offset: int = ..., count: Positive = ...,
                       start_message_id: Positive = ..., preview_length: Positive = ...,
                       unread: bool = ..., important: bool = ..., unanswered: bool = ...,
                       user_id: str = ...) -> ResponseOfItems: ...
        @staticmethod
        def getHistory(*, offset: int = ..., count: Positive = ...,
                       user_id: str = ..., peer_id: int = ...,
                       start_message_id: int = ..., rev: int = ...,
                       extended: bool = ..., fields: str = ...,
                       group_id: int = ...) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getHistoryAttachments(*, peer_id: int, media_type: str = ...,
                                  start_from: str = ...,
                                  count: Positive = ..., photo_sizes: bool = ...,
                                  fields: str = ..., group_id: Positive = ...,
                                  preserve_order: bool = ..., 
                                  max_forwards_level: Positive = ...
                                  ) -> VkObject: ...
        @staticmethod
        def getImportantMessages(*, count: Positive = ..., offset: Positive = ...,
                                 start_message_id: Positive = ...,
                                 preview_length: Positive = ...,
                                 fields: str = ..., extended: bool = ...,
                                 group_id: Positive = ...
                                 ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getIntentUsers(*, intent: Literal["promo_newsletter",
                                              "non_promo_newsletter",
                                              "confirmed_notification"],
                           subscribe_id: Positive = ..., offset: Positive = ...,
                           count: Positive = ..., extended: bool = ...,
                           name_case: NAME_CASE = ..., fields: str = ...,
                           ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getInviteLink(*, peer_id: Positive, reset: bool = ...,
                          group_id: Positive = ...
                          ) -> dict[Literal["link"], str]: ...
        @staticmethod
        def getLastActivity(*, user_id: int) -> VkObject: ...
        @staticmethod
        def getLongPollHistory(*, ts: Positive = ..., pts: Positive = ...,
                               preview_length: Positive = ..., onlines: bool = ...,
                               fields: str = ..., events_limit: Positive = ...,
                               msgs_limit: Positive = ..., max_msg_id: Positive = ...,
                               group_id: int = ..., lp_version: Positive = ...,
                               last_n: Positive = ..., credentials: bool = ...,
                               extended: bool = ...) -> VkObject: ...
        @staticmethod
        def getLongPollServer(*, need_pts: bool = ..., group_id: int = ...,
                              lp_version: Positive=...) -> VkObject: ...
        @staticmethod
        def isMessagesFromGroupAllowed(*, group_id: str, user_id: str
                                       ) -> dict[Literal["is_allowed"], Literal[0, 1]]: ...
        @staticmethod
        def joinChatByInviteLink(*, link: str
                                 ) ->dict[Literal["chat_id"], int]: ...
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
                conversation_message_id: Positive = ...) -> VkObject: ...
        @staticmethod
        def removeChatUser(*, chat_id: Positive, user_id: int = ...,
                           member_id: int = ...) -> Literal[1]: ...
        @staticmethod
        def restore(*, message_id: Positive, group_id: Positive = ...) -> Literal[1]: ...
        @staticmethod
        def search(*, q: str = ..., peer_id: int = ..., date: Positive = ...,
                   preview_length: Positive = ..., offset: Positive = ...,
                   count: Positive = ..., extended: bool = ...,
                   fields: str = ..., group_id: Positive = ...
                   ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def searchConversations(*, q: str = ..., count: Positive = ...,
                                extended: bool = ..., fields: str = ...,
                                group_id: Positive = ...
                                ) -> ExtendedResponseOfItems: ...
        @staticmethod
        def searchDialogs(*, q: str = ..., limit: Positive = ..., 
                          fields: str = ...) -> VkObject: ...
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
                 subscribe_id: Positive = ...) -> VkObject | int: ...
        @staticmethod
        def sendMessageEventAnswer(*, event_id: str, user_id: int, peer_id: int,
                                   event_data: str = ...) -> Literal[1]: ...
        @staticmethod
        def setActivity(*, user_id: str = ..., type: Literal["typing",
                                                             "audiomessage"] = ...,
                        peer_id: int = ..., group_id: Positive = ...) -> Literal[1]: ...
        @staticmethod
        def setChatPhoto(*, file: str) -> VkObject: ...
        @staticmethod
        def startCall(*, group_id: int = ...) -> VkObject: ...
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
            ) -> ResponseOfItems: ...

    class secure:
        ...

    class stats:
        @staticmethod
        def get(*, group_id: Positive = ..., app_id: Positive = ...,
                date_from : str = ..., date_to: str = ...,
                timestamp_from: Positive = ..., timestamp_to: Positive = ...,
                interval: Literal["day", "week", "month", "year", "all"] = ...,
                intervals_count: Positive = ..., filters: str = ...,
                stats_groups: Literal["visitors", "reach", "activity"] = ...,
                extended: bool = ...) -> VkObject: ...
        @staticmethod
        def getPostReach(*, owner_id: str,
                         post_ids: str) -> ListOfVkObjects: ...
        @staticmethod
        def trackVisitor() -> Literal[1]: ...
    class status:
        @staticmethod
        def get(*, user_id: int = ...,
                group_id: Positive = ...
                ) -> dict[Literal["text"], str]: ...
        @staticmethod
        def set(*, text: str = ...,
                group_id: Positive = ...) -> Literal[1]: ...
    class storage:
        @staticmethod
        def get(*, key: str = ...,
                keys: str = ...,
                user_id: Positive = ...) -> ListOfVkObjects: ...
        @staticmethod
        def getKeys(*, user_id: Positive = ...,
                    offset: Positive = ..., count: Positive = ...
                    ) -> list[str]: ...
        @staticmethod
        def set(*, key: str, value: Text = ..., user_id: Positive = ...) ->Literal[1]: ...
    class store:
        @staticmethod
        def addStickersToFavorite(*, stickers_ids: str) -> Literal[1]: ...
        @staticmethod
        def getFavoriteStickers() -> ResponseOfItems: ...
        @staticmethod
        def getProducts(*, type: Literal["stickers", "votes"] = ...,
                        merchant: Literal["google", "apple", "microsoft"] = ...,
                        section: str = ..., product_ids: str = ...,
                        filters: str = ...,
                        extended: bool = ...) -> ExtendedResponseOfItems: ...
        @staticmethod
        def getStickersKeywords(*, stickers_ids: str = ...,
                                products_ids: str = ...,
                                aliases: bool = ...,
                                all_products: bool = ...,
                                need_stickers: bool = ...) -> VkObject: ...
        @staticmethod
        def removeStickersFromFavorite(*, sticker_ids: str) -> Literal[1]: ...

    class stories:
        ...

    class streaming:
        @staticmethod
        def getServerUrl() -> VkObject: ...
        @staticmethod
        def getSettings() -> VkObject: ...
        @staticmethod
        def getStats(*, type: Literal["received", "prepared"] = ...,
                     interval: Literal["5m", "1h", "24h"] = ...,
                     start_time: Positive = ..., end_time: Positive = ...
                     ) -> ListOfVkObjects: ...
        @staticmethod
        def getStem(*, word: str) -> Any: ...
        @staticmethod
        def setSettings(*,
                        monthly_tier: Literal["tier_1",
                                              "tier_2",
                                              "tier_3",
                                              "tier_4",
                                              "tier_5",
                                              "tier_6",
                                              "unlimited"]) -> Literal[1]: ...
    class users:
        @staticmethod
        def get(*, user_ids: str = ..., fields: str = ...,
                name_case: NAME_CASE = ...
                ) -> ListOfVkObjects:
            """Возвращает расширенную информацию о пользователях."""
        @staticmethod
        def getFollowers(*, user_id: Positive = ..., offset: Positive = ...,
                         count: Positive = ..., fields: str = ...,
                         name_case: NAME_CASE = ...
                         ) -> ResponseOfItems: ...

        @staticmethod
        def getSubscriptions(*, user_id: Positive = ..., extended: bool = ...,
                             offset: Positive = ..., count: Positive = ...,
                             fields: str = ...) -> ExtendedResponseOfItems: ...

        @staticmethod
        def report(*, user_id: Positive, type: Literal["porn", "spam",
                   "insult", "advertisеment"], comment: str = ...) -> Literal[1]: ...

        @staticmethod
        def search(*, q: str = ..., sort: Literal[0, 1] = ...,
                   offset: Positive = ..., count: Positive = ...,
                   fields: str = ..., city: Positive = ...,
                   country: Positive = ..., hometown: str = ...,
                   university_country: Positive = ...,
                   university: Positive = ..., university_year: Positive = ...,
                   university_faculty: Positive = ...,
                   university_chair: Positive = ...,
                   sex: Literal[0, 1, 2] = ...,
                   status: Literal[1, 2, 3, 4, 5, 6, 7, 8] = ...,
                   age_from: Positive = ..., age_to: Positive = ...,
                   birth_day: Positive = ...,
                   birth_month: Positive = ..., birth_year: Positive  = ...,
                   online: bool = ...,
                   has_photo: bool = ..., school_country: Positive = ...,
                   school_city: Positive = ..., school_class: Positive = ...,
                   school: Positive  = ..., school_year: Positive = ...,
                   religion: str = ..., company: str = ..., position: str = ...,
                   group_id: Positive = ..., from_list: str  = ...
                   ) -> ResponseOfItems: ...
    class utils:
        @staticmethod
        def checkLink(*, url: str
                      ) -> dict[Literal["status", "link"], str]: ...
        @staticmethod
        def deleteFromLastShortened(*, key: str) -> Literal[1]: ...
        @staticmethod
        def getLastShortenedLinks(*, count: Positive=..., offset: Positive = ...
                                  ) -> ResponseOfItems: ...
        @staticmethod
        def getLinkStats(*, key: str, source: str = ..., access_key: str = ...,
                         interval: Literal["hour", "day", "week", "month",
                                           "forever"] = ...,
                         intervals_count: Positive = ..., extended: bool = ...
                         )->VkObject: ...
        @staticmethod
        def getServerTime() -> int: ...
        @staticmethod
        def getShortLink(*, url: str, private: bool = ...
                         ) -> dict[Literal["short_url"], str]: ...
        @staticmethod
        def resolveScreenName(*, screen_name: str) -> VkObject: ...
        

    class video:
        ...

    class wall:
        ...

    class widgets:
        @staticmethod
        def getComments(*, widget_api_id: int = ..., url: str = ...,
                        page_id: str = ..., order: str = ...,
                        fields: str = ..., offset: Positive = ...,
                        count: Positive = ...) -> VkObject: ...
        @staticmethod
        def getPages(*, widget_api_id: int = ...,
                     order: Literal["date", "comments", "likes",
                                    "friend_likes"] = ...,
                     offset: Positive = ..., count: Positive = ...
                     ) -> VkObject: ...

    class audio:
        @staticmethod
        def get(*, owner_id: int = ..., album_id: int = ...,
                audio_ids: str = ..., need_user: bool = ...,
                offset: Positive = ..., count: Positive = ...) -> VkObject:
            "Возвращает список аудиозаписей пользователя или сообщества."
        @staticmethod
        def getById(*, audios: str) -> ListOfVkObjects:
            "Возвращает информацию об аудиозаписях."
        @staticmethod
        def getLyrics(*, lyrics_id: int) -> VkObject:
            "Возвращает текст аудиозаписи."
        @staticmethod
        def search(*, q: str, auto_complete: bool = ...,
                   lyrics: bool = ..., performer_only: bool = ...,
                   sort: int = ..., search_own: Literal[0, 1] = ...,
                   offset: Positive = ..., count: Positive = ...) -> VkObject:
            "Возвращает список аудиозаписей в соответствии с заданным критерием поиска."
        @staticmethod
        def getUploadServer() -> VkObject:
            "Возвращает адрес сервера для загрузки аудиозаписей."
        @staticmethod
        def save(*, server: int, audio: str, hash: str = ..., artist: str = ...,
                 title: str = ...) -> VkObject:
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
        def restore(*, audio_id: Positive, owner_id: int = ...) -> VkObject:
            "Восстанавливает аудиозапись после удаления."
        @staticmethod
        def getPlaylists(*, owner_id: int = ..., offset: Positive = ...,
                      cont: int = 50) -> VkObject:
            "Возвращает список альбомов аудиозаписей пользователя или группы."
        @staticmethod
        def addPlaylist(*, group_id: Positive = ..., title: str = ...) -> int:
            "Создает пустой альбом аудиозаписей."
        @staticmethod
        def editPlaylist(*, album_id: Positive, title: str,
                         group_id: Positive = ...
                      ) -> Literal[1]:
            "Редактирует название альбома аудиозаписей."
        @staticmethod
        def deletePlaylist(*, group_id: Positive = ..., album_id: Positive = ...
                        ) -> Literal[1]:
            "Удаляет альбом аудиозаписей."
        @staticmethod
        def moveToPlaylist(*, audio_ids: str, group_id: Positive = ...,
                           album_id: Positive = ...
                        ) -> Literal[1]:
            "Перемещает аудиозаписи в альбом."
        @staticmethod
        def setBroadcast(*, audio: str = ..., target_ids: str) -> VkObject:
            "Транслирует аудиозапись в статус пользователю или сообществу."
        @staticmethod
        def getBroadcastList(*, filter: Literal["friends", "groups", "all"] = ...,
                             active: bool = ...) -> ListOfVkObjects:
            "Возвращает список друзей и сообществ пользователя, которые транслируют музыку в статус."
        @staticmethod
        def getRecommendations(*, target_audio: str = ..., user_id: Positive  = ...,
                               offset: Positive  = ..., count: Positive = ...,
                               shuffle: bool = ...) -> ListOfVkObjects:
            "Возвращает список рекомендуемых аудиозаписей на основе списка воспроизведения заданного пользователя или на основе одной выбранной аудиозаписи."
        @staticmethod
        def getPopular(*, only_eng: bool = ..., genre_id: Positive  = ...,
                       offset: Positive = ..., count: Positive = ...
                       ) -> ListOfVkObjects:
            "Возвращает список аудиозаписей из раздела “Популярное”."
        @staticmethod
        def getCount(*, owner_id: int) -> int:
            "Возвращает количество аудиозаписей пользователя или сообщества."
