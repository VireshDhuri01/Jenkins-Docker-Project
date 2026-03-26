#!/bin/bash

#simply run this file and get Jenkins installed on your EC2 machine !

#install java
sudo apt update
sudo apt install openjdk-21-jre -y
java --version

#jenkins pre-req and jenkins installation

sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \https://pkg.jenkins.io/debian-stable binary/ | sudo tee \/etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins -y
