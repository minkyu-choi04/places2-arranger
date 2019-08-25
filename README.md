# Places2-Arranger
Python code for re-arranging Places2-large dataset.   
Places2 (http://places2.csail.mit.edu/download.html) provides high-resolution images which is not arranged to be used to in Pytorch data loader. This repo provides codes for re-arranging high-resolution Places2 dataset for Pytorch data loader. 

## Usage
### Requirements
1. Download Places2-large train dataset from http://data.csail.mit.edu/places/places365/train_large_places365standard.tar
2. Download Places2-large valiation dataset from http://data.csail.mit.edu/places/places365/val_large.tar
3. Untar two downloaded files to one directory. (`~/Places2/` in this example)
4. Download and save this repo's codes in the same directory. 
Then, `~/Places2/` directory has followings: `data_large`, `val_large`, `arrange_train.py`, `arrange_val.py`, `val.txt`.

Use terminal to execute `arrange_train.py` and `arrange_val.py`. 
```
python arrange_train.py
python arrange_val.py
```

## Tested Environments
`Ubuntu 16.04`, `python 3.6`

## To Do
Elabarate codes. 
