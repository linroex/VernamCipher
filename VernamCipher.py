from operator import xor

def autokey(key, plain_text):
    new_key = ''
    key_i = 0;
    text_i = 0;

    while len(new_key) < len(plain_text):
        if key_i >= len(key):
            key_i = 0
        if text_i >= len(plain_text):
            plain_text = 0
        new_key += plain_text[text_i] + key[key_i]

        key_i += 1
        text_i += 1

    return new_key
def char_process(char):
    return ord(char) - 97
def encrypt(char1, char2):
    return chr(xor(char_process(char1), char_process(char2)) + 97)

def main():
    key = 'XMCL'.lower()
    plain_text = 'HELO'.lower()
    encrypt_text = ''

    key = autokey(key, plain_text)

    for i in range(0, len(plain_text)):
        encrypt_text += encrypt(plain_text[i], key[i])

    print(encrypt_text.upper())

if __name__ == '__main__':
    main()