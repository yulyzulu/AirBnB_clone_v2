#!/usr/bin/python3
"""Module to execute functions"""
from fabric.api import *
import os.path
from fabric.decorators import runs_once
from datetime import datetime
from os.path import getsize


@runs_once
def do_pack():
    local("mkdir -p versions")
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    command = local("tar -cvzf versions/web_static_{}.tgz ./web_stat\
ic".format(date_time))

    if command.succeeded:
        size = getsize('versions/web_static_{}.tgz'.format(date_time))
        print("web_static packed: versions/web_static_{}.tgz -> {}Byt\
es".format(date_time, size))
        return ('versions/web_static_{}.tgz'.format(date_time))
    else:
        return None


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


@task
def deploy():
    """deploy function"""
    path = do_pack()

    if os.path.isfile(path):
        new_path = do_deploy(path)
        return new_path
    else:
        return False
