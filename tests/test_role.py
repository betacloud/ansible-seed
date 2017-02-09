# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def test_python_packages_are_installed(Package, SystemInfo):
    if SystemInfo.distribution == 'ubuntu':
        package = Package("python-pip")
        assert package.is_installed

    elif SystemInfo.distribution == 'centos':
        package = Package("python2-pip")
        assert package.is_installed

    package = Package("python-virtualenv")
    assert package.is_installed
