import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_ice_version(Command, TestinfraBackend):
    assert Command.exists('icegridnode')
    c = Command('icegridnode --version')
    assert c.stderr.startswith('3.6.')


def test_icepy_version(Command, TestinfraBackend):
    c = Command('python -c "import Ice; print Ice.stringVersion()"')
    assert c.stdout.startswith('3.6.')


def test_ice_devel(Package, TestinfraBackend):
    assert Package('ice-all-devel').is_installed
