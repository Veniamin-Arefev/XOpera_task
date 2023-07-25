#!/bin/bash
if ! [ -e artifacts/images/jammy-server-cloudimg-amd64.img ]; then
    wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img -P artifacts/images/ -c
fi

if ! [ -e artifacts/images/focal-server-cloudimg-amd64.img ]; then
    wget https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64.img -P artifacts/images/ -c
fi

if ! [ -e artifacts/images/bionic-server-cloudimg-amd64.img ]; then
    wget https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.img -P artifacts/images/ -c
fi

