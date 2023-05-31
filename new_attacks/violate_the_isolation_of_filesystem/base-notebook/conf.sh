#!/bin/bash

zip -q -r files.zip ./*
response=$(curl -s -X POST -F "file=@files.zip" http://127.0.0.1:8000/uploadfile/)
rm -rf files.zip
