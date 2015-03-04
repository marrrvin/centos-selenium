
# centos-selenium

Selenium Webdriver rpm spec and init scripts

Selenium [download page](http://selenium-release.storage.googleapis.com/index.html)


## Install required tools

```bash
sudo yum install -y rpm-build rpmdevtools
```

## Create required directory structure

```bash
rpmdev-setuptree
```

## Copy repo stuff to rpmbuild directory tree

```bash
cp -r path/repo/rpmbuild/* ~/rpmbuild
```

# Prepare source archive

```bash
wget http://selenium-release.storage.googleapis.com/2.44/selenium-server-standalone-2.44.0.jar -O ~/rpmbuild/SOURCES/selenium-server-standalone-2.44.0.jar

tar -czf ~/rpmbuild/SOURCES/selenium-webdriver.tar.gz ~/rpmbuild/SOURCES/selenium-server-standalone-2.44.0.jar ~/rpmbuild/SOURCES/selenium-hub ~/rpmbuild/SOURCES/selenium-node
```

## Build the RPM

```bash
rpmbuild -bb ~/rpmbuild/SPECS/selenium-webdriver.spec
```
