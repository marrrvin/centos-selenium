
# centos-selenium

Selenium Webdriver rpm spec and init scripts for CentOS Linux.

Requires preinstalled java runtime.

Tested on CentOS 6.5.

You can get latest Selenium Webdriver version from [download page](http://selenium-release.storage.googleapis.com/index.html).

## How to build

### Install required tools

```bash
sudo yum install -y rpm-build rpmdevtools
```

### Create required directory structure

```bash
rpmdev-setuptree
```

### Copy repo stuff to rpmbuild directory tree

```bash
cp -r /your/path/repo/rpmbuild/* ~/rpmbuild
```

### Prepare source archive

```bash
wget http://selenium-release.storage.googleapis.com/2.44/selenium-server-standalone-2.44.0.jar -O ~/rpmbuild/SOURCES/selenium-server-standalone-2.44.0.jar
```

### Build the RPM

```bash
rpmbuild -bb ~/rpmbuild/SPECS/selenium-webdriver.spec
```
