let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

if !has("python3")
	echo "Vim has to be compiled with +python3 to run this"
	finish
endif

if exists('g:vim_cmakeintegration_loaded')
	finish
endif

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
EOF

function! StartServer()

python3 << EOF
import cmake_server
import asyncio

server = cmake_server.Server()
loop = asyncio.get_event_loop()
loop.create_task(server.start())
loop.start()

EOF

endfunction

function! Configure()

python3 << EOF
import message_sender

sender = message_sender.MessageSender()
asyncio.run(sender.send('configure'))
EOF

endfunction

function! Quit()

python3 << EOF
import message_sender

sender = message_sender.MessageSender()
asyncio.run(sender.send('quit'))
EOF

endfunction

call StartServer()

command! -nargs=0 CMakeConfigure call Configure()
command! -nargs=0 CMakeQuit call Quit()
