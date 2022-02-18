from ..api import campreq, get_resources

def get_comments(unit_id: int, offset: int = 0, from_bottom: bool = False):
    params = {
        "unitId": int(unit_id),
        "offsetDate": int(offset),
        "old": False,
        "startFromBottom": bool(from_bottom),
        "J_REQUEST_NAME": "RCommentsGetAll"
    }
    return campreq(params)["units"]

def comment(unit_id: int, text: str, sticker: int = 0, images: list = [], reply: int = 0):
    res_images = [None] + get_resources(images)
    
    params = {
        "unitId": int(unit_id),
        "text": str(text),
        "parentCommentId": int(reply),
        "watchPost": True,
        "quoteId": int(reply),
        "stickerId": int(sticker),
        "J_REQUEST_NAME": "RCommentsCreate",
        "dataOutputBase64": res_images
    }
    return campreq(params)["comment"]

def set_karma(unit_id: int, positive: bool = True, anonim: bool = False):
    params = {
        "unitId": int(unit_id),
        "up": bool(positive),
        "userLanguage": 2,
        "anon": bool(anonim),
        "J_REQUEST_NAME": "RPublicationsKarmaAdd"
    }
    return campreq(params)

def reaction_add(unit_id: int, index: int):
    params = {
        "unitId": int(unit_id),
        "reactionIndex": int(index),
        "J_REQUEST_NAME": "RPublicationsReactionAdd"
    }
    return campreq(params)

def reaction_remove(unit_id: int, index: int):
    params = {
        "unitId": int(unit_id),
        "reactionIndex": int(index),
        "J_REQUEST_NAME": "RPublicationsReactionRemove"
    }
    return campreq(params)

def reaction_get(unit_id: int, index: int):
    params = {
        "unitId": int(unit_id),
        "reactionIndex": int(index),
        "J_REQUEST_NAME": "RPublicationsReactionGetAccounts"
    }
    return campreq(params)["accounts"]

def report(unit_id: int, text: str):
    params = {
        "unitId": int(unit_id),
        "comment": str(text),
        "J_REQUEST_NAME": "RPublicationsReport"
    }
    return campreq(params)

def get_rates(unit_id: int, offset: int):
    params = {
        "unitId": int(unit_id),
        "offset": int(offset),
        "J_REQUEST_NAME": "RPostRatesGetAll"
    }
    return campreq(params)

def get_history(unit_id: int, offset: int):
    params = {
        "unitId": int(unit_id),
        "offset": int(offset),
        "J_REQUEST_NAME": "RPublicationsHistoryGetAll"
    }
    return campreq(params)["history"]

def get_reports(unit_id: int, offset: int):
    params = {
        "publicationId": int(unit_id),
        "offset": int(offset),
        "J_REQUEST_NAME": "RPublicationsReportsGetAll"
    }
    return campreq(params)["reports"]

def remove(unit_id: int):
    params = {
        "unitId": int(unit_id),
        "J_REQUEST_NAME": "RPublicationsRemove"
    }
    return campreq(params)

def moderator_block(unit_id: int, comment: str, block_last_publications: bool = False, ban_time: int = -1, block_in_app: bool = False):
    params = {
        "unitId": int(unit_id),
        "blockTime": int(ban_time),
        "blockLastUnits": bool(block_last_publications),
        "comment": str(comment),
        "blockInApp": bool(block_in_app),
        "userLanguageId": 2,
        "J_REQUEST_NAME": "RFandomsModerationBlock"
    }
    return campreq(params)

def moderator_clear_reports(unit_id: int):
    params = {
        "unitId": int(unit_id),
        "J_REQUEST_NAME": "RPublicationsAdminClearReports"
    }
    return campreq(params)

# Post

def get_post(post_id):
    params = {
        "unitId": int(post_id),
        "J_REQUEST_NAME": "RPostGet"
    }
    return campreq(params)["unit"]

def get_posts_from_feed(offset: int = 0, languages: list = [2], subscribes: bool = False, important: int = False):
    if subscribes:
        params = {
            "offsetDate": int(offset),
            "categoryId": 0,
            "J_REQUEST_NAME": "RPostFeedGetAllSubscribe"
        }
    else:
        params = {
            "offsetDate": int(offset),
            "importantOnly": bool(important),
            "languagesId": list(languages),
            "categoriesId": [],
            "karmaCategory": 0,
            "noSubscribers": True,
            "noKarmaCategory": True,
            "J_REQUEST_NAME": "RPostFeedGetAll"
        }
    return campreq(params)["units"]

def post_change_fandom(unit_id: int, comment: str, fandom_id: int, fandom_lang: int = 2):
    params = {
        "unitId": int(unit_id),
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": str(comment),
        "J_REQUEST_NAME": "RPostChangeFandom"
    }
    return campreq(params)

def post_to_drafts(unit_id: int):
    params = {
        "unitId": int(unit_id),
        "J_REQUEST_NAME": "RPostToDrafts"
    }
    return campreq(params)

def post_close(unit_id: int):
    params = {
        "unitId": int(unit_id),
        "J_REQUEST_NAME": "RPostClose"
    }
    return campreq(params)

def post_close_no(unit_id: int):
    params = {
        "unitId": int(unit_id),
        "J_REQUEST_NAME": "RPostCloseNo"
    }
    return campreq(params)

def post_set_multilingual(unit_id: int):
    params = {
        "unitId": int(unit_id),
        "J_REQUEST_NAME": "RPostMakeMultilingual"
    }
    return campreq(params)

def post_unset_multilingual(unit_id: int):
    params = {
        "unitId": int(unit_id),
        "J_REQUEST_NAME": "RPostMakeMultilingualNot"
    }
    return campreq(params)

def post_notify_followers(unit_id: int):
    params = {
        "unitId": int(unit_id),
        "J_REQUEST_NAME": "RPostNotifyFollowers"
    }
    return campreq(params)

def post_pin_to_account(post_id: int):
    params = {
        "postId": int(post_id),
        "J_REQUEST_NAME": "RPostPinAccount"
    }
    return campreq(params)

def moderator_post_close(unit_id: int, comment: str):
    params = {
        "unitId": int(unit_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RPostCloseModerator"
    }
    return campreq(params)

def moderator_post_close_no(unit_id: int, comment: str):
    params = {
        "unitId": int(unit_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RPostCloseNoModerator"
    }
    return campreq(params)

def moderator_post_unset_multilingual(unit_id: int, comment: str):
    params = {
        "unitId": int(unit_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RPostMakeMultilingualModeratorNot"
    }
    return campreq(params)

def moderator_post_set_important(unit_id: int, comment: str, important: bool = True):
    params = {
        "unitId": int(unit_id),
        "important": bool(important),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationImportant"
    }
    return campreq(params)

def moderator_post_to_drafts(unit_id: int, comment: str):
    params = {
        "unitId": int(unit_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsModerationToDrafts"
    }
    return campreq(params)

def moderator_post_pin_to_fandom(post_id: int, fandom_id: int, fandom_lang: int, comment: str):
    params = {
        "postId": int(post_id),
        "comment": str(comment),
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "J_REQUEST_NAME": "RPostPinFandom"
    }
    return campreq(params)

def admin_post_make_moderator(unit_id: int, comment: str):
    params = {
        "unitId": int(unit_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAdminMakeModerator"
    }
    return campreq(params)

# Comment

def get_comment(parent_id: int, unit_id: int):
    params = {
        "parentPublicationId": int(parent_id),
        "commentId": int(unit_id),
        "J_REQUEST_NAME": "RCommentGet"
    }
    return campreq(params)["comment"]

def comment_change(unit_id: int, text: str, reply: int):
    params = {
        "commentId": int(unit_id),
        "quoteId": int(reply),
        "text": str(text),
        "J_REQUEST_NAME": "RCommentsChange"
    }
    return campreq(params)