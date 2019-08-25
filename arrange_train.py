import os
'''
Code for re-arranging Places365-large for pytorch dir-loader. 
Dir structure: Places365/data_large
Run this progam in the dir of Places365.
'''
alp_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('removing a, b, c ...')
target_dir = './data_large'
list_dir = os.listdir(target_dir)
for alp in list_dir:
    if alp in alp_list:
        cat_dir = os.listdir(os.path.join(target_dir, alp))
        for cat in cat_dir:
            os.rename(os.path.join(target_dir, alp, cat), os.path.join(target_dir, cat))

for cat in list_dir:
    fn = os.listdir(os.path.join(target_dir, cat))
    if len(fn) is 0:
        os.rmdir(os.path.join(target_dir, cat))
        print(cat)

print('removing in/out door')
target_dir = './data_large'
list_dir = os.listdir(target_dir)
for cat in list_dir:
    if os.path.exists(os.path.join(target_dir, cat, 'indoor')):
        os.rename(os.path.join(target_dir, cat, 'indoor'), os.path.join(target_dir, cat+'-indoor'))
        print(os.path.join(target_dir, cat, 'indoor'), os.path.join(target_dir, cat+'-indoor'))
    
    if os.path.exists(os.path.join(target_dir, cat, 'outdoor')):
        os.rename(os.path.join(target_dir, cat, 'outdoor'), os.path.join(target_dir, cat+'-outdoor'))
        print(os.path.join(target_dir, cat, 'outdoor'), os.path.join(target_dir, cat+'-outdoor'))

for cat in list_dir:
    fn = os.listdir(os.path.join(target_dir, cat))
    if len(fn) is 0:
        os.rmdir(os.path.join(target_dir, cat))
        print(cat)

print('removing rest sub-dirs')
list_dir = os.listdir(target_dir)
for cat in list_dir:
    file_names = os.listdir(os.path.join(target_dir, cat))
    for fn in file_names:
        if fn[-3:] == 'jpg':
            continue
        else:
            os.rename(os.path.join(target_dir, cat, fn), os.path.join(target_dir, cat + '-' + fn))
            print(os.path.join(target_dir, cat, fn), os.path.join(target_dir, cat + '-' + fn))

for cat in list_dir:
    fn = os.listdir(os.path.join(target_dir, cat))
    if len(fn) is 0:
        os.rmdir(os.path.join(target_dir, cat))
        print(cat)
