#!/bin/bash
if [[ $(whoami) != "root" ]]; then
  echo "[!] You need to be root to install whysp"
  exit 1
fi
pip install -r ./requirements.txt
mkdir /opt/whysp
chmod 777 /opt/whysp
cp whysp.py /opt/whysp/whysp.py
ln -s /opt/whysp/whysp.py /usr/bin/whysp
