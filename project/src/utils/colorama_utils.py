from colorama import init, Fore, Style

init()

def color(string: str, color: str):
    return getattr(Fore, color.upper()) + f"{string}" + Style.RESET_ALL