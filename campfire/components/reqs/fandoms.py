# This file was generated automatically
# using other files prepared for generation

from ._abcollect import *

def get(fandom_id: int, fandom_lang: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "accountLanguageId": 2,
        "J_REQUEST_NAME": "RFandomsGet"
    }
    return campreq(params)["fandom"]

def get_all(name: str, lang: int, offset: int, subscribed: int, category_id: int, params1: list, params2: list, params3: list, params4: list):
    params = {
        "name": str(name),
        "languageId": int(lang),
        "offset": int(offset),
        "subscribedStatus": int(subscribed),
        "categoryId": int(category_id),
        "params1": list(params1),
        "params2": list(params2),
        "params3": list(params3),
        "params4": list(params4),
        "J_REQUEST_NAME": "RFandomsGetAll"
    }
    return campreq(params)["fandoms"]

def get_publications(fandom_id: int, fandom_lang: int, offset: int, count: int, fandom_ids: list, only_with_fandom: bool, important: bool, types: list, tags: list):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "offset": int(offset),
        "count": int(count),
        "fandomIds": list(fandom_ids),
        "onlyWithFandom": bool(only_with_fandom),
        "important": bool(important),
        "unitTypes": list(types),
        "tags": list(tags),
        "accountId": 0,
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

def suggest(name: str, note: str, avatar, background, category_id: int, closed: bool, params1: list, params2: list, params3: list, params4: list):
    params = {
        "name": str(name),
        "notes": str(note),
        "categoryId": int(category_id),
        "closed": bool(closed),
        "params1": list(params1),
        "params2": list(params2),
        "params3": list(params3),
        "params4": list(params4),
        "J_REQUEST_NAME": "RFandomsSuggest"
    }
    return campreq(params, FLAG_DATAOUTPUT, resources = ((avatar, FLAG_RESOURCE_REQUIRED), (background, FLAG_RESOURCE_REQUIRED),))

def subscribe(fandom_id: int, fandom_lang: int, subscribed: int, important: bool):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "subscriptionType": int(subscribed),
        "notifyImportant": bool(important),
        "J_REQUEST_NAME": "RFandomsSubscribeChange"
    }
    return campreq(params)

def get_subscribers(fandom_id: int, fandom_lang: int, offset: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "offset": int(offset),
        "J_REQUEST_NAME": "RFandomsSubscribersGetAll"
    }
    return campreq(params)["accounts"]

def get_chats(fandom_id: int, fandom_lang: int, offset: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "offset": int(offset),
        "J_REQUEST_NAME": "RChatsFandomGetAll"
    }
    return campreq(params)["chats"]

def get_activities(fandom_id: int, fandom_lang: int, offset: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "offset": int(offset),
        "accountId": 0,
        "J_REQUEST_NAME": "RActivitiesGetAllNotForAccount"
    }
    return campreq(params)["userActivities"]

def get_rubrics(fandom_id: int, fandom_lang: int, offset: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "offset": int(offset),
        "ownerId": 0,
        "J_REQUEST_NAME": "RRubricsGetAll"
    }
    return campreq(params)["rubrics"]

def add_bl(fandom_id: int):
    params = {
        "fandomId": int(fandom_id),
        "J_REQUEST_NAME": "RFandomsBlackListAdd"
    }
    return campreq(params)

def remove_bl(fandom_id: int):
    params = {
        "fandomId": int(fandom_id),
        "J_REQUEST_NAME": "RFandomsBlackListRemove"
    }
    return campreq(params)

def check_bl(fandom_id: int):
    params = {
        "fandomId": int(fandom_id),
        "J_REQUEST_NAME": "RFandomsBlackListContains"
    }
    return campreq(params)["contains"]

def moderator_create_chat(fandom_id: int, fandom_lang: int, comment: str, name: str, text: str, avatar):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "name": str(name),
        "text": str(text),
        "J_REQUEST_NAME": "RFandomsModerationChatCreate"
    }
    return campreq(params, FLAG_DATAOUTPUT, resources = ((avatar, FLAG_RESOURCE_REQUIRED),))

def moderator_change_chat_background(fandom_id: int, fandom_lang: int, comment: str, background):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationChangeImageBackground"
    }
    return campreq(params, FLAG_DATAOUTPUT, resources = ((background, FLAG_RESOURCE_REQUIRED),))

def moderator_add_link(fandom_id: int, fandom_lang: int, comment: str, title: str, url: str, icon: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "title": str(title),
        "url": str(url),
        "iconIndex": int(icon),
        "J_REQUEST_NAME": "RFandomsModerationLinkAdd"
    }
    return campreq(params)

def moderator_change_link(fandom_id: int, fandom_lang: int, comment: str, link_id: int, title: str, url: str, icon: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "linkId": int(link_id),
        "title": str(title),
        "url": str(url),
        "iconIndex": int(icon),
        "J_REQUEST_NAME": "RFandomsModerationLinkChange"
    }
    return campreq(params)

def moderator_remove_link(link_id: int, comment: str):
    params = {
        "linkIndex": int(link_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationLinkRemove"
    }
    return campreq(params)

def moderator_change_description(fandom_id: int, fandom_lang: int, comment: str, description: str):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "description": str(description),
        "J_REQUEST_NAME": "RFandomsModerationDescriptionChange"
    }
    return campreq(params)

def moderator_gallery_add(fandom_id: int, fandom_lang: int, comment: str, image):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationGalleryAdd"
    }
    return campreq(params, FLAG_DATAOUTPUT, resources = ((image, FLAG_RESOURCE_REQUIRED),))

def moderator_gallery_remove(fandom_id: int, fandom_lang: int, comment: str, image_id: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "imageId": int(image_id),
        "J_REQUEST_NAME": "RFandomsModerationGalleryRemove"
    }
    return campreq(params)

def moderator_set_names(fandom_id: int, fandom_lang: int, comment: str, names: list):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "names": list(names),
        "J_REQUEST_NAME": "RFandomsModerationNames"
    }
    return campreq(params)

def moderator_create_activity(fandom_id: int, fandom_lang: int, comment: str, name: str, description: str, account_id: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "name": str(name),
        "description": str(description),
        "accountId": int(account_id),
        "J_REQUEST_NAME": "RActivitiesRelayRaceCreate"
    }
    return campreq(params)

def moderator_create_rubric(fandom_id: int, fandom_lang: int, comment: str, name: str, owner_id: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "name": str(name),
        "ownerId": int(owner_id),
        "J_REQUEST_NAME": "RRubricsModerCreate"
    }
    return campreq(params)

def admin_change_avatar(fandom_id: int, comment: str, avatar):
    params = {
        "fandomId": int(fandom_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAdminChangeImage"
    }
    return campreq(params, FLAG_DATAOUTPUT, resources = ((avatar, FLAG_RESOURCE_REQUIRED),))

def admin_change_name(fandom_id: int, comment: str, name: str):
    params = {
        "fandomId": int(fandom_id),
        "comment": str(comment),
        "name": str(name),
        "J_REQUEST_NAME": "RFandomsAdminChangeName"
    }
    return campreq(params)

def admin_close(fandom_id: int, comment: str, closed: bool):
    params = {
        "fandomId": int(fandom_id),
        "comment": str(comment),
        "closed": bool(closed),
        "J_REQUEST_NAME": "RFandomsAdminClose"
    }
    return campreq(params)

def admin_remove_moderator(fandom_id: int, fandom_lang: int, comment: str, account_id: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "accountId": int(account_id),
        "J_REQUEST_NAME": "RFandomsAdminRemoveModerator"
    }
    return campreq(params)

def admin_change_viceroy(fandom_id: int, fandom_lang: int, comment: str, account_id: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "accountId": int(account_id),
        "J_REQUEST_NAME": "RFandomsAdminViceroyAssign"
    }
    return campreq(params)

def admin_remove_viceroy(fandom_id: int, fandom_lang: int, comment: str):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAdminViceroyRemove"
    }
    return campreq(params)

def admin_set_cof(fandom_id: int, comment: str, cof: int):
    params = {
        "fandomId": int(fandom_id),
        "comment": str(comment),
        "cof": int(cof),
        "J_REQUEST_NAME": "RFandomsAdminSetCof"
    }
    return campreq(params)

def admin_remove(fandom_id: int, comment: str):
    params = {
        "fandomId": int(fandom_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAdminRemove"
    }
    return campreq(params)

def admin_change_category(fandom_id: int, comment: str, category_id: int):
    params = {
        "fandomId": int(fandom_id),
        "comment": str(comment),
        "categoryId": int(category_id),
        "J_REQUEST_NAME": "RFandomsAdminChangeCategory"
    }
    return campreq(params)

def admin_get_all_suggested(offset: int):
    params = {
        "offset": int(offset),
        "J_REQUEST_NAME": "RFandomsSuggestedGetAll"
    }
    return campreq(params)["fandoms"]

def admin_suggest_get_info(fandom_id: int):
    params = {
        "fandomId": int(fandom_id),
        "J_REQUEST_NAME": "RFandomsSuggestedGet"
    }
    return campreq(params)

def admin_suggest_accept(fandom_id: int, accepted: bool, comment: str):
    params = {
        "fandomId": int(fandom_id),
        "accepted": bool(accepted),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAdminAccept"
    }
    return campreq(params)

def get_info(fandom_id: int, fandom_lang: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "J_REQUEST_NAME": "RFandomsGetInfo"
    }
    return campreq(params)