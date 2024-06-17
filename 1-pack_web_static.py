#!/usr/bin/python3
"""
Contains fabric script that generates a .tgz archive
from the contents of the web_static. All files in the
folder web_static must be added to the final archive
All archives must be stored in the folder versions
(your function should create this folder if it doesn’t exist)
The name of the archive created must be
web_static_<year><month><day><hour><minute><second>.tgz

"""
from fabric.api import *
from time import strftime


def do_pack():
    """ returns archive path if the archive has been correctly generated"""
    ct = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -zcvf versions/web_static_{:s}.tgz web_static/".format(ct))
        return ("versions/web_static_{:s}.tgz".format(current_time))

    except:
        return None
