from firebase_manager import FireBaseManager
from interface_functions import *


def load_file(path):
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content


def main():
    manager = FireBaseManager(
        certificate_path='caminho do arquivo que contém o certificado de ',
        url='url do banco',
        key='chave para criptografaro conteúdo'
    )

    while True:

        title('Bem Vindo ao CriptoCloud')
        menu_list = ['Acessar arquivo', 'Adicionar arquivo', 'Atualizar arquivo', 'Deletar arquivo', 'Sair']
        option = menu(menu_list)

        if option == 5:
            break

        key_user = input('Digite  a chave de usuário: ')
        manager.key = key_user

        if option == 4:
            file_name = input('Digite o nome do arquivo para deletar: ').strip()
            content = manager.get(file_name)
            if content is None:
                pass
            else:
                if not content:
                    title('Chave invalida!!!')
                else:
                    print(f'Deseja deletar "{file_name}: {content}"')
                    confirm_remove = input('[s/n]').lower().strip()
                    if confirm_remove == 's':
                        manager.remove(file_name)
                        print(f'removido com sucesso!')

        elif option == 3:
            file_name = input('Digite o nome do arquivo na nuvem para ser atualizar: ').strip()
            file_path = input('Digite o caminho do novo arquivo: ').strip()
            content = manager.get(file_name)
            if content is None:
                pass
            else:
                if not content:
                    title('Chave invalida!!!')
                else:
                    new_content = load_file(file_path)
                    manager.update({file_name: new_content})
                    title('Atualização bem sucedida!!!')

        elif option == 2:
            file_path = input('Digite o caminho do arquivo: ').strip()
            content = load_file(file_path)
            file_name = file_path.split('\\')[-1].replace('.txt','')
            manager.add({file_name: content})

        elif option == 1:
            file_name = input('Digite o nome do arquivo: ')
            content = manager.get(file_name)
            if content is None:
                pass
            else:
                if not content:
                    title('Chave invalida!!!')
                else:
                    line(quantity=70)
                    print(content)
                    line(quantity=70)

        else:
            print('Opção inexistente')

        print('\n' * 5)


if __name__ == '__main__':
    main()
