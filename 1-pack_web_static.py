#!/usr/bin/python3
""" fabric script """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ .tgz archive """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"versions/web_static_{date}.tgz"

    result = local(f"sudo tar -cvzf {filename} web_static")

    return filename if result.succeeded else None
