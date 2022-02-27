# This file was generated automatically
# using other files prepared for generation

from ._abcollect import *

def get_comments(unit_id: int, offset, from_bottom: bool):
    params = {
        "unitId": int(unit_id),
        "offsetDate": get_timestamp(offset),
        "startFromBottom": bool(from_bottom),
        "old": False,
        "J_REQUEST_NAME": "RCommentsGetAll"
    }
    return campreq(params)["units"]

def comment(unit_id: int, text: str, sticker: int, voice, images: list, reply: int):
    params = {
        "unitId": int(unit_id),
        "text": str(text),
        "stickerId": int(sticker),
        "quoteId": int(reply),
        "watchPost": True,
        "J_REQUEST_NAME": "RCommentsCreate"
    }
    return campreq(params, FLAG_DATAOUTPUT, resources = ((voice, FLAG_RESOURCE_NO_REQUIRED), (images, FLAG_RESOURCE_LIST),))

def set_karma(unit_id: int, positive: bool, anonim: bool):
    params = {
        "unitId": int(unit_id),
        "up": bool(positive),
        "anon": bool(anonim),
        "userLanguage": 2,
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

def report(unit_id: int, comment: str):
    params = {
        "publicationId": int(unit_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RPublicationsReport"
    }
    return campreq(params)

def get_rates(unit_id: int, offset: int):
    params = {
        "unitId": int(unit_id),
        "offset": int(offset),
        "J_REQUEST_NAME": "RPostRatesGetAll"
    }
    return campreq(params)["rates"]

def get_history(unit_id: int, offset: int):
    params = {
        "unitId": int(unit_id),
        "offset": int(offset),
        "J_REQUEST_NAME": "RPublicationsHistoryGetAll"
    }
    return campreq(params)["history"]

def get_reports(unit_id: int, offset: int):
    params = {
        "unitId": int(unit_id),
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

def moderator_block(unit_id: int, comment: str, block_last_units: bool, ban_time, block_in_app: bool):
    params = {
        "unitId": int(unit_id),
        "comment": str(comment),
        "blockLastUnits": bool(block_last_units),
        "blockTime": get_deltastamp(ban_time),
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

def get_post(unit_id: int):
    params = {
        "unitId": int(unit_id),
        "J_REQUEST_NAME": "RPostGet"
    }
    return campreq(params)["unit"]

def post_get_from_feed(offset, important: bool, languages: list, no_karma_category: bool, karma_category: bool, categories: list):
    params = {
        "offsetDate": get_timestamp(offset),
        "importantOnly": bool(important),
        "languagesId": list(languages),
        "noKarmaCategory": bool(no_karma_category),
        "karmaCategory": bool(karma_category),
        "categoriesId": list(categories),
        "noSubscribers": True,
        "J_REQUEST_NAME": "RPostFeedGetAll"
    }
    return campreq(params)["units"]

def post_get_from_subscribers(offset, category: int):
    params = {
        "offsetDate": get_timestamp(offset),
        "categoryId": int(category),
        "J_REQUEST_NAME": "RPostFeedGetAllSubscribe"
    }
    return campreq(params)["units"]

def post_change_fandom(unit_id: int, fandom_id: int, fandom_lang: int):
    params = {
        "unitId": int(unit_id),
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "comment": "",
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

def post_no_close(unit_id: int):
    params = {
        "unitId": int(unit_id),
        "J_REQUEST_NAME": "RPostCloseNo"
    }
    return campreq(params)

def post_make_multilingual(unit_id: int):
    params = {
        "unitId": int(unit_id),
        "J_REQUEST_NAME": "RPostMakeMultilingual"
    }
    return campreq(params)

def post_make_no_multilingual(unit_id: int):
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

def post_pin_account(unit_id: int):
    params = {
        "unitId": int(unit_id),
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

def moderator_post_no_close(unit_id: int, comment: str):
    params = {
        "unitId": int(unit_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RPostCloseNoModerator"
    }
    return campreq(params)

def moderator_post_make_no_multilingual(unit_id: int, comment: str):
    params = {
        "unitId": int(unit_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RPostMakeMultilingualModeratorNot"
    }
    return campreq(params)

def moderator_post_important(unit_id: int, comment: str, important: bool):
    params = {
        "unitId": int(unit_id),
        "comment": str(comment),
        "important": bool(important),
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

def moderator_post_pin_fandom(unit_id: int, comment: str, fandom_id: int, fandom_lang: int):
    params = {
        "unitId": int(unit_id),
        "comment": str(comment),
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "J_REQUEST_NAME": "RPostPinFandom"
    }
    return campreq(params)

def moderator_post_make_moderator(unit_id: int, comment: str):
    params = {
        "unitId": int(unit_id),
        "comment": str(comment),
        "J_REQUEST_NAME": "RFandomsAdminMakeModerator"
    }
    return campreq(params)

def get_comment(parent_id: int, comment_id: int):
    params = {
        "parentPublicationId": int(parent_id),
        "commentId": int(comment_id),
        "J_REQUEST_NAME": "RCommentGet"
    }
    return campreq(params)["comment"]

def comment_change(comment_id: int, text: str, reply: int):
    params = {
        "commentId": int(comment_id),
        "text": str(text),
        "quoteId": int(reply),
        "J_REQUEST_NAME": "RCommentsChange"
    }
    return campreq(params)