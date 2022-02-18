from ...reqs import publications
from .. import main

class Comment(main._all["publication"]):
    __slots__ = (
        "images",
        "sticker",
        "sticker_image",
        "reactions",
        "is_changed",
        "text",
        
        "quote_id",
        "quote_text",
        "quote_images",
        "quote_sticker",
        "quote_sticker_image",
        "quote_author_name"
    )
    
    def __init__(self, content):
        super(Comment, self).__init__(content)
        
        self.images = content["jsonDB"]["imageIdArray"]
        self.sticker = content["jsonDB"]["stickerId"]
        self.sticker_image = content["jsonDB"]["stickerImageId"]
        self.reactions = content["jsonDB"]["reactions"]
        self.is_changed = content["jsonDB"]["changed"]
        self.text = content["jsonDB"]["J_TEXT"]
        
        self.quote_id = content["jsonDB"]["quoteId"]
        self.quote_text = content["jsonDB"]["quoteText"]
        self.quote_images = content["jsonDB"]["quoteImages"]
        self.quote_sticker = content["jsonDB"]["quoteStickerId"]
        self.quote_sticker_image = content["jsonDB"]["quoteStickerImageId"]
        if "quoteCreatorName" in content["jsonDB"]:
            self.quote_author_name = content["jsonDB"]["quoteCreatorName"]
        else:
            self.quote_author_name = None
    
    @staticmethod
    def get(parent_id: int, unit_id: int):
        return Comment(publications.get_comment(parent_id, unit_id))
    
    def reply(self, text: str, *, sticker: int = 0, images: list = []):
        return Comment(publications.comment(self.parent_id, text, sticker, images, self.id))
    
    # Self-actions
    
    def change(self, text: str, *, reply: int = -1):
        reply = int(reply)
        return publications.comment_change(self.id, text, self.quote_id if reply == -1 else reply)

main._all["comment"] = Comment