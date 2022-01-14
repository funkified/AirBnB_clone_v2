#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""

from datetime import datetime
from fabric.api import local, put, run, env
from os.path import isdir, exists


env.hosts = ['34.139.124.220', '34.74.25.112']
env.user = 'ubuntu'
env.my_ssh_private_key = 'my_ssh_private_key'


def do_pack():
    """generate tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except None:
        return None


def do_deploy(archive_path):
    """Distribute archives to web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False


def deploy():
    """ create an archive to servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
