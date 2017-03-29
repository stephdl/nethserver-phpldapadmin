%define name nethserver-phpldapadmin
%define version 0.0.3
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

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} %{buildroot}   \
   $RPM_BUILD_ROOT > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%clean 
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.3-1.ns7
- Template expansion on trusted-network

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.2-2.ns7
- GPL license

* Mon Feb 06 2017 stephane de labrusse <stephdl@de-labrusse.fr> - 0.0.2-1.ns7
- Corrected the php variable interpretation in config.php

* Wed Dec 14 2016 stephane de labrusse <stephdl@de-labrusse.fr> - 0.0.1-1.ns7
- First release to NS7
