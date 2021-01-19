%define name nethserver-phpldapadmin
%define version 1.0.3
%define release 1
Summary: Nethserver integration of phpldapadmin
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildArch: noarch

Requires: phpldapadmin
Requires: nethserver-httpd

BuildRequires: perl
BuildRequires: nethserver-devtools 

%description
Implementation of phpldapadmin for Nethserver
Access via: https://yourdomain/phpmyadmin.

%prep
%setup

%build
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

%{genfilelist} %{buildroot}   \
   $RPM_BUILD_ROOT > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update
%attr(0440,root,root) /etc/sudoers.d/50_nsapi_nethserver_phpldapadmin

%clean 
rm -rf $RPM_BUILD_ROOT

%postun
if [ $1 == 0 ] ; then
   /usr/bin/rm -f /etc/httpd/conf.d/phpldapadmin.conf
   /usr/bin/systemctl reload httpd
fi

%changelog
* Tue Jan 19 2021 stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.3-1
- Fix the pla_password_hash upgrade

* Sun Jul 05 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.2-1
- Remove http templates after rpm removal

* Thu Mar 05 2020  stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.1-1.ns7
- Fix bad sudoers permission

* Mon Oct 14 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.6-1.ns7
- cockpit. added to legacy apps

* Tue May 8 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.5-1.ns7
- Subscribe to the nethserver-sssd-save event

* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.4-1.ns7
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.3-1.ns7
- Template expansion on trusted-network

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.2-2.ns7
- GPL license

* Mon Feb 06 2017 stephane de labrusse <stephdl@de-labrusse.fr> - 0.0.2-1.ns7
- Corrected the php variable interpretation in config.php

* Wed Dec 14 2016 stephane de labrusse <stephdl@de-labrusse.fr> - 0.0.1-1.ns7
- First release to NS7
