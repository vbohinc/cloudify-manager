#/*******************************************************************************
# * Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *       http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.
# *******************************************************************************/
import getpass
import logging
import os
import random
import string
import tempfile

from cloudify.mocks import MockCloudifyContext

from worker_installer.tasks import FabricRetryingRunner


__author__ = 'idanm'

VAGRANT_MACHINE_IP = "10.0.0.5"
VAGRANT_PATH = os.path.join(tempfile.gettempdir(), "vagrant-vms")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def get_remote_runner():

    host_config = {
        'user': 'vagrant',
        'host': VAGRANT_MACHINE_IP,
        'port': 22,
        'key': '~/.vagrant.d/insecure_private_key'
    }
    host_string = '%(user)s@%(host)s:%(port)s' % host_config
    key_filename = host_config['key']

    return FabricRetryingRunner(key_filename=key_filename, host_string=host_string)


def get_local_runner():
    return FabricRetryingRunner(local=True)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.level = logging.DEBUG
    return logger


def get_local_management_worker_config():
    return {
        "user": getpass.getuser(),
        "management": True,
        "broker": "amqp://",
        "name": "test-worker-{0}".format(id_generator(3)),
        "env": {
            "BROKER_URL": "amqp://guest:guest@localhost:5672//",
            "MANAGEMENT_IP": "localhost",
            "MANAGER_REST_PORT": 8100
        }
    }


def get_local_worker_config():
    return {
        "user": getpass.getuser(),
        "broker": "amqp://",
        "name": "test-worker-{0}".format(id_generator(3)),
        "env": {
            "BROKER_URL": "amqp://guest:guest@localhost:5672//",
            "MANAGEMENT_IP": "localhost",
            "MANAGER_REST_PORT": 8100
        }
    }


def get_remote_worker_config():
    return {
        "user": "vagrant",
        "port": 22,
        "name": "test-worker-{0}".format(id_generator(3)),
        "key": "~/.vagrant.d/insecure_private_key",
        "env": {
            "BROKER_URL": "amqp://guest:guest@10.0.0.1:5672//",
            "MANAGEMENT_IP": VAGRANT_MACHINE_IP,
            "MANAGER_REST_PORT": 8100
        }
    }


def get_remote_management_worker_config():
    return {
        "user": "vagrant",
        "port": 22,
        "management": True,
        "name": "test-worker-{0}".format(id_generator(3)),
        "key": "~/.vagrant.d/insecure_private_key",
        "env": {
            "BROKER_URL": "amqp://guest:guest@10.0.0.1:5672//",
            "MANAGEMENT_IP": VAGRANT_MACHINE_IP,
            "MANAGER_REST_PORT": 8100
        }
    }


def get_local_context():

    capabilities = {
        'ip': '127.0.0.1'
    }

    return MockCloudifyContext(capabilities=capabilities)


def get_remote_context():

    capabilities = {
        'ip': VAGRANT_MACHINE_IP
    }

    return MockCloudifyContext(capabilities=capabilities)
