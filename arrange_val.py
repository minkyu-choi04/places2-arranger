import os 
'''
Code for re-arranging Places365-large for pytorch dir-loader. 
Dir structure: Places365/val_large
val.txt is from places365-standard-easy-format and should be placed in Places365
Run this progam in the dir of Places365.
This program moves data from val_large to val.
'''

filename = 'val.txt'
source_dir = './val_large'
val_dir = './val'
if not os.path.exists(val_dir):
    os.makedirs(val_dir)

with open(filename) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        #print(line)
        #print(line.split('/'))
        #print(line.split('/')[-1][:-1])
        
        cat_dir = line.split('/')[1]
        file_name = line.split('/')[-1][:-1]
        
        if not os.path.exists(os.path.join(val_dir, cat_dir)):
            os.makedirs(os.path.join(val_dir, cat_dir))
        os.rename(os.path.join(source_dir, file_name), os.path.join(val_dir, cat_dir, file_name))
        
        line = fp.readline()
        cnt += 1

