from urllib import request
import argparse

from colorama import Fore
from colorama import Style

# print(f"{Fore.RED}Error{Style.RESET_ALL} This is {Fore.GREEN}{name}{Style.RESET_ALL}!")
def create_gitignore(language):
    try:
        language = language.capitalize()
        url = f"https://raw.githubusercontent.com/github/gitignore/master/{language}.gitignore"
        response = request.urlopen(url)
        data = response.read()
        text = data.decode("utf-8")
        with open(".gitignore", "w") as f:
            f.write(text)
        print(f"{Fore.GREEN}Success!:  .gitignore file created{Style.RESET_ALL}")

    except :
        print(f"{Fore.RED}Error!: try again.{Style.RESET_ALL} \n.gitignore file for {Fore.RED}{language}{Style.RESET_ALL} not found. \nYou are not connected to the internet or the language you entered is not supported yet. \nCheck out {Fore.GREEN}https://github.com/github/gitignore{Style.RESET_ALL} for list of available languages.")
            


def main():
    parser = argparse.ArgumentParser(
        description="CLI tool to create .gitignore files for your projects."
    )
    parser.add_argument(
        "language",
        type=str,
        help=f"The language you want your gitignore file for. \nCheck out {Fore.GREEN}https://github.com/github/gitignore{Style.RESET_ALL} for list of available languages. ",
    )

    args = parser.parse_args()
    create_gitignore(args.language)


if __name__ == "__main__":
    main()
