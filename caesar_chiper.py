import enchant


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


class CaesarsCipher:
    def __init__(self):
        self.caesarsCipher = CaesarsCipher()


def decrypt(message: str, key: int):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            sym_index = SYMBOLS.find(symbol)
            trans_index = sym_index - key
            if trans_index >= len(SYMBOLS):
                trans_index = trans_index - len(SYMBOLS)
            elif trans_index < 0:
                trans_index = trans_index + len(SYMBOLS)
                translated = translated + SYMBOLS[trans_index]
            else:
                translated = translated + SYMBOLS[trans_index]
    return translated


def encrypt(message, key):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            sym_index = SYMBOLS.find(symbol)
            trans_index = sym_index + key
            if trans_index >= len(SYMBOLS):
                trans_index = trans_index - len(SYMBOLS)
                translated = translated + SYMBOLS[trans_index]
            else:
                translated = translated + SYMBOLS[trans_index]
    return translated


if __name__ == '__main__':
    d = enchant.Dict("en_US")
    m = input('Введите зашифрованную строку: ')  #Получение строки для расшифровки
    for i in range(0, 26):
        s = decrypt(message=m, key=i)
        words = s.split()
        for elem in words:
            if d.check(elem) and len(elem) > 2:
                s_d = f"key = {i}, {s}"
                break

    t_path = input('Укажите путь к файлу'
                   'с расшифрованной строкой: ')

    with open(t_path, "w") as file:
        file.write(f'Ваша фраза: {s_d}')

    print(s_d)
    print(encrypt(message='The vacation was a success', key=3))
