# This file was generated automatically
# using other files prepared for generation

from ._abcollect import *

def get(account_id: int, account_name: str):
    params = {
        "accountId": int(account_id),
        "accountName": str(account_name),
        "J_REQUEST_NAME": "RAccountsGet"
    }
    return campreq(params)["account"]

def get_from_rating():
    params = {
        "J_REQUEST_NAME": "RAccountsRatingGet"
    }
    return campreq(params)["accounts"]

def get_from_online(offset_date):
    params = {
        "offsetDate": get_timestamp(offset_date),
        "J_REQUEST_NAME": "RAccountsGetAllOnline"
    }
    return campreq(params)["accounts"]

def get_profile(account_id: int, account_name: str):
    params = {
        "accountId": int(account_id),
        "accountName": str(account_name),
        "J_REQUEST_NAME": "RAccountsGetProfile"
    }
    return campreq(params)

def get_story(account_id: int):
    params = {
        "accountId": int(account_id),
        "J_REQUEST_NAME": "RAccountsGetStory"
    }
    return campreq(params)

def follow(account_id: int, state: bool):
    params = {
        "accountId": int(account_id),
        "follow": bool(state),
        "J_REQUEST_NAME": "RAccountsFollowsChange"
    }
    return campreq(params)

def get_follows(account_id: int, followers: bool, offset: int):
    params = {
        "followsOfaAccountId": int(account_id),
        "followers": bool(followers),
        "offset": int(offset),
        "J_REQUEST_NAME": "RAccountsFollowsGetAll"
    }
    return campreq(params)["accounts"]

def get_rates(account_id: int, offset: int):
    params = {
        "accountId": int(account_id),
        "offset": int(offset),
        "J_REQUEST_NAME": "RAccountsRatesGetAll"
    }
    return campreq(params)["rates"]

def get_punishments(account_id: int, offset: int):
    params = {
        "accountId": int(account_id),
        "offset": int(offset),
        "J_REQUEST_NAME": "RAccountsPunishmentsGetAll"
    }
    return campreq(params)

def add_bl(account_id: int):
    params = {
        "accountId": int(account_id),
        "J_REQUEST_NAME": "RAccountsBlackListAdd"
    }
    return campreq(params)

def remove_bl(account_id: int):
    params = {
        "accountId": int(account_id),
        "J_REQUEST_NAME": "RAccountsBlackListRemove"
    }
    return campreq(params)

def check_bl(account_id: int):
    params = {
        "accountId": int(account_id),
        "J_REQUEST_NAME": "RAccountsBlackListCheck"
    }
    return campreq(params)["isInBlackList"]

def get_subscribed_fandoms(account_id: int, offset: int):
    params = {
        "accountId": int(account_id),
        "offset": int(offset),
        "J_REQUEST_NAME": "RFandomsGetAllSubscribed"
    }
    return campreq(params)["fandoms"]

def get_moderated_fandoms(account_id: int, offset: int):
    params = {
        "accountId": int(account_id),
        "offset": int(offset),
        "J_REQUEST_NAME": "RFandomsGetAllModerated"
    }
    return campreq(params)["fandoms"]

def get_activities(account_id: int, offset: int):
    params = {
        "accountId": int(account_id),
        "offset": int(offset),
        "fandomId": 0,
        "languageId": 0,
        "J_REQUEST_NAME": "RActivitiesGetAllForAccount"
    }
    return campreq(params)["userActivities"]

def get_rubrics(account_id: int, offset: int):
    params = {
        "ownerId": int(account_id),
        "offset": int(offset),
        "fandomId": 0,
        "languageId": 0,
        "J_REQUEST_NAME": "RRubricsGetAll"
    }
    return campreq(params)["rubrics"]

def report(account_id: int, comment: str):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsReport"
    }
    return campreq(params)

def get_publications(account_id: int, offset: int, count: int, fandom_id: int, fandom_ids: list, only_with_fandom: bool, important: bool, types: list, lang: int, tags: list):
    params = {
        "accountId": int(account_id),
        "offset": int(offset),
        "count": int(count),
        "fandomId": int(fandom_id),
        "fandomIds": list(fandom_ids),
        "onlyWithFandom": bool(only_with_fandom),
        "important": bool(important),
        "unitTypes": list(types),
        "languageId": int(lang),
        "tags": list(tags),
        "parentUnitId": 0,
        "drafts": False,
        "includeZeroLanguages": True,
        "includeModerationsBlock": True,
        "includeModerationsOther": True,
        "includeMultilingual": True,
        "order": 1,
        "appKey": None,
        "appSubKey": None,
        "J_REQUEST_NAME": "RPublicationsGetAll"
    }
    return campreq(params)["units"]

def admin_ban(account_id: int, comment: str, ban_time):
    params = {
        "accointId": int(account_id),
        "comment": str(comment),
        "banTime": get_deltastamp(ban_time),
        "J_REQUEST_NAME": "RAccountsAdminBan"
    }
    return campreq(params)

def admin_change_name(account_id: int, comment: str, name: str):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "name": str(name),
        "J_REQUEST_NAME": "RAccountsAdminChangeName"
    }
    return campreq(params)

def admin_effect_add(account_id: int, comment: str, index: int, end_date):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "effectIndex": int(index),
        "effectEndDate": get_timestamp(end_date),
        "J_REQUEST_NAME": "RAccountsAdminEffectAdd"
    }
    return campreq(params)

def admin_remove_description(account_id: int, comment: str):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsAdminRemoveDescription"
    }
    return campreq(params)

def admin_remove_status(account_id: int, comment: str):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsAdminRemoveStatus"
    }
    return campreq(params)

def admin_remove_background(account_id: int, comment: str):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsAdminRemoveBackground"
    }
    return campreq(params)

def admin_remove_avatar(account_id: int, comment: str):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsAdminRemoveAvatar"
    }
    return campreq(params)

def admin_remove_name(account_id: int, comment: str):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsAdminRemoveName"
    }
    return campreq(params)

def admin_remove_link(account_id: int, comment: str, index: int):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "index": int(index),
        "J_REQUEST_NAME": "RAccountsAdminRemoveLink"
    }
    return campreq(params)

def admin_recount_karma(account_id: int, comment: str):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsKarmaRecount"
    }
    return campreq(params)

def admin_recount_achievements(account_id: int, comment: str):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsAchievementsRecount"
    }
    return campreq(params)

def admin_clear_reports(account_id: int, comment: str):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsClearReports"
    }
    return campreq(params)

def admin_get_reports(account_id: int, offset: int):
    params = {
        "unitId": int(account_id),
        "offset": int(offset),
        "J_REQUEST_NAME": "RAccountsReportsGetAllForAccount"
    }
    return campreq(params)["reports"]

def admin_remove_moderator(account_id: int, comment: str, fandom_id: int, fandom_lang: int):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "J_REQUEST_NAME": "RFandomsAdminRemoveModerator"
    }
    return campreq(params)

def admin_change_viceroy(account_id: int, comment: str, fandom_id: int, fandom_lang: int):
    params = {
        "accountId": int(account_id),
        "comment": str(comment),
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "J_REQUEST_NAME": "RFandomsAdminViceroyAssign"
    }
    return campreq(params)

def admin_effect_remove(effect_id: int, comment: str):
    params = {
        "effectId": int(effect_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsAdminEffectRemove"
    }
    return campreq(params)

def admin_punishment_remove(punishment_id: int, comment: str):
    params = {
        "punishmentId": int(punishment_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsAdminPunishmentsRemove"
    }
    return campreq(params)