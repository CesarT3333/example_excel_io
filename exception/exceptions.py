class GenericValidationError(Exception):

    def __init__(self, error_message: str):
        super().__init__(error_message + self.__get_correct_format_json_example())

    @staticmethod
    def __get_correct_format_json_example():
        return """\n
                Follow the json example below:
                {
                    "Id_Adherent_Co_Etab": [ 1, 2, ... ],
                    "exportOptions": {
                        "Pa": true,
                        "Pe": true
                    }
                }
                """


class MandatoryArgumentError(GenericValidationError):
    pass


class InvalidFileFormatError(GenericValidationError):
    pass


class InvalidJsonFormat(GenericValidationError):
    pass


class AdditionalPropertiesError(GenericValidationError):
    pass
