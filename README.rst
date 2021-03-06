Campfire API
==============

.. image:: https://readthedocs.org/projects/campfirepy/badge/?version=latest
    :target: https://campfirepy.readthedocs.io/ru/latest/?badge=latest
    :alt: Documentation Status

Модуль, основанный на `CampfireAPI <https://github.com/ZeonXX/CampfireApi>`_ для соцсети Campfire.

Документация
--------------

Для некоторых запросов на сервер Campfire необходимо указывать логин-токен. Вы заранее должны иметь свой аккаунт в Campfire и его емэйл и пароль, чтобы иметь доступ к некоторым функциям.
Пример простой программы:

.. code:: py
    
    import campfire
    campfire.auth("емэйл", "пароль")
    post = campfire.Post.get(4525600)
    print(post.get_comments()[0].text)

Эта программа сделала первый запрос на сервер, который получает информацию о посте 4525600, а во втором запросе сервер отправил список комментариев этого поста.
В консоль был выведен текст первого комментария.

Документация для проекта существует на `Readthedocs <https://campfirepy.readthedocs.io/ru/latest/>`_.
