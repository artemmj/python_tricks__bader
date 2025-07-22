def validate_name(name: str):
    if len(name) < 10:
        raise NameToShortError

class BaseCustomError(ValueError):
    pass

class NameToShortError(BaseCustomError):
    pass

class NameToLongError(BaseCustomError):
    pass

def handle_validation_error(err: BaseCustomError):
    return err

try:
    validate_name('qweasdzxc')
except BaseCustomError as err:
    handle_validation_error(err)
