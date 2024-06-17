#!/usr/bin/python3
"""
distributes an archive to web servers
"""
from fabric.api import *
from fabric.operations import run, put, sudo
import os.path
env.hosts = ['142.44.167.241', '144.217.246.212']
#env.user = 'ubuntu'


def do_deploy(archive_path):
    """ returns true if deployed correctly, else false"""
    # EX:
    # archive_path = versions/web_static_20170315003959.tgz
    # filename = web_static_20170315003959.tgz

    if not os.path.isfile(archive_path):
        return False

    try:
        filename = archive_path.split("/")[1]
        temp_path = "/tmp/" + filename
        filename_split = filename.split(".")[0]

        #folder name = /data/web_static/releases/<archive filename w/o ext
        # EX: mkdir -p /data/web_static/releases/web_static_20170315003959/
        folder = "/data/web_static/releases/" + filename_split

        #Upload the archive to the /tmp/ directory
        put(archive_path, temp_path)

        run("sudo mkdir -p {}".format(folder))

        # Uncompress the archive to the folder
        #syntax: tar -zxvf filename -C dir
        run("sudo tar -xzf {} -C {}".format(temp_path, folder))

        #Delete the archive from the web server
        # /tmp/web_static_20170315003959.tgz
        run("sudo rm {}".format(temp_path))
        run("sudo mv {}web_static/* {}".format(folder, folder))
        run("sudo rm -rf {}web_static".format(folder))

        #Delete the symbolic link /data/web_static/current from the web server
        run("sudo rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current
        # on the web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        run("ln -s {} /data/web_static/current".format(folder))
        print("end")
        return True

    except:
        return False
