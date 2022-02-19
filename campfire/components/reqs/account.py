from ..api import campreq, get_timestamp

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
    return campreq(params)

def get_from_online(offset_date: int):
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
        "offset": int(offset),
        "followers": bool(followers),
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
    return campreq(params)["punishments"]

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
        "fandomId": 0,
        "languageId": 0,
        "offset": int(offset),
        "J_REQUEST_NAME": "RActivitiesGetAllForAccount"
    }
    return campreq(params)["userActivities"]

def get_rubrics(account_id: int, offset: int):
    params = {
        "fandomId": 0,
        "languageId": 0,
        "ownerId": int(account_id),
        "offset": int(offset),
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

# AccountEffect

def admin_effect_remove(effect_id: int, comment: str):
    params = {
        "effectId": int(effect_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsAdminEffectRemove"
    }
    return campreq(params)

# AccountPunishment

def admin_punishment_remove(punishment_id: int, comment: str):
    params = {
        "punishmentId": int(punishment_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RAccountsAdminPunishmentsRemove"
    }
    return campreq(params)