#!/usr/bin/env bash
# Prepare the web servers

sudo apt-get update
sudo apt-get install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}' /etc/nginx/sites-enabled/default

sudo service nginx restart
