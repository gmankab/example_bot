import time

import pandas as pd

from data import *


# translate
def t(text, language):
    if language == Languages.default:
        return text
    elif text in translations[Languages.default]:
        return translations.loc[translations[Languages.default] == text][language].iloc[0]
    else:
        translate_to_all()


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


translations = pd.DataFrame()


def translate_to_all(text, add_lang_in_end=False):
    df = ''
    progress = 0
    print(f'translating "{text}" to all languages\n')
    for language in Languages.Supported.list:
        translate = text
        if add_lang_in_end:
            translate += ' ' + language
        print(f'\r{"#" * progress}{"-" * (107 - progress)} {progress}/106 {language}', end='')
        if language != Languages.default:
            translate = GoogleTranslator(source=Languages.default, target=language).translate(translate)
        df_to_add = pd.DataFrame({text: translate}, index=[0])
        if len(df):
            df = pd.concat([df, df_to_add], ignore_index=True)
        else:
            df = df_to_add
        progress += 1

    print(f'\r{"#" * progress}{"-" * (107 - progress)} {"done"}', end='')
    print(df)
    df.to_csv(r'data\translations.scv')


# df = pd.DataFrame({'language': Languages.Supported.list})

translate_to_all('your language is', True)
