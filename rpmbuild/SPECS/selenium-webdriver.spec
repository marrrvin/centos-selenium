
%define jar_name selenium-server-standalone
%define app_dir /usr/lib/selenium
%define app_user selenium
%define app_group selenium
%define log_dir /var/log/selenium

Name: selenium-webdriver
Version: 2.44.0
Release: 1
Summary: Selenium Webdriver Server
Group: Applications/System
BuildArch: noarch
License: Apache 2.0
URL: http://seleniumhq.org/
Packager: Sergei Orlov
Source0: %{jar_name}-%{version}.jar
Source1: selenium-hub
Source2: selenium-node

Requires: xorg-x11-server-Xvfb

Requires(pre): shadow-utils

%description
The Selenium Server is needed in order to run either Selenium RC style scripts or Remote Selenium Webdriver ones. The 2.x server is a drop-in replacement for the old Selenium RC server and is designed to be backwards compatible with your existing infrastructure.

# prevent repacking of jar (not needed)
%define __jar_repack %{nil}

%pre
getent group %{app_group} >/dev/null || groupadd -r %{app_group}
getent passwd %{app_user} >/dev/null || \
    useradd -r -g %{app_group} -s /sbin/nologin \
    -c "Selenium Webdriver system user" %{app_user}
exit 0

%install
rm -rf %{buildroot}

%{__install} -d -m 0755 %{buildroot}/%{app_dir}
%{__install} -m 0755 %{SOURCE0} %{buildroot}%{app_dir}
ln -s %{app_dir}/%{jar_name}-%{version}.jar %{buildroot}%{app_dir}/%{jar_name}.jar

%{__install} -d %{buildroot}%{_sysconfdir}/rc.d/init.d
%{__install} -m 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/rc.d/init.d/
%{__install} -m 0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/rc.d/init.d/

%{__install} -d -m 0755 %{buildroot}%{log_dir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{app_dir}/%{jar_name}-%{version}.jar
%{app_dir}/%{jar_name}.jar
%dir %{app_dir}
%{_sysconfdir}/rc.d/init.d/selenium-hub
%{_sysconfdir}/rc.d/init.d/selenium-node
%attr(0755,%{app_user},%{app_group}) %{log_dir}
