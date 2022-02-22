from ...reqs import publications
from ...api import get_date
from .. import main

class Publication(object):
    __slots__ = (
        "id",
        "category",
        "type",
        "parent_id",
        "parent_type",
        "sub_units",
        "karma",
        "my_karma",
        "reports",
        "is_important",
        "is_closed",
        "date_create",
        "status",
        
        "author_id",
        "author_name",
        "author_avatar",
        "author_karma_30",
        "author_sex",
        "author_lvl",
        "author_last_online",
        "author",
        
        "fandom_id",
        "fandom_lang",
        "fandom_name",
        "fandom_karma_cof",
        "fandom_is_closed",
        "fandom_image",
        "fandom",
        
        "tags",
        "s_tag"
    )
    
    TYPE_COMMENT = 1
    TYPE_MESSAGE = 8
    TYPE_POST = 9
    TYPE_TAG = 10
    TYPE_MODERATION = 11
    TYPE_EVENT_USER = 12
    TYPE_STICKER_PACK = 15
    TYPE_STICKER = 16
    TYPE_EVENT_MODER = 17
    TYPE_EVENT_ADMIN = 18
    TYPE_EVENT_FANDOM = 19
    TYPE_UNKNOWN = 20
    
    _type_classes = {
        1: "comment",
        8: "message",
        9: "post",
        10: "tag",
        11: "moderation",
        15: "stickerpack",
        16: "sticker"
    }
    _type_classes_valid = _type_classes.keys()
    
    def __init__(self, content):
        self.id = content["id"]
        self.category = content["category"]
        self.type = content["unitType"]
        self.parent_id = content["parentUnitId"]
        self.parent_type = content["parentUnitType"]
        self.sub_units = content["subUnitsCount"]
        self.karma = content["karmaCount"] / 100
        self.my_karma = content["myKarma"] / 100
        self.reports = content["reportsCount"]
        self.is_important = True if content["important"] == -1 else False
        self.is_closed = content["closed"]
        self.date_create = get_date(content["dateCreate"])
        self.status = content["status"]
        
        self.author_id = content["creatorId"]
        self.author_name = content["creatorName"]
        self.author_avatar = content["creatorImageId"]
        self.author_karma_30 = content["creatorKarma30"] / 100
        self.author_sex = content["creatorSex"]
        self.author_lvl = content["creatorLvl"] / 100
        self.author_last_online = get_date(content["creatorLastOnlineTime"])
        self.author = main._all["account"](content["creator"])
        
        self.fandom_id = content["fandomId"]
        self.fandom_lang = content["languageId"]
        self.fandom_name = content["fandomName"]
        self.fandom_karma_cof = content["fandomKarmaCof"] / 100
        self.fandom_is_closed = True if content["fandomClosed"] == -1 else False
        self.fandom_image = content["fandomImageId"]
        self.fandom = main._all["fandom"](content["fandom"])
        
        self.tags = (
            content["tag_1"],
            content["tag_2"],
            content["tag_3"],
            content["tag_4"],
            content["tag_5"],
            content["tag_6"],
            content["tag_7"],
        )
        self.s_tag = content["tag_s_1"]
    
    def get_comments(self, *, offset: int = 0, from_bottom: bool = False):
        comments = publications.get_comments(self.id, offset, from_bottom)
        return [ main._all["comment"](comment) for comment in comments ]
    
    def comment(self, text: str, *, sticker: int = 0, images: list = [], reply: int = 0):
        comment = publications.comment(self.id, text, sticker, images, reply)
        return main._all["comment"](comment)
    
    def set_karma(self, positive: bool = True, *, anonim: bool = False):
        return publications.set_karma(self.id, positive, anonim)
    
    def add_reaction(self, index: int):
        return publications.reaction_add(self.id, index)
    
    def remove_reaction(self, index: int):
        return publications.reaction_remove(self.id, index)
    
    def get_reaction(self, index: int):
        accounts = publications.reaction_get(self.id, index)
        return [ main._all["account"](account) for account in accounts ]
    
    def report(self, text: str):
        return publications.report(self.id, text)
    
    def get_rates(self, *, offset: int = 0):
        rates = publications.get_rates(self.id, offset)
        return [ Rate(rate) for rate in rates ]
    
    def get_history(self, *, offset: int = 0):
        history = publications.get_history(self.id, offset)
        return [ HistoryItem(item) for item in history ]
    
    def get_reports(self, *, offset: int = 0):
        reports = publications.get_reports(self.id, offset)
        return [ Report(report) for report in reports ]
    
    # Self-actions
    
    def remove(self):
        return publications.remove(self.id)
    
    # Moderator
    
    def moderator_block(self, comment: str, block_last_publications: bool = False, ban_time: int = -1, block_in_app: bool = False):
        return publications.moderator_block(self.id, comment, block_last_publications, ban_time, block_in_app)
    
    def moderator_clear_reports(self):
        return publications.moderator_clear_reports(self.id)

class Rate(object):
    __slots__ = (
        "id",
        "parent_id",
        "date",
        "karma_cof",
        "karma",
        "anonim",
        "author"
    )
    
    def __init__(self, content):
        self.id = content["unitId"]
        self.parent_id = content["unitParentId"]
        self.date = get_date(content["date"])
        self.karma_cof = content["karmaCof"] / 100
        self.karma = content["karmaCount"] / 100
        self.anonim = content["anonymous"]
        self.author = main._all["account"](content["account"])

class HistoryItem(object):
    __slots__ = (
        "date",
        "unit_id",
        "id",
        
        "author_id",
        "author_avatar",
        "author_name",
        "comment",
        "type"
    )
    
    def __init__(self, content):
        self.date = get_date(content["date"])
        self.unit_id = content["unitId"]
        self.id = content["id"]
        
        self.author_id = content["history"]["userId"]
        self.author_avatar = content["history"]["userImageId"]
        self.author_name = content["history"]["userName"]
        self.comment = content["history"]["comment"]
        self.type = content["history"]["type"]

class Report(object):
    __slots__ = (
        "id",
        "account",
        "comment"
    )
    
    def __init__(self, content):
        self.id = content["id"]
        self.account = main._all["account"](content["account"])
        self.comment = content["comment"]

main._all["publication"] = Publication
main._all["rate"] = Rate
main._all["report"] = Report
main._all["historyitem"] = HistoryItem