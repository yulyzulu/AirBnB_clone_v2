#!/usr/bin/python3
"""Module to execute functions"""
from fabric.api import *
import os.path
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


env.host = ['35.231.167.55', '34.236.146.248']

#if __name__ == "__main__":

def deploy():
    """deploy function"""
    path = do_pack()

    if os.path.isfile(path):
        new_path = do_deploy(path)
        return new_path
    else:
        return False
