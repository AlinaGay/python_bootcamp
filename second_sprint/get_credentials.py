# Напишите декоратор obfuscator
def obfuscator(func):
    def wrapper():
        result = func()
        result['name'] = (
            result['name'][0] + ('*' * (len(result['name']) - 2)) +
            result['name'][-1]
            )
        result['password'] = len(result['password']) * '*'
        return result
    return wrapper


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())
