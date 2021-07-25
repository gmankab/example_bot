from data import *


# translate
def t(text, language):
    if language == Languages.default:
        return text
    else:
        return GoogleTranslator(source=Languages.default, target=language).translate(text)


def change_language(language, username):
    if username in Languages.users_list:
        index = Languages.users.loc[Languages.users['user'] == username].index[0]
        Languages.users['language'][index] = language
        Languages.users.to_csv(r'data\users.csv', index=False)
    else:
        language_user_set(language, username)


def language_user_set(language, username):
    if language in Languages.Supported.abbreviations:
        language = Languages.Supported.dict[language]
    else:
        language = 'english'
    Languages.users = Languages.users.append({'user': username, 'language': language}, ignore_index=True)
    Languages.users.to_csv(r'data\users.csv', index=False)
    Languages.users_list = list(Languages.users['user'])
