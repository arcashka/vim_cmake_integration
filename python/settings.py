import json


class Settings:
    def __init__(self):
        self.data = []

    def parse(self, filename):
        with open(filename, "r") as settings_file:
            settings_data = json.load(settings_file)
            for configuration_data in settings_data["configurations"]:
                configuration = {}
                configuration['name'] = configuration_data['name']
                configuration['build_type'] = configuration_data['build_type']
                configuration['arch'] = configuration_data['arch']
                configuration['build_dir'] = configuration_data['build_dir']
                configuration['cmake_generator'] = configuration_data['cmake_generator']
                configuration['cmake_variables'] = configuration_data['cmake_variables']
                for key in configuration:
                    if '%SRC_DIR%' in configuration[key]:
                        configuration[key] = configuration[key].replace('%SRC_DIR%', '.')
                    if '%NAME%' in configuration[key]:
                        configuration[key] = configuration[key].replace('%NAME%', configuration['name'])
                self.data.append(configuration)

