python3 -m venv venv
. venv/bin/activate
pip install pyyaml==5.3.1 opera ansible

ansible-galaxy collection install community.libvirt
