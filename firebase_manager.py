import firebase_admin
from firebase_admin import credentials, db
import cryptocode


class FireBaseManager:
    def __init__(self,
                 certificate_path,
                 url,
                 key
                 ):
        self.key = key
        cred = credentials.Certificate(certificate_path)
        firebase_admin.initialize_app(cred, {'databaseURL': url})
        self.data_base_reference = db.reference()

    def add(self, data: dict):
        dict_db = self.data_base_reference.get()
        if len(data) > 1:
            print(f'ERRO! Só é permitido adcionar um arquivo por vez')
            return

        for key in data:
            if dict_db is not None and key in dict_db:
                print(f'ERRO! {key} já existente')
                return
            data = {key: cryptocode.encrypt(data[key], self.key)}

        self.data_base_reference.update(data)

    def get(self, key):
        content = self.data_base_reference.child(key).get()
        if content is None:
            print('ERRO! Chave não cadastrada!')
            return
        return cryptocode.decrypt(str(content), self.key)

    def remove(self, key):
        dict_db = self.data_base_reference.get()
        if dict_db is None or key not in dict_db:
            print('ERRO! Chave não cadastrada!')
            return
        self.data_base_reference.child(key).delete()

    def update(self, data: dict):
        if len(data) > 1:
            print(f'ERRO! Só é permitido atualizar um arquivo por vez')
            return

        for key in data:
            data = {key: cryptocode.encrypt(data[key], self.key)}
        self.data_base_reference.update(data)

