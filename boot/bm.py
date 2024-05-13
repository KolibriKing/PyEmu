# PyEmu boot menu
# Runs at emu_bios.boot() if the third argument isn't passed
print('\033c')
from os import get_terminal_size, listdir, path
term_width = get_terminal_size()[0]
spaces = term_width / 2 - (len('Boot menu') / 2)
# check if number is power of 2
if not spaces > 0 and (spaces & (spaces - 1)) == 0:
  spaces = spaces - 1
print('\033[7m' + ' ' * int(spaces) + 'Boot menu' + ' ' * int(spaces) + '\033[0m')

i = 0
ilist = []
for fname in listdir('boot/os'):
  f = path.join('boot/os', fname)
  if path.isfile(f):
    with open(f, 'r') as file:
      file_content = file.readlines()
      if file_content[0][:16] == '#emu_boot def os':
        print(f'[{i}] ' + file_content[0][17:])
        i = i + 1
        ilist.append(f)
osindex = input('> ')