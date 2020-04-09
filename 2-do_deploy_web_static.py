#!/usr/bin/python3
"""Module that execute functions"""
from fabric.api import *
from datetime import datetime
import os.path

env.hosts = ['35.231.167.55', '34.236.146.248']


def do_deploy(archive_path):
    if os.path.isfile(archive_path):
        path1 = archive_path.split("/")
        path2 = path1[-1].split(".")
        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/release\
s/{}".format(path2[0]))
        sudo("tar -xzf /tmp/{} -C /data/web_static/release\
s/{}".format(path1[-1], path2[0]))
        sudo("rm /tmp/{}".format(path1[-1]))
        sudo("mv /data/web_static/releases/{0}/web_static/* /data/web_stat\
ic/releases/{0}/".format(path2[0]))
        sudo("rm -rf /data/web_static/releases/{}/web_stat\
ic/".format(path2[0]))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{} /data/web_stat\
ic/current".format(path2[0]))
        print("New version deployed!")
        return True
    else:
        return False
