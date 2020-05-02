import subprocess

class CMakeHelper:
    def __init__(self):
        pass


    def configure(self, settings):
        build_dir_param = '-B'
        source_dir_param = '-S'
        generator_param = '-G'
        print('cmake ' + build_dir_param + source_dir_param + generator_param)
        subprocess.run(["cmake", build_dir_param, settings['build_dir'], source_dir_param, '.', generator_param, settings['cmake_generator']])


    def cmake_run(self, settings):
        subprocess.run(["cmake"])

