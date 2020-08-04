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
    ("osism-run-without-secrets"),
    ("osism-update-manager")
])
def test_wrapper_script_files(host, name):
    f = host.file("/usr/local/bin/%s" % name)
    assert f.exists
    assert f.is_file


@pytest.mark.parametrize("name", [
    ("manager_ara-server_1"),
    ("manager_redis_1"),
    ("manager_ceph-ansible_1"),
    ("manager_mariadb_1"),
    ("manager_kolla-ansible_1"),
    ("manager_osism-ansible_1")
])
def test_running_containers(host, name):
    c = host.docker(name)
    assert c.is_running
