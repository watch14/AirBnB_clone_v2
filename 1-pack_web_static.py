#!/usr/bin/python3
""" fabric script """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ .tgz archive """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)

    result = local("sudo tar -cvzf {} web_static".format(filename))

    return filename if result.succeeded else None
