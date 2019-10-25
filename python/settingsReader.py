import json
import vim
import daemon

def parse_settings():
    with open("vim_cmake_settings.json", "r") as settings_file:
        settings_data = json.load(settings_file)
        settings = []
        configuration = {}
        for configuration_data in settings_data["configurations"]:
            configuration['name']            = configuration_data['name']
            configuration['build_type']      = configuration_data['build_type']
            configuration['bit']             = configuration_data['bit']
            configuration['build_dir']       = configuration_data['build_dir']
            configuration['cmake_generator'] = configuration_data['cmake_generator']
            configuration['cmake_variables'] = configuration_data['cmake_variables']
            settings.append(configuration)
        print(settings)
