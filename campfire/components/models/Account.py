from ..reqs import account
from ..api import get_date
from . import main

class Account(object):
    __slots__ = (
        "id",
        "name",
        "sex",
        "karma_30",
        "avatar",
        "level",
        "last_online",
        "sponsor",
        "sponsor_times",
        "date_create",
        "effects"
    )
    
    def __init__(self, content):
        self.id = content["J_ID"]
        self.name = content["J_NAME"]
        self.sex = content["sex"]
        self.karma_30 = content["karma30"] / 100
        self.avatar = content["J_IMAGE_ID"]
        self.level = content["J_LVL"] / 100
        self.last_online = get_date(content["J_LAST_ONLINE_DATE"])
        self.sponsor = content["sponsor"]
        self.sponsor_times = content["sponsorTimes"]
        self.date_create = get_date(content["J_DATE_CREATE"])
        self.effects = [ AccountEffect(effect) for effect in content["accountEffects"] ]
    
    @staticmethod
    def get(account_id: int = 0, account_name: str = ""):
        return Account(account.get(account_id, account_name))
    
    @staticmethod
    def get_from_rating():
        content = account.get_from_rating()
        return [ Account(account) for account in content["karmaAccounts"] ], [ Account(account) for account in content["forceAccounts"] ]
    
    @staticmethod
    def get_from_online(offset_date: int = 0):
        accounts = account.get_from_online(offset_date)
        return [ Account(account) for account in accounts ]
    
    def get_profile(self):
        return AccountProfile(account.get_profile(self.id, ""))
    
    def get_story(self):
        return AccountStory(account.get_story(self.id))
    
    def follow(self, state: bool = True):
        return account.follow(self.id, state)
    
    def get_follows(self, *, offset: int = 0):
        accounts = account.get_follows(self.id, False, offset)
        return [ Account(account) for account in accounts ]
    
    def get_followers(self, *, offset: int = 0):
        accounts = account.get_follows(self.id, True, offset)
        return [ Account(account) for account in accounts ]
    
    def get_rates(self, *, offset: int = 0):
        rates = account.get_rates(self.id, offset)
        return [ main._all["rate"](rate) for rate in rates ]
    
    def get_punishments(self, *, offset: int = 0):
        punishments = account.get_punishments(self.id, offset)
        return [ AccountPunishment(punish) for punish in punishments ]
    
    def add_bl(self):
        return account.add_bl(self.id)
    
    def remove_bl(self):
        return account.remove_bl(self.id)
    
    def check_bl(self):
        return account.check_bl(self.id)
    
    def get_subscribed_fandoms(self, offset: int = 0):
        fandoms = account.get_subscribed_fandoms(self.id, offset)
        return [ main._all["fandom"](fandom) for fandom in fandoms ]
    
    def get_moderated_fandoms(self, offset: int = 0):
        fandoms = account.get_moderated_fandoms(self.id, offset)
        return [ main._all["fandom"](fandom) for fandom in fandoms ]
    
    def get_activities(self, *, offset: int = 0):
        activities = account.get_activities(self.id, offset)
        return [ main._all["activity"](activity) for activity in activities ]
    
    def get_rubrics(self, *, offset: int = 0):
        rubrics = account.get_rubrics(self.id, offset)
        return [ main._all["rubric"](rubric) for rubric in rubrics ]
    
    def report(self, comment: str):
        return account.report(self.id, comment)
    
    def get_publications(self, lang: int = 2, offset: int = 0, count: int = 20, types: list = [1, 8, 9, 11]):
        """Get publications"""
        
        params = {
            "accountId": self.account_id,
            "parentUnitId": 0,
            "offset": int(offset),
            "fandomId": 0,
            "fandomIds": [],
            "important": 0,
            "drafts": False,
            "includeZeroLanguages": True,
            "includeModerationsBlocks": True,
            "includeModerationsOther": True,
            "includeMultilingual": True,
            "unitTypes": list(types),
            "order": 1,
            "languageId": int(lang),
            "onlyWithFandom": True,
            "count": int(count),
            "appKey": None,
            "appSubKey": None,
            "tags": [],
            "J_REQUEST_NAME": "RPublicationsGetAll"
        }
        content = post(params)
        if "code" in content: return
        
        res = []
        for unit in content["units"]:
            for unit_type, category in category_types.items():
                if unit["unitType"] == category:
                    if unit_type == "COMMENT":
                        res.append((unit["unitType"], Comment.Comment(unit)))
                    elif unit_type == "POST":
                        res.append((unit["unitType"], Post.Post(unit)))
                    elif unit_type == "MESSAGE":
                        res.append((unit["unitType"], Chat.Message(unit)))
                    elif unit_type == "MODERATION":
                        res.append((unit["unitType"], Moderation.Moderation(unit)))
                    else:
                        res.append(None)
                    break
        
        return res
    
    # Admin
    
    def admin_ban(self, comment: str, ban_time: int):
        """Ban this Account"""
        
        params = {
            "accountId": self.account_id,
            "banTime": get_deltastamp(ban_time),
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsAdminBan"
        }
        content = post(params)
        return content
    
    def admin_change_name(self, comment: str, name: str):
        """Change name"""
        
        params = {
            "accountId": self.account_id,
            "name": str(name),
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsAdminChangeName"
        }
        content = post(params)
        return content
    
    def admin_add_effect(self, comment: str, index: int, end_date: int):
        """Add effect"""
        
        params = {
            "accountId": self.account_id,
            "effectIndex": int(index),
            "effectEndDate": get_timestamp(end_date),
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsAdminEffectAdd"
        }
        content = post(params)
        return content
    
    @staticmethod
    def admin_remove_effect(comment: str, effect_id: int):
        """Remove effect"""
        
        params = {
            "effectId": int(effect_id),
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsAdminEffectRemove"
        }
        content = post(params)
        return content
    
    def admin_remove_description(self, comment: str):
        """Remove description"""
        
        params = {
            "accountId": self.account_id,
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsAdminRemoveDescription"
        }
        content = post(params)
        return content
    
    def admin_remove_status(self, comment: str):
        """Remove status"""
        
        params = {
            "accountId": self.account_id,
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsAdminStatusRemove"
        }
        content = post(params)
        return content
    
    def admin_remove_link(self, comment: str, index: int):
        """Remove link"""
        
        params = {
            "accountId": self.account_id,
            "index": int(index),
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsAdminRemoveLink"
        }
        content = post(params)
        return content
    
    def admin_remove_background(self, comment: str):
        """Remove background"""
        
        params = {
            "accountId": self.account_id,
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsRemoveTitleImage"
        }
        content = post(params)
        return content
    
    def admin_remove_avatar(self, comment: str):
        """Remove avatar"""
        
        params = {
            "accountId": self.account_id,
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsRemoveAvatar"
        }
        content = post(params)
        return content
    
    def admin_remove_name(self, comment: str):
        """Remove name"""
        
        params = {
            "accountId": self.account_id,
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsRemoveName"
        }
        content = post(params)
        return content
    
    def admin_recount_karma(self, comment: str):
        """Recount karma"""
        
        params = {
            "accountId": self.account_id,
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsKarmaRecount"
        }
        content = post(params)
        return content
    
    def admin_recount_achievements(self, comment: str):
        """Recount achievements (level)"""
        
        params = {
            "accountId": self.account_id,
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsAchievementsRecount"
        }
        content = post(params)
        return content
    
    def admin_clear_reports(self, comment: str):
        """Clear reports"""
        
        params = {
            "accountId": self.account_id,
            "comment": str(comment),
            "J_REQUEST_NAME": "RAccountsClearReports"
        }
        content = post(params)
        return content
    
    def admin_get_reports(self, *, offset: int = 0):
        """Get reports"""
        
        params = {
            "unitId": self.account_id,
            "offset": int(offset),
            "J_REQUEST_NAME": "RAccountsReportsGetAllForAccount"
        }
        content = post(params)
        if "code" in content: return content
        
        res = []
        for report in content["reports"]:
            res.append(Publication.Report(report))
        
        return res
    
    def admin_remove_moderator(self, comment: str, fandom_id: int, lang: int = 2):
        """Remove moderator in Fandom"""
        
        params = {
            "fandomId": int(fandom_id),
            "languageId": int(lang),
            "accountId": self.account_id,
            "comment": str(comment),
            "J_REQUEST_NAME": "RFandomsAdminRemoveModerator"
        }
        content = post(params)
        return content
    
    def admin_change_viceroy(self, comment: str, fandom_id: int, lang: int = 2):
        """Change Viceroy in Fandom"""
        
        params = {
            "fandomId": int(fandom_id),
            "languageId": int(lang),
            "accountId": self.account_id,
            "comment": str(comment),
            "J_REQUEST_NAME": "RFandomsAdminViceroyAssign"
        }
        content = post(params)
        return content

class AccountProfile(object):
    __slots__ = (
        "karma_total",
        "background",
        "background_gif",
        "description",
        "status",
        "age",
        "warns",
        "bans",
        "follows",
        "followers",
        
        "ban_date",
        "bl_fandoms",
        "bl_accounts",
        "rates",
        "stickers",
        "moderation_fandoms",
        "subscribed_fandoms",
        "pinned_post",
        
        "is_follow",
        "note",
        "links"
    )
    
    def __init__(self, content):
        self.karma_total = content["karmaTotal"] / 100
        self.background = content["titleImageId"]
        self.background_gif = content["titleImageGifId"]
        self.description = content["description"]
        self.status = content["status"]
        self.age = content["age"]
        self.warns = content["warnsCount"]
        self.bans = content["bansCount"]
        self.follows = content["followsCount"]
        self.followers = content["followersCount"]
        
        self.ban_date = get_date(content["banDate"])
        self.bl_fandoms = content["blackFandomsCount"]
        self.bl_accounts = content["blackAccountsCount"]
        self.rates = content["rates"]
        self.stickers = content["stickersCount"]
        self.moderation_fandoms = content["moderationFandomsCount"]
        self.subscribed_fandoms = content["subscribedFandomsCount"]
        
        if content["pinnedPost"] != None:
            self.pinned_post = main._all["post"](content["pinnedPost"])
        else:
            self.pinned_post = None
        
        self.is_follow = content["isFollow"]
        self.note = content["note"]
        self.links = content["links"]

class AccountStory(object):
    __slots__ = (
        "total_karma_plus",
        "total_karma_minus",
        "total_rates_plus",
        "total_rates_minus",
        
        "total_karma",
        "total_rates",
        "total_comments",
        "total_posts",
        "total_messages",
        
        "best_post",
        "best_comment"
    )
    
    def __init__(self, content):
        self.total_karma_plus = content["totalKarmaPlus"] / 100
        self.total_karma_minus = content["totalKarmaMinus"] / 100
        self.total_rates_plus = content["totalRatesPlus"]
        self.total_rates_minus = content["totalRatesMinus"]
        
        self.total_karma = content["totalKarmaPlus"] - content["totalKarmaMinus"] / 100
        self.total_rates = content["totalRatesPlus"] + content["totalRatesMinus"]
        self.total_comments = content["totalComments"]
        self.total_posts = content["totalPosts"]
        self.total_messages = content["totalMessages"]
        
        self.best_post = content["bestPost"]
        self.best_comment = content["bestComment"]

class AccountEffect(object):
    __slots__ = (
        "id",
        "account_id",
        "date_create",
        "date_end",
        "comment",
        
        "index",
        "tag",
        "comment_tag",
        "account_name"
    )
    
    HATER = 1
    PIG = 2
    VAHTER = 3
    GOOSE = 4
    SNOW = 5
    BAN = 6
    TRANSLATOR = 7
    MENTION_LOCK = 8
    
    def __init__(self, content):
        self.id = content["id"]
        self.account_id = content["accountId"]
        self.date_create = get_date(content["dateCreate"])
        self.date_end = get_date(content["dateEnd"])
        self.comment = content["comment"]
        
        self.index = content["effectIndex"]
        self.tag = content["tag"]
        self.comment_tag = content["commentTag"]
        self.account_name = content["fromAccountName"]
    
    def admin_remove(self, comment: str):
        return account.admin_effect_remove(self.id, comment)

class AccountPunishment(object):
    __slots__ = (
        "id",
        "owner_id",
        "fandom_id",
        "fandom_name",
        "fandom_lang",
        "fandom_avatar",
        "comment",
        
        "account_id",
        "account_avatar",
        "account_name",
        "account_sex",
        
        "ban_date",
        "date_create"
    )
    
    def __init__(self, content):
        self.id = content["id"]
        self.owner_id = content["ownerId"]
        self.fandom_id = content["fandomId"]
        self.fandom_name = content["fandomName"]
        self.fandom_lang = content["languageId"]
        self.fandom_avatar = content["fandomImageId"]
        self.comment = content["comment"]
        
        self.account_id = content["fromAccountId"]
        self.account_avatar = content["fromAccountImageId"]
        self.account_name = content["fromAccountName"]
        self.account_sex = content["fromAccountSex"]
        
        self.ban_date = get_date(content["banDate"])
        self.date_create = get_date(content["dateCreate"])
    
    def admin_remove(self, comment: str):
        return account.admin_punishment_remove(self.id, comment)

main._all["account"] = Account
main._all["accountprofile"] = AccountProfile
main._all["accountstory"] = AccountStory
main._all["accounteffect"] = AccountEffect