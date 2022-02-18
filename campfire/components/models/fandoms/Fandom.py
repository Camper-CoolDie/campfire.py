from ...reqs import fandoms
from ...api import get_date
from .. import main

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

main._all["fandom"] = Fandom