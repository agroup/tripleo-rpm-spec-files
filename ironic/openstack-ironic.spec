%global release_name icehouse
%global release_letter b
%global milestone 2
%global full_release ironic-%{version}.%{release_letter}%{milestone}
%global sname ironic


Name:		openstack-ironic
Summary:	OpenStack Baremetal Hypervisor API (ironic)
Version:	2014.1
Release:	%{release_letter}%{milestone}.2%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		http://www.openstack.org
Source0:	https://launchpad.net/ironic/%{release_name}/%{release_name}-%{milestone}/+download/%{full_release}.tar.gz
Provides:	ironic

Source1:        openstack-ironic-api.service
Source2:        openstack-ironic-conductor.service

BuildArch: noarch
BuildRequires: python-setuptools
BuildRequires: python-pbr
BuildRequires: python-devel
BuildRequires: openssl-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: gmp-devel
BuildRequires: python-sphinx

Requires: swig
Requires: python-pbr
Requires: python-eventlet
Requires: python-fixtures
Requires: python-iso8601
Requires: python-jsonpatch
Requires: python-kombu
Requires: python-anyjson
Requires: python-migrate
Requires: python-mock
Requires: python-netaddr
Requires: python-paramiko
Requires: python-pecan
Requires: pyflakes
Requires: python-stevedore
Requires: python-wsme
Requires: pycrypto
Requires: python-sqlalchemy
Requires: python-neutronclient
Requires: python-glanceclient
Requires: python-keystoneclient
Requires: python-jinja2
Requires(pre): shadow-utils

%description
Ironic provides an API for management and provisioning of physical machines



%prep
%setup -q -n %{full_release}

# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

#Relocate the default sqlite DB
sed -i 's/^#connection=/connection=/' etc/ironic/ironic.conf.sample
sed -i 's/ironic\/openstack\/common\/db/var\/lib\/ironic/' etc/ironic/ironic.conf.sample

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}


# install systemd scripts
mkdir -p %{buildroot}/usr/lib/systemd/system/
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/systemd/system/
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_prefix}/lib/systemd/system/

mkdir -p %{buildroot}%{_sharedstatedir}/ironic/
mkdir -p %{buildroot}%{_sysconfdir}/ironic/rootwrap.d

#Populate the conf dir
install -p -D -m 640 %{_builddir}/%{full_release}/etc/ironic/ironic.conf.sample %{buildroot}/%{_sysconfdir}/ironic/ironic.conf
install -p -D -m 640 %{_builddir}/%{full_release}/etc/ironic/policy.json %{buildroot}/%{_sysconfdir}/ironic/policy.json
install -p -D -m 640 %{_builddir}/%{full_release}/etc/ironic/rootwrap.conf %{buildroot}/%{_sysconfdir}/ironic/rootwrap.conf
install -p -D -m 640 %{_builddir}/%{full_release}/etc/ironic/rootwrap.d/* %{buildroot}/%{_sysconfdir}/ironic/rootwrap.d/

%files
%{_bindir}/*
%{_prefix}/lib/systemd/system/*
%{python_sitelib}/ironic*
%config %attr(-,root,ironic) %{_sysconfdir}/ironic
%attr(-,ironic,ironic) %{_sharedstatedir}/ironic
%doc README.rst LICENSE

# TODO - Switch to a statid UID/GID allocation https://fedorahosted.org/fpc/ticket/396
%pre
getent group ironic >/dev/null || groupadd -r ironic
getent passwd ironic >/dev/null || \
    useradd -r -g ironic -d %{_sharedstatedir}/ironic -s /sbin/nologin \
-c "OpenStack Ironic Daemons" ironic
exit 0


%changelog
* Mon Feb 24 2014 Angus Thomas <athomas@redhat.com> - 2014.1-b2.2
- Removed /var/log/ironic from package
- Replaced hardcoded file paths with macros
- Added LICENSE and README.rst docs

* Fri Feb 21 2014 Angus Thomas <athomas@redhat.com> - 2014.1-b2.1
- Initial package build

