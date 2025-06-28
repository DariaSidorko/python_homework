
import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        pos_args = list(args) if args else "none"
        kw_args = dict(kwargs) if kwargs else "none"
        
        result = func(*args, **kwargs)
        
        logger.log(logging.INFO, f"function: {func.__name__} | "
                                 f"positional parameters: {pos_args} | "
                                 f"keyword parameters: {kw_args} | "
                                 f"return: {result}")
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def accepts_args(*args):
    return True

@logger_decorator
def accepts_kwargs(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    say_hello()
    accepts_args(1, 2, 3, "test")
    accepts_kwargs(a=1, b=2, name="Daria")
