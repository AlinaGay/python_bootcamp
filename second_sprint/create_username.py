from typing import Optional


class User:
    def __init__(
            self,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            username: Optional[str] = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # Опишите метод класса with_name.
    @classmethod
    def with_name(
        cls,
        first_name: str,
        last_name: str
    ):
        return User(first_name=first_name, last_name=last_name)

    # Опишите метод класса with_username.
    @classmethod
    def with_username(
        cls,
        username: str
    ):
        if not User.is_username_allowed(username):
            raise ValueError('Некорректное имя пользователя')
        return User(username=username)

    # Опишите статический метод класса is_username_allowed.
    @staticmethod
    def is_username_allowed(username: str):
        if username.startswith('admin'):
            return False
        else:
            return True

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'@{self.username}'


stas = User.with_name('Стас', 'Басов')
print(stas.full_name)

# Попробуем создать пользователя с "запрещённым" именем.
ne_stas = User.with_username('admin_nestas_anonymous')
print(ne_stas.full_name)
