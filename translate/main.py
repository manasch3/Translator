from googletrans import Translator, LANGUAGES


def available_languages(letter):
    letter = letter.lower()
    languages = [f'{code} :{language}' for code,language in LANGUAGES.items() if language.lower().startswith(letter)]

    if not languages:
        print(f'NO LANGUAGES AVAILABLE WITH "{letter}"')
        return

    for i in range(0, len(languages), 10):
        print(',  '.join(languages[i:i + 10]))


def translate_text(text, language):
    """
    Translates the given text into any language mentioned by user!
    :param text: text to be translated.
    :param language: user mentioned language.
    :return: translated language.
    """
    translator = Translator()
    translated = translator.translate(text, dest=language)
    return translated.text

while True:
    user_text = input('Text ["e" to exit] : ')
    if user_text == 'e':
        break

    user_language = input('Language code  [eg: te, fr, ar] : ')

    try:
        translated_text = translate_text(user_text, user_language)
        print(f'{translated_text}')
    except Exception as e:
        print(f'Error: {e}')

    lang_list = input('Check languages by letter? [y/n] : ').lower()
    if lang_list == 'y':
        letter = input('Starting letter: ')
        available_languages(letter)







