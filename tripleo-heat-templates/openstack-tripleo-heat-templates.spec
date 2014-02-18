Name:		openstack-tripleo-heat-templates
Summary:	Heat templates for TripleO
Version:	0.4.0
Release:	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:    http://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{version}.tar.gz


BuildArch: noarch
BuildRequires: python
BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-d2to1
BuildRequires: python-pbr

Requires: PyYAML

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.

%prep
%setup -q -n tripleo-heat-templates-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}
install -d -m 755 %{buildroot}/%{_datadir}/tripleo-heat-templates
cp -ar *.yaml %{buildroot}/%{_datadir}/tripleo-heat-templates

install -d -m 755 %{buildroot}/%{_datarootdir}/doc/tripleo-heat-templates 
cp -ar examples %{buildroot}/%{_datarootdir}/doc/tripleo-heat-templates
cp README.md %{buildroot}/%{_datarootdir}/doc/tripleo-heat-templates
cp LICENSE %{buildroot}/%{_datarootdir}/doc/tripleo-heat-templates

%files
%{python_sitelib}/tripleo_heat_merge
%{python_sitelib}/tripleo_heat_templates-%{version}*.egg-info
%{_datadir}/tripleo-heat-templates
%{_bindir}/tripleo-heat-merge

%doc %{_datarootdir}/doc/tripleo-heat-templates

%changelog
* Mon Feb 17 2013 James Slagle <jslagle@redhat.com> - 0.4.0
- Update spec file for Fedora Packaging 

* Thu Sep 19 2013 Ben Nemec <bnemec@redhat.com> - 0.0.1-1
- First build of tripleo-heat-templates
