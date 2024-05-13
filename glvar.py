from os import path

def create(name, c):
  if not path.exists(f'var/{name}.txt'):
    with open(f'var/{name}.txt', 'w') as f:
      f.write(c)
  else:
    print(f'Error at glvar.create: {name}: variable already exists')

def set(name, c):
  if path.exists(f'var/{name}.txt'):
    with open(f'var/{name}.txt', 'w') as f:
      f.write(c)
  else:
    print(f'Error at glvar.create: {name}: variable doesn\'t exists')

def read(name):
  if path.exists(f'var/{name}.txt'):
    with open(f'var/{name}.txt', 'r') as f:
      return f.read()
  else:
    print(f'Error at glvar.create: {name}: variable doesn\'t exists')
  
def exists(name):
  return path.exists(f'var/{name}.txt')