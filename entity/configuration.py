class Configuration:

    def __init__(self, output_file_name='', input_file_path='', input_file='', schema_validation='',
                 env=''):
        self.__output_file_name = output_file_name
        self.__input_file_path = input_file_path
        self.__input_file = input_file
        self.__schema_validation = schema_validation
        self.__env: str = env

    @property
    def output_file_name(self):
        return self.__output_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        self.__output_file_name = output_file_name

    @property
    def input_file_path(self):
        return self.__input_file_path

    @input_file_path.setter
    def input_file_path(self, input_file_path):
        self.__input_file_path = input_file_path

    @property
    def schema_validation(self):
        return self.__schema_validation

    @schema_validation.setter
    def schema_validation(self, schema_validation):
        self.__schema_validation = schema_validation

    @property
    def input_file(self):
        return self.__input_file

    @input_file.setter
    def input_file(self, input_file):
        self.__input_file = input_file

    @property
    def env(self):
        return self.__env

    @env.setter
    def env(self, env):
        self.__env = env

    @staticmethod
    def sheets(): return ['Feuil3', 'Règles sur contrat', 'Caractéristiques-Attributs', 'catalogue PA',
                          'Valeurs', 'catalogue CA', 'catalogue CT', 'catalogue SV', 'Package',
                          'Catalogue PE', 'Catalogue PSE']
