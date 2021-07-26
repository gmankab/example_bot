from data import *


# translate
def t(text, language):
    if text in :
        return text
    elif text in translations[Langs.default]:
        return translations.loc[translations[Langs.default] == text][language].iloc[0]
    else:
        translate_to_all()


def change_language(language, username):
    if username in Users.list:
        index = Users.df.loc[Users.df['user'] == username].index[0]
        Users.df['language'][index] = language
        Users.df.to_csv(r'data\users.csv', index=False)
        Users.langs[username] = language
    else:
        language_user_set(language, username)


def language_user_set(language, username):
    if language in Langs.abbreviations:
        language = Langs.dict[language]
    else:
        language = 'english'
    Langs.users = Langs.users.append({'user': username, 'language': language}, ignore_index=True)
    Langs.users.to_csv(r'data\users.csv', index=False)
    Langs.users_list = list(Langs.users['user'])


def translate_to_all(text, add_lang_in_end=False):
    df = ''
    progress = 0
    print(f'translating "{text}" to all languages\n')
    for language in Langs.list:
        translate = text
        if add_lang_in_end:
            translate += ' ' + language
        print(f'\r{"#" * progress}{"-" * (107 - progress)} {progress}/106 {language}', end='')
        if language != Langs.default:
            translate = GoogleTranslator(source=Langs.default, target=language).translate(translate)
        df_to_add = pd.DataFrame({text: translate}, index=[0])
        if len(df):
            df = pd.concat([df, df_to_add], ignore_index=True)
        else:
            df = df_to_add
        progress += 1

    print(f'\r{"#" * progress}{"-" * (107 - progress)} {"106/106 done"}')
    translations = pd.concat([Langs.translations, df], axis=1)
    translations.to_csv(r'data\translations.csv', index=False)


@dataclass()
class Get:
    @staticmethod
    def language_indexes():
        lang_index = 0
        for i in GoogleTranslator.get_supported_languages():
            Langs.index[i] = lang_index
            lang_index += 1

    language_indexes()
