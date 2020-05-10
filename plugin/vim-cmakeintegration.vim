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

import subprocess
import vim

plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
proc = subprocess.Popen(['python', python_root_dir + '/cmake_server.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#proc = subprocess.Popen(['python', python_root_dir + '/cmake_server.py'])

EOF

endfunction

function! Configure()

python3 << EOF

import message_sender
import asyncio

sender = message_sender.MessageSender()
asyncio.run(sender.send('configure'))

EOF

endfunction

function! Quit()

python3 << EOF
import message_sender
import asyncio

sender = message_sender.MessageSender()
asyncio.run(sender.send('quit'))
EOF

endfunction

command! -nargs=0 CMakeConfigure call Configure()
command! -nargs=0 CMakeQuit call Quit()
command! -nargs=0 CMakeStart call StartServer()

