import re
hoge = input('入力＞ ')
hoge = re.split('[.!?]', hoge)
if hoge[-1] == '':
    del hoge[-1]
print(len(hoge))
