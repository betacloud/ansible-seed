import pytest


@pytest.mark.parametrize("name", [
    ("osism-ansible"),
    ("osism-ceph"),
    ("osism-generic"),
    ("osism-infrastructure"),
    ("osism-kolla"),
    ("osism-manager"),
    ("osism-mirror"),
    ("osism-monitoring"),
    ("osism-openstack"),
    ("osism-run"),
    ("osism-run-without-secrets")
])
def test_wrapper_script_files(host, name):
    f = host.file("/usr/local/bin/%s" % name)
    assert f.exists
    assert f.is_file
