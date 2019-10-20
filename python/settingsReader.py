import json
import vim

def parse_settings():
    with open("vim_cmake_settings.json", "r") as settings_file:
        settings = json.load(settings_file)
        for configuration in settings["configurations"]:
            name = vim.bindeval('g:cmake_configuration_name')
            name 




