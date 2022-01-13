#!/usr/bin/env bash
#Write a Bash script that sets up your web servers for the deployment of web_static.

# Install Nginx (if not already)

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

#Create folders

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create fake html to test Nginx to test configuration

echo "This is a test" | sudo tee /data/web_static/releases/test/index.html

#Create symbolic link

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Changes the owner

sudo chown -hR ubuntu:ubuntu /data/

# Updates the nginx conf

sudo sed -i '45i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restarts Nginx

sudo service nginx start
