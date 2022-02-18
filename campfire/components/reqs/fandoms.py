from ..api import campreq

def get(fandom_id: int, fandom_lang: int):
    params = {
        "fandomId": int(fandom_id),
        "languageId": int(fandom_lang),
        "accountLanguageId": 2,
        "J_REQUEST_NAME": "RFandomsGet"
    }
    return campreq(params)