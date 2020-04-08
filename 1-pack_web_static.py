#!/usr/bin/python3
"""Module that execute functions"""
from fabric.api import local
from datetime import datetime

def do_pack():
    local("mkdir -p versions")
    comand = local("tar -cvzf versions/web_static_{}.tgz ./web_static".format(datetime.now().strftime("%Y%m%d%H%M%S")))

#Conditional to return path
