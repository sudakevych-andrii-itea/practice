import datetime


class User:
    posts = []

    def __init__(self):
        self._current_user = None

    @property
    def current_user(self):
        return self._current_user

    @current_user.setter
    def current_user(self, value):
        assert isinstance(value, dict), f'{value}'
        self._current_user = value

    def add_post(self, post):
        if self._current_user:
            self.__class__.posts.append({'id': len(self.__class__.posts) + 1,
                                         'post': post,
                                         'auth': self._current_user['id'],
                                         'publication_date': datetime.datetime.now().strftime('%d-%m-%Y %H:%M')})

    @classmethod
    def get_posts(cls):
        return cls.posts


class Admin(User):
    def __init__(self):
        super().__init__()

    def get_users_posts_info(self, users):
        user_info = [{k: v for k, v in user.items() if k in ('id', 'registration_date')} for user in users]
        user_info = [{**user, 'posts': []} for user in user_info]
        print(user_info)
        for index, user in enumerate(user_info):
            for post in self.__class__.posts:
                if user['id'] == post['auth']:
                    user_info[index]['posts'].append({'id': post['id'], 'post': post['post']})

        return user_info
