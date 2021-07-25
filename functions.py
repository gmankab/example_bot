from data import *


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


# translate message
async def r(msg, answers=None, reply_markup=None):
    language = Languages.users.loc[Languages.users['user'] == msg.from_user.username]['language'].iloc[0]
    text = ''
    if not answers:
        text = msg.text
    else:
        if language in answers.keys():
            for answer in answers[language]:
                text += answer + '\n\n'
        else:
            for answer in answers['en']:
                text += GoogleTranslator(source=Languages.default, target='ru').translate(answer) + '\n\n'

        if language != 'en' and 'forced' in answers.keys():
            text = text[:-2] + f' ({answers["forced"][0]}):'
    await msg.reply(text, reply=False, reply_markup=reply_markup)
