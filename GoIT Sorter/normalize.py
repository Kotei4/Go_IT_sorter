import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "zh","z", "y", "y", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "shch", "", "y", "", "e", "yu", "ya", "ye", "i","yi", "g")

TRANS = dict()      #Створюємо словник який буде мати вигляд: {1072: 'a', 1040: 'A' .... }


for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):  # Ітеруємося по двох послідовностях, щоб зробити словник вигляду
    TRANS[ord(cyrillic)] = latin                            # Номеру Кириличного літери : літеру латинського алфавіту
    TRANS[ord(cyrillic.upper())] = latin.upper()            # Номеру Кириличного великого літери : літеру латинського алфавіту
                                                            # За одну ітерацію маленьку та велику літери : а, б, в ...

def normalize(name: str) -> str:
    translate_name = re.sub(r'\W\.]', '_', name.translate(TRANS))
    return translate_name