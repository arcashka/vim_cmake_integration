import subprocess
import asyncio

class CMakeHelper:
    def __init__(self):
        pass


    async def configure(self, settings, out):
        build_dir_param = '-B'
        source_dir_param = '-S'
        generator_param = '-G'
        process = await asyncio.create_subprocess_exec(cmake, build_dir_param, setting['build_dir'], source_dir_param, '.', generator_param, settings['cmake_generator'], stdout=out)
        await proc.wait()
        print('configure trying to write eof. Can write eof = {}').format(out.can_write_eof())
        out.write_eof()


    def cmake_run(self, settings):
        subprocess.run(["cmake"])

