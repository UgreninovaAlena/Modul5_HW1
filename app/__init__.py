import os

list = os.listdir(path=os.getcwd())
msg = '\n'.join(list)
print(list)
print(msg)