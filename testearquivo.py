

def teste():
    test = open('marcos.txt', 'w', encoding='utf-8')
    test.write('Esse é um teste')
    test.close()


if __name__ == '__main__':
    teste()
