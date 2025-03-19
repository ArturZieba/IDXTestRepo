#!/bin/bash

echo "Count in int and string:"

for n in 1 two 3 four
do
    echo "Number $n"
done

echo "Count in int range:"

for n in {1...5}
do 
    echo "Number $n"
done

echo "Run ls:"
for f in $(ls)
do
    echo $f
done