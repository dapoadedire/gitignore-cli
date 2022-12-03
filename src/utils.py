from urllib import request
from bs4 import BeautifulSoup
import re
import difflib

# URL on the Github where the csv files are stored
gitignore_url = 'https://github.com/github/gitignore'

result = request.urlopen(gitignore_url)
data = result.read()
text = data.decode("utf-8")
soup = BeautifulSoup(text, 'html.parser')
gitignorefiles = soup.find_all(class_="Link--primary",title=re.compile("\.gitignore$"))

filenames = [ ]
for i in gitignorefiles:
        filenames.append(i.extract().get_text())
# print(filenames)

known_languages = [filename.split(".")[0] for filename in filenames]
# print(known_languages)
def check_typo(language):
    """ check if there is a word similar to language """
    return len(difflib.get_close_matches(language, known_languages)) > 0

def get_most_similar_languages(language, limit=3):
    """ get languages similar to the language passed in """
    return difflib.get_close_matches(language, known_languages, limit)