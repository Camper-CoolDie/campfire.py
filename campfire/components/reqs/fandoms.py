from ..api import campreq, get_resource

def get(fandom_id: int, fandom_lang: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "accountLanguageId": 2,
        "J_REQUEST_NAME": "RFandomsGet"
    }
    return campreq(params)["fandom"]

def get_all(
        name: str,
        fandom_lang: int,
        offset: int,
        subscribed: int,
        category_id: int,
        params1: list,
        params2: list,
        params3: list,
        params4: list ):
    params = {
        "name": str(name),
        "subscribedStatus": int(subscribed),
        "languageId": int(fandom_lang),
        "categoryId": int(category_id),
        "offset": int(offset),
        "params1": list(params1),
        "params2": list(params2),
        "params3": list(params3),
        "params4": list(params4),
        "J_REQUEST_NAME": "RFandomsGetAll"
    }
    return campreq(params)["fandoms"]

def get_publications(
        fandom_id: int,
        fandom_lang: int,
        offset: int,
        count: int,
        fandom_ids: list,
        only_with_fandom: bool,
        important: bool,
        types: list,
        tags: list ):
    params = {
        "accountId": 0,
        "parentUnitId": 0,
        "offset": int(offset),
        "fandomId": int(fandom_id),
        "fandomIds": list(fandom_ids),
        "important": bool(important),
        "drafts": False,
        "includeZeroLanguages": True,
        "includeModerationsBlocks": True,
        "includeModerationsOther": True,
        "includeMultilingual": True,
        "unitTypes": list(types),
        "order": 1,
        "languageId": int(fandom_lang),
        "onlyWithFandom": bool(only_with_fandom),
        "count": int(count),
        "appKey": None,
        "appSubKey": None,
        "tags": list(tags),
        "J_REQUEST_NAME": "RPublicationsGetAll"
    }
    return campreq(params)["units"]

def suggest(name: str, note: str, avatar: bytes, background: bytes, category_id: int, closed: bool, params1: list, params2: list, params3: list, params4: list):
    avatar = get_resource(avatar)
    background = get_resource(background)
    
    params = {
        "name": str(name),
        "categoryId": int(category_id),
        "closed": bool(closed),
        "params1": list(params1),
        "params2": list(params2),
        "params3": list(params3),
        "params4": list(params4),
        "notes": str(note),
        "J_REQUEST_NAME": "RFandomsSuggest",
        "dataOutputBase64": [
            avatar,
            background
        ]
    }
    return campreq(params)

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
        "offset": int(offset),
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "J_REQUEST_NAME": "RFandomsSubscribersGetAll"
    }
    return campreq(params)["accounts"]

def get_chats(fandom_id: int, fandom_lang: int, offset: int):
    params = {
        "offset": int(offset),
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "J_REQUEST_NAME": "RChatsFandomGetAll"
    }
    return campreq(params)["chats"]

def get_activities(fandom_id: int, fandom_lang: int, offset: int):
    params = {
        "accountId": 0,
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "offset": int(offset),
        "J_REQUEST_NAME": "RActivitiesGetAllNotForAccount"
    }
    return campreq(params)["userActivities"]

def get_rubrics(fandom_id: int, fandom_lang: int, offset: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "ownerId": 0,
        "offset": int(offset),
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

# Moderator

def moderator_create_chat(fandom_id: int, fandom_lang: int, comment: str, name: str, text: str, avatar: bytes):
    avatar = get_resource(avatar)
    
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "name": str(name),
        "text": str(text),
        "comment": str(comment),
        "dataOutputBase64": [
            avatar
        ],
        "J_REQUEST_NAME": "RFandomsModerationChatCreate"
    }
    return campreq(params)

def moderator_change_chat_background(fandom_id: int, fandom_lang: int, comment: str, background: bytes):
    background = get_resource(background)
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationChangeImageBackground",
        "dataOutputBase64": [
            background
        ]
    }
    return campreq(params)

def moderator_add_link(fandom_id: int, fandom_lang: int, comment: str, title: str, url: str, icon: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "title": str(title),
        "url": str(url),
        "iconIndex": int(icon),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationLinkAdd"
    }
    return campreq(params)

def moderator_remove_link(comment: str, index: int):
    params = {
        "linkIndex": int(index),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationLinkRemove"
    }
    return campreq(params)

def moderator_change_link(fandom_id: int, fandom_lang: int, comment: str, index: int, title: str, url: str, icon: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "linkId": int(index),
        "title": str(title),
        "url": str(url),
        "iconIndex": int(icon),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationLinkChange"
    }
    return campreq(params)

def moderator_change_description(fandom_id: int, fandom_lang: int, comment: str, text: str):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "description": str(text),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationDescriptionChange"
    }
    return campreq(params)

def moderator_gallery_add(fandom_id: int, fandom_lang: int, comment: str, image: bytes):
    image = get_resource(image)
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationGalleryAdd",
        "dataOutputBase64": [
            image
        ]
    }
    return campreq(params)

def moderator_gallery_remove(fandom_id: int, fandom_lang: int, comment: str, image_id: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "imageId": int(image_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationGalleryRemove"
    }
    return campreq(params)

def moderator_set_names(fandom_id: int, fandom_lang: int, comment: str, names: list):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "names": list(names),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationNames"
    }
    return campreq(params)

def moderator_create_activity(fandom_id: int, fandom_lang: int, comment: str, name: str, description: str, account_id: int):
    params = {
        "accountId": int(account_id),
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "name": str(name),
        "description": str(description),
        "comment": str(comment),
        "J_REQUEST_NAME": "RActivitiesRelayRaceCreate"
    }
    return campreq(params)

def moderator_create_rubric(fandom_id: int, fandom_lang: int, comment: str, name: str, account_id: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "name": str(name),
        "ownerId": int(account_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RRubricsModerCreate"
    }
    return campreq(params)

# Admin

def admin_change_avatar(fandom_id: int, comment: str, image: bytes):
    image = get_resource(image)
    params = {
        "fandomId": int(fandom_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAdminChangeImage",
        "dataOutputBase64": [
            image
        ]
    }
    return campreq(params)

def admin_change_name(fandom_id: int, comment: str, name: str):
    params = {
        "fandomId": int(fandom_id),
        "name": str(name),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAdminChangeName"
    }
    return campreq(params)

def admin_close(fandom_id: int, comment: str, closed: bool):
    params = {
        "fandomId": int(fandom_id),
        "closed": bool(closed),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAdminClose"
    }
    return campreq(params)

def admin_remove_moderator(fandom_id: int, fandom_lang: int, comment: str, account_id: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "accountId": int(account_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAdminRemoveModerator"
    }
    return campreq(params)

def admin_change_viceroy(fandom_id: int, fandom_lang: int, comment: str, account_id: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "accountId": int(account_id),
        "comment": str(comment),
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

def admin_set_cof(fandom_id: int, comment: str, karma_cof: int):
    params = {
        "fandomId": int(fandom_id),
        "cof": int(float(karma_cof) * 100),
        "comment": str(comment),
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
        "categoryId": int(category_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAdminChangeCategory"
    }
    return campreq(params)

def admin_get_suggested(offset: int):
    params = {
        "offset": int(offset),
        "J_REQUEST_NAME": "RFandomsSuggestedGetAll"
    }
    return campreq(params)["fandoms"]

# FandomSuggested

def admin_suggest_get_info(fandom_id: int):
    params = {
        "fandomId": int(fandom_id),
        "J_REQUEST_NAME": "RFandomsSuggestedGet"
    }
    return campreq(params)

def admin_accept(fandom_id: int, comment: str, accepted: bool):
    params = {
        "fandomId": int(fandom_id),
        "accepted": bool(accepted),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAccept"
    }
    return campreq(params)

# FandomInfo

def get_info(fandom_id: int, fandom_lang: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "J_REQUEST_NAME": "RFandomsGetInfo"
    }
    return campreq(params)