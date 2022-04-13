from entity.configuration import Configuration
from utils import output_utils, argument_utils, input_utils


def start():
    configuration: Configuration = Configuration()

    argument_utils.process_arguments(configuration)

    input_utils.import_schema_validation(configuration)
    input_utils.import_configuration_file(configuration)
    input_utils.validate_schema_of_input_file(configuration)

    output_utils.define_file_name(configuration)
    output_utils.create_sheets(configuration)
    output_utils.show_importation_success_log(configuration)


start()
