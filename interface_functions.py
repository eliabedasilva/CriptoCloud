def line(char='-', quantity=50):
    print(char*quantity)


def title(phrase):
    line()
    print(phrase.center(50))
    line()


def menu(menu_list):
    line()
    for index, item in enumerate(menu_list):
        print(f'{index+1} - {item}')
    line()
    return int(input('Opção: '))
