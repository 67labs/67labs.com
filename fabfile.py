from fabric.api import local, env, hosts
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer

from pelican.server import ComplexHTTPRequestHandler

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
PELICAN_BIN = os.path.join(ROOT_PATH, 'bin', 'pelican')
DEVELOPMENT_CONFIG = os.path.join(ROOT_PATH, 'settings', 'base.py')
PUBLISH_CONFIG = os.path.join(ROOT_PATH, 'settings', 'publish.py')

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = os.path.join(ROOT_PATH, 'html')
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@67labs.com:22'
dest_path = '/srv/sites/67labs.com/'

# Port for `serve`
PORT = 8000


def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)


def build():
    """Build local version of site"""
    local('"%s" -s "%s"' % (PELICAN_BIN, DEVELOPMENT_CONFIG))


def rebuild():
    """`clean` then `build`"""
    clean()
    build()


def regenerate():
    """Automatically regenerate site upon file modification"""
    local('"%s" -r -s "%s"' % (PELICAN_BIN, DEVELOPMENT_CONFIG))


def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()


def reserve():
    """`build`, then `serve`"""
    build()
    serve()


def preview():
    """Build production version of site"""
    local('"%s" -s "%s"' % (PELICAN_BIN, PUBLISH_CONFIG))


@hosts(production)
def publish():
    """Publish to production via rsync"""
    local('"%s" -s "%s"' % (PELICAN_BIN, PUBLISH_CONFIG))
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )
