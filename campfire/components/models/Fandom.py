from ..reqs import fandoms
from ..api import get_date
from . import main

_pubcls = main._all["publication"]

class Fandom(object):
    __slots__ = (
        "id",
        "name",
        "subscribers",
        "karma_cof",
        "lang",
        "date_create",
        "category",
        "closed",
        
        "author_id",
        "avatar",
        "background"
    )
    
    def __init__(self, content):
        self.id = content["id"]
        self.name = content["name"]
        self.subscribers = content["subscribesCount"]
        self.karma_cof = content["karmaCof"] / 100
        self.lang = content["languageId"]
        self.date_create = get_date(content["dateCreate"])
        self.category = content["category"]
        self.closed = True if content["closed"] == -1 else False
        
        self.author_id = content["creatorId"]
        self.avatar = content["imageId"]
        self.background = content["imageTitleId"]
    
    @staticmethod
    def get(fandom_id: int, fandom_lang: int = 2):
        return Fandom(fandoms.get(fandom_id, fandom_lang))
    
    @staticmethod
    def get_all(
            name: str,
            fandom_lang: int = 2,
            *,
            offset: int = 0,
            subscribed: int = 0,
            category_id: int = 0,
            params1: list = [],
            params2: list = [],
            params3: list = [],
            params4: list = [] ):
        allfandoms = fandoms.get_all(name, fandom_lang, offset, subscribed, category_id, params1, params2, params3, params4)
        return [ Fandom(fandom) for fandom in allfandoms ]
    
    def get_info(self):
        return FandomInfo(fandoms.get_info(self.id, self.lang))
    
    def get_publications(self,
            offset: int = 0,
            count: int = 20,
            types: list = _pubcls._type_classes_valid,
            *,
            fandom_ids: list = [],
            only_with_fandom: bool = False,
            important: bool = False,
            tags: list = [] ):
        units = fandoms.get_publications(self.id, self.lang, offset, count, fandom_ids, only_with_fandom, important, types, tags)
        
        res = [ main._all[_pubcls._type_classes[unit["unitType"]]](unit) for unit in units if _pubcls._type_classes[unit["unitType"]] in main._all ]
        return res
    
    @staticmethod
    def suggest(name: str, avatar: bytes, background: bytes, note: str = "", *, closed: bool = False, category_id: int = 1, params1: list = [0], params2: list = [0], params3: list = [0], params4: list = [0]):
        return fandoms.suggest(name, note, avatar, background, category_id, closed, params1, params2, params3, params4)
    
    def subscribe(self, subscribed: int = 0, important: bool = True):
        return fandoms.subscribe(self.id, self.lang, subscribed, important)
    
    def get_subscribers(self, offset: int = 0):
        accounts = fandoms.get_subscribers(self.id, self.lang, offset)
        return [ main._all["account"](account) for account in accounts ]
    
    def get_chats(self, offset: int = 0):
        chats = fandoms.get_chats(self.id, self.lang, offset)
        return [ main._all["chat"](chat) for chat in chats ]
    
    def get_activities(self, offset: int = 0):
        activities = fandoms.get_activities(self.id, self.lang, offset)
        return [ main._all["activity"](activity) for activity in activities ]
    
    def get_rubrics(self, offset: int = 0):
        rubrics = fandoms.get_rubrics(self.id, self.lang, offset)
        return [ main._all["rubric"](rubric) for rubric in rubrics ]
    
    def add_bl(self):
        return fandoms.add_bl(self.id)
    
    def remove_bl(self):
        return fandoms.remove_bl(self.id)
    
    def check_bl(self):
        return fandoms.check_bl(self.id)
    
    # Moderator
    
    def moderator_create_chat(self, comment: str, name: str, text: str, avatar: bytes):
        return fandoms.moderator_create_chat(self.id, self.lang, comment, name, text, avatar)
    
    def moderator_change_chat_background(self, comment: str, background: bytes):
        return fandoms.moderator_change_chat_background(self.id, self.lang, comment, background)
    
    def moderator_add_link(self, comment: str, title: str, url: str, icon: int = -1):
        return fandoms.moderator_add_link(self.id, self.lang, comment, title, url, icon)
    
    @staticmethod
    def moderator_remove_link(comment: str, index: int):
        return fandoms.moderator_remove_link(comment, index)
    
    def moderator_change_link(self, comment: str, index: int, title: str, url: str, icon: int = -1):
        return fandoms.moderator_change_link(self.id, self.lang, comment, index, title, url, icon)
    
    def moderator_change_description(self, comment: str, text: str):
        return fandoms.moderator_change_description(self.id, self.lang, comment, text)
    
    def moderator_gallery_add(self, comment: str, image: bytes):
        return fandoms.moderator_gallery_add(self.id, self.lang, comment, image)
    
    def moderator_gallery_remove(self, comment: str, image_id: int):
        return fandoms.moderator_gallery_remove(self.id, self.lang, comment, image_id)
    
    def moderator_set_names(self, comment: str, names: list):
        return fandoms.moderator_set_names(self.id, self.lang, comment, names)
    
    def moderator_create_activity(self, comment: str, name: str, description: str, account_id: int):
        return fandoms.moderator_create_activity(self.id, self.lang, comment, name, description, account_id)
    
    def moderator_create_rubric(self, comment: str, name: str, account_id: int):
        return fandoms.moderator_create_rubric(self.id, self.lang, comment, name, account_id)
    
    # Admin
    
    def admin_change_avatar(self, comment: str, image: bytes):
        return fandoms.admin_change_avatar(self.id, comment, image)
    
    def admin_change_name(self, comment: str, name: str):
        return fandoms.admin_change_name(self.id, comment, name)
    
    def admin_close(self, comment: str, closed: bool = True):
        return fandoms.admin_close(self.id, comment, closed)
    
    def admin_remove_moderator(self, comment: str, account_id: int):
        return fandoms.admin_remove_moderator(self.id, self.lang, comment, account_id)
    
    def admin_change_viceroy(self, comment: str, account_id: int):
        return fandoms.admin_change_viceroy(self.id, self.lang, comment, account_id)
    
    def admin_remove_viceroy(self, comment: str):
        return fandoms.admin_remove_viceroy(self.id, self.lang, comment)
    
    def admin_set_cof(self, comment: str, karma_cof: int):
        return fandoms.admin_set_cof(self.id, comment, karma_cof)
    
    def admin_remove(self, comment: str):
        return fandoms.admin_remove(self.id, comment)
    
    def admin_change_category(self, comment: str, category_id: int):
        return fandoms.admin_change_category(self.id, comment, category_id)
    
    @staticmethod
    def admin_get_suggested(offset: int = 0):
        allfandoms = fandoms.admin_get_suggested(offset)
        return [ FandomSuggested(fandom) for fandom in allfandoms ]

class FandomSuggested(Fandom):
    __slots__ = ()
    
    def admin_get_info(self):
        fandom = fandoms.admin_get_info(self.id)
        res = {}
        res["fandom"] = Fandom(content["fandom"])
        res["author"] = main._all["account"](content["creator"])
        res["params1"] = content["params1"]
        res["params2"] = content["params2"]
        res["params3"] = content["params3"]
        res["params4"] = content["params4"]
        res["note"] = content["notes"]
        return res
    
    def admin_accept(self, comment: str, accepted: bool = True):
        return fandoms.admin_accept(self.id, comment, accepted)

class FandomInfo(object):
    __slots__ = (
        "description",
        "names",
        "links",
        "gallery",
        "category",
        
        "params1",
        "params2",
        "params3",
        "params4"
    )
    
    def __init__(self, content):
        self.description = content["description"]
        self.names = content["names"]
        self.links = content["links"]
        self.gallery = content["gallery"]
        self.category = content["categoryId"]
        
        self.params1 = content["params1"]
        self.params2 = content["params2"]
        self.params3 = content["params3"]
        self.params4 = content["params4"]

main._all["fandom"] = Fandom
main._all["fandominfo"] = FandomInfo