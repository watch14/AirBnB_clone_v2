#!/usr/bin/python3
""" upload web_static / uncompres / create new symbolik link """

from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['35.237.166.125', '54.167.61.201']


def do_deploy(archive_path):
    """ deploy """

    if exists(archive_path) is False:
        return False

    filename = archive_path.split('/')[-1]
    no_tgz = f'/data/web_static/releases/{filename.split(".")[0]}'
    tmp = f'/tmp/{filename}'

    # Upload to tmp
    put_result = put(archive_path, '/tmp/')
    if put_result.failed:
        return False

    # Uncompress /data/web_static/releases
    run_result1 = run(f'mkdir -p {no_tgz}/')
    run_result2 = run(f'tar -xzf {tmp} -C {no_tgz}/')
    run_result3 = run(f'rm {tmp}')

    # Move to web static / delete old files
    run_result4 = run(f'mv {no_tgz}/web_static/* {no_tgz}/')
    run_result5 = run(f'rm -rf {no_tgz}/web_static')

    # create a new symbolic link
    run_result6 = run('rm -rf /data/web_static/current')
    run_result7 = run(f'ln -s {no_tgz}/ /data/web_static/current')

    if (put_result.failed or run_result1.failed or run_result2.failed or
            run_result3.failed or run_result4.failed or run_result5.failed or
            run_result6.failed or run_result7.failed):
        return False

    return True
