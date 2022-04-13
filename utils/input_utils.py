from jsonschema.exceptions import ValidationError
import sys
import constans
from entity.configuration import Configuration
from jsonschema import validate
import json

import exception


def import_schema_validation(configuration: Configuration):
    with open('resources/json_file_schema.json', 'r') as file:
        schema: dict = json.load(file)

    configuration.schema_validation = schema


def import_configuration_file(configuration: Configuration):
    if configuration.input_file_path.endswith('.json'):
        with open(configuration.input_file_path, 'r') as file:
            input_file: dict = json.load(file)

        configuration.input_file = input_file

    else:
        raise exception.InvalidFileFormatError(constans.INVALID_FILE_FORMAT_ERROR)


def validate_schema_of_input_file(configuration: Configuration):
    try:
        validate(instance=configuration.input_file, schema=configuration.schema_validation)
    except ValidationError as err:
        print('Error Message: ', err.message)
        __process_id_adherent_co_etab_errors(err)
        __process_export_options_errors(err)
        __process_additional_properties_errors(err)
        sys.exit()


def __process_export_options_errors(err: ValidationError):
    if 'exportOptions' in err.absolute_path:
        raise exception.InvalidJsonFormat(constans.FORMAT_INVALID_PA_PE_ERROR)


def __process_id_adherent_co_etab_errors(err: ValidationError):
    id_adherent_co_etab_has_errors = "Id_Adherent_Co_Etab" in err.schema_path or \
                                     "Id_Adherent_Co_Etab" in err.args[0]

    if id_adherent_co_etab_has_errors:
        if err.validator in 'required':
            raise exception.InvalidJsonFormat(constans.ID_ADHERENT_CO_ESTAB_IS_NOT_PRESENT_ERROR)

        if err.validator in 'minItems':
            raise exception.InvalidJsonFormat(constans.MIN_LENGTH_ID_ADHERENT_CO_ESTABDHERENT_CO_ETAB_ERROR)


def __process_additional_properties_errors(err: ValidationError):
    if err.validator in 'additionalProperties':
        raise exception.AdditionalPropertiesError(constans.ADDITIONAL_PROPERTIES_ERROR)
