Name:           openstack-m-release
Version:        icehouse
Release:        2
Summary:        openstack-m repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            http://repos.fedorapeople.org/repos/openstack-m/openstack-m
Source0:        openstack-m-release.repo

BuildArch:      noarch


%description
This package contains the openstack-m repository


%install
install -p -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/openstack-m-release.repo


%files
%{_sysconfdir}/yum.repos.d/*.repo


%changelog
* Tue Mar 18 2014 James Slagle <jslagle@redhat.com> icehouse-2
- Added testing repository

* Tue Feb 18 2014 James Slagle <jslagle@redhat.com> icehouse-1
- Initial rpm build.
