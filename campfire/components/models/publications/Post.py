from ...reqs import publications
from .. import main

class Post(main._all["publication"]):
    """
    Имитирует объект поста.
    """
    
    __slots__ = (
        "pages",
        "best_comment",
        "rubric_id",
        "rubric_name"
    )
    
    def __init__(self, content):
        """
        Создать класс Post.
        
        content: :class:`dict`
            Словарь, который сервер Campfire отправляет для создания объекта поста.
        """
        
        super(Post, self).__init__(content)
        
        self.pages = content["jsonDB"]["J_PAGES"] # list::dict
        if content["bestComment"] != None:
            self.best_comment = main._all["comment"](content["bestComment"])
        else:
            self.best_comment = None
        
        self.rubric_id = content["rubricId"]
        self.rubric_name = content["rubricName"]
    
    @staticmethod
    def get(post_id: int):
        """
        Создать класс Post с помощью его идентификатора.
        
        post_id: :class:`int`
            Айди поста.
        
        Возвращает
        
        :class:`Post`
            Объект поста.
        """
        
        return Post(publications.get_post(post_id))
    
    @staticmethod
    def get_from_feed(offset: int = 0, languages: list = [2], subscribes: bool = False, *, important: int = False):
        """
        Получить посты из ленты.
        
        offset: :class:`int`
            Дата создания последнего поста в миллисекундах.
        languages: :class:`list[int]`
            Лист с языками, которые будут иметь посты из ленты.
        subscribes: :class:`bool`
            Если значение верно, то посты из ленты будут из категории "Подписки".
        important: :class:`bool`
            Только важные посты.
        
        Возвращает
        
        :class:`list[Post]`
            Посты из ленты.
        """
        
        posts = publications.get_posts_from_feed(offset, languages, subscribes, important)
        return [ Post(post) for post in posts ]
    
    # Self-actions
    
    def change_fandom(self, fandom_id: int, fandom_lang: int = 2):
        return publications.post_change_fandom(self.id, "", fandom_id, fandom_lang)
    
    def to_drafts(self):
        return publications.post_to_drafts(self.id)
    
    def close(self):
        return publications.post_close(self.id)
    
    def no_close(self):
        return publications.post_close_no(self.id)
    
    def set_multilingual(self):
        return publications.post_set_multilingual(self.id)
    
    def unset_multilingual(self):
        return publications.post_unset_multilingual(self.id)
    
    def notify_followers(self):
        return publications.post_notify_followers(self.id)
    
    def pin_to_account(self):
        return publications.post_pin_to_account(self.id)
    
    # Moderator
    
    def moderator_close(self, comment: str):
        return publications.moderator_post_close(self.id, comment)
    
    def moderator_no_close(self, comment: str):
        return publications.moderator_post_close_no(self.id, comment)
    
    def moderator_unset_multilingual(self, comment: str):
        return publications.moderator_post_unset_multilingual(self.id, comment)
    
    def moderator_set_important(self, comment: str, important: bool = True):
        return publications.moderator_post_set_important(self.id, comment, important)
    
    def moderator_to_drafts(self, comment: str):
        return publications.moderator_post_to_drafts(self.id, comment)
    
    def moderator_pin_to_fandom(self, comment: str):
        return publications.moderator_post_pin_to_fandom(self.id, self.fandom_id, self.fandom_lang, comment)
    
    def admin_change_fandom(self, comment: str, fandom_id: int, fandom_lang: int = 2):
        return publications.post_change_fandom(self.id, comment, fandom_id, fandom_lang)
    
    def admin_make_moderator(self, comment: str):
        return publications.admin_post_make_moderator(self.id, comment)

main._all["post"] = Post