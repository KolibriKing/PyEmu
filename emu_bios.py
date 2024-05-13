"""
Module to control general functions of machine
"""

import glvar

"""
Start machine

Argument 1: bool, loading_screen: show loading screen, default True
Argument 2: string, mode, default 'n': modes:
n: normal
s: safe mode
Argument 3: string, data_file: boot data file, opened as `f'boot/{data_file}'`,
must contain main boot file and other configurations, see docs/boot_data_file.txt
"""

# Check if MACHINE_STATUS variable exists
if not glvar.exists('MACHINE_STATUS'):
  glvar.create('MACHINE_STATUS', 'off')
# else, try to recover last session
else:
  # coming soon
  pass

def boot(loading_screen=True, mode='n', data_file='boot/bm.json'):
  bscr = None
  glvar.set('MACHINE_STATUS', 'boot')
  from json import load
  data_file_obj = open(data_file, 'r')
  data = load(data_file_obj)
  print('\033c')
  print(f'[BIOS] Starting {data["os_fname"]}...')
  if data["boot_mode"] == 'r':
    with open(data["boot"], 'r') as f:
      exec(f.read())
  elif data["boot_mode"] == 'p':
    from subprocess import run
    run(['python3.12', data['boot']])
  elif data['boot_mode'] == 'c':
    from os import system
    system(f'python3.12 {data["boot"]}')