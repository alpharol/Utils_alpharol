#!/bin/bash

echo "--------------------数据拼接中....----------------------"
python data_aug.py
python con_text.py

echo "--------------------数据整合中....----------------------"
mkdir chanxian_golden
cd chanxian_golden
mkdir wavs
cd wavs
cp /nfsc/cyx/data/chanxian_15230_v4/wavs/* .
cp /nfsc/cyx/data/chepai_1758/wavs/* . 
cp /nfsc/cyx/data/output/* .
cd ..
cp /nfsc/cyx/data/metadata.txt .
cd ..

echo "--------------------数据压缩中....----------------------"
zip -q -r chanxian_golden.zip chanxian_golden

echo "--------------------删除冗余数据....----------------------"
rm -rf output
rm -rf output_text.txt
rm -rf metadata.txt
