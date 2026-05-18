#!/bin/bash
mkdir linux_practice
mkdir linux_practice/docs linux_practice/backup
cd ./linux_practice/docs 
touch readme.txt notes.log temp.tmp
rm temp.tmp
mv notes.log daily_report.txt
echo "Project Status: Active" >daily_report.txt
date >> daily_report.txt
cd ..
cp docs/*.txt backup/ 
for file in backup/*
do 
    chmod 444 "$file"
    echo "Archive Complete. File [$(basename "$file")] is now read-only"
done
