Name:		openstack-tripleo-heat-templates
Summary:	Heat templates for TripleO
Version:	0.4.2
Release:	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:	http://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{version}.tar.gz

# Roll back the switch to use OS::Heat::UpdateWaitConditionHandle, since RDO
# openstack-heat does not yet have that functionality.
Patch0001:	0001-WaitConditionHandle.patch

# Per: # https://github.com/openstack/tripleo-image-elements/tree/master/elements/qpidd,
# this patch sed's the templates to switch them all over to use qpid, which is
# the default we want for RDO.
Patch0002:	0002-use-qpid.patch

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
