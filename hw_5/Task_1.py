# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = 'АБВ ылоаабВжы фыыдлхsdfs абв Зщышф вабвв ффлжgfhв абВ'
new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
print(new_str)