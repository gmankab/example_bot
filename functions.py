from data import *


# translate
def t(text, language):
    if text in list(Langs.translations.columns):
        return Langs.translations[text][Langs.index[language]]
    else:
        print(f'error: can\'t find "{text}" in translations df')
        translate_to_all(text)
        return text + ' (translate error)'


def set_language(username, language):
    Users.langs[username] = language
    Users.langs.to_csv(r'data\users.csv', index=False)
    Users.list = list(Users.langs.columns)


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
