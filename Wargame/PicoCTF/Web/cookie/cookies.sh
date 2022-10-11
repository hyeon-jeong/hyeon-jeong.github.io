#!/bin/bash

for i in {0..28}
do
    echo "cookie name : $i"
    curl --cookie "name=$i" "http://mercury.picoctf.net:54219/check"
done
