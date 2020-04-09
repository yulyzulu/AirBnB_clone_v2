#!/usr/bin/python3
"""Module that execute functions"""
from fabric.api import local
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
