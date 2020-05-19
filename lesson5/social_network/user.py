import datetime
import shelve


class User:

    def __init__(self, current_user):
        self._current_user = current_user

    @property
    def current_user(self):
        return self._current_user

    @current_user.setter
    def current_user(self, value):
        self._current_user = value

    def add_post(self, post):
        if self._current_user:
            posts_dict = {
                'post': post,
                'auth': self._current_user,
                'publication_date': datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
            }
            with shelve.open('posts') as posts:
                posts_dict.update(post_id=f'{len(posts) + 1}')
                posts[f'{len(posts) + 1}'] = posts_dict

    @staticmethod
    def get_posts():
        with shelve.open('posts') as posts:
            return [post for post in posts.items()]


class Admin(User):
    def __init__(self, current_user):
        super().__init__(current_user)

    @staticmethod
    def get_users_posts_info():
        with shelve.open('users') as users:
            user_info = [{k: v for k, v in user.items() if k in ('user_id', 'registration_date')} for user in users.values()]
            user_info = [{**user, 'posts': []} for user in user_info]

        with shelve.open('posts') as posts:
            for index, user in enumerate(user_info):
                for post in posts.values():
                    if user['user_id'] == post['auth']:
                        user_info[index]['posts'].append({'post_id': post['post_id'], 'post': post['post']})

        return user_info
