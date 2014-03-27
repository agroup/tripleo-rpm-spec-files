Name:		openstack-tripleo-heat-templates
Summary:	Heat templates for TripleO
Version:	0.4.2
Release:	4%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:	http://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{version}.tar.gz

# Not yet submitted upstream
# Add BlockStorage0Config and enable_tunneling to block-storage and
# swift-storage-source ovs metadata sections.
# https://review.openstack.org/83416
# https://review.openstack.org/83417
Patch0001:	0001-Add-BlockStorageConfig0.patch

# https://review.openstack.org/#/c/82803/
# git format-patch -1 55722cc7fa4624e4738bb695348955745e297649
Patch0002:	0002-Expose-dnsmasq-options.patch

# Per: # https://github.com/openstack/tripleo-image-elements/tree/master/elements/qpidd,
# this patch sed's the templates to switch them all over to use qpid, which is
# the default we want for RDO.
Patch0003:	0003-use-qpid.patch

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-d2to1
BuildRequires:	python-pbr

Requires:	PyYAML

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.

%prep
%setup -q -n tripleo-heat-templates-%{version}

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
cp -ar *.yaml %{buildroot}/%{_datadir}/%{name}

%files
%doc README.md LICENSE examples
%{python2_sitelib}/tripleo_heat_merge
%{python2_sitelib}/tripleo_heat_templates-%{version}*.egg-info
%{_datadir}/%{name}
%{_bindir}/tripleo-heat-merge

%changelog
* Thu Mar 27 2014 James Slagle <jslagle@redhat.com> - 0.4.2-4
- Update patch 0001-Add-BlockStorageConfig0.patch to include NeutronNetworkType
  parameter.

* Wed Mar 26 2014 James Slagle <jslagle@redhat.com> - 0.4.2-3
- Update patches

* Tue Mar 25 2014 James Slagle <jslagle@redhat.com> - 0.4.2-2
- Add patch 0003-Expose-dnsmasq-options.patch

* Mon Mar 24 2014 James Slagle <jslagle@redhat.com> - 0.4.2-1
- Bump to 0.4.2.

* Fri Mar 21 2014 James Slagle <jslagle@redhat.com> - 0.4.1-1
- Rebase onto 0.4.1.
- Add patch to switch from rabbit to qpid as default message bus

* Wed Mar 12 2014 James Slagle <jslagle@redhat.com> - 0.4.0-2
- Remove python BuildRequires
- Switch __python to __python2 macro
- Switch python_sitelib to python2_sitelib macro
- Use doc macro for README.md, LICENSE, and examples
- Use name macro when copying templates in install

* Mon Feb 17 2014 James Slagle <jslagle@redhat.com> - 0.4.0-1
- Update spec file for Fedora Packaging 

* Thu Sep 19 2013 Ben Nemec <bnemec@redhat.com> - 0.0.1-1
- First build of tripleo-heat-templates
