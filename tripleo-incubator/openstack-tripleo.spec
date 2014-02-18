%global commit e8f0ee3b9a66c6c64bb7f2017baec0f68b4f2764
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global repo_name tripleo-incubator

Name:           openstack-tripleo
Version:        0.0.1
Release:        1%{?dist}
Summary:        OpenStack TripleO

Group:          Applications/System
License:        ASL 2.0
URL:            https://wiki.openstack.org/wiki/TripleO
Source0:        https://github.com/openstack/%{repo_name}/archive/%{commit}.tar.gz

BuildArch:      noarch

BuildRequires:    python-sphinx
BuildRequires:    python-oslo-sphinx

%description
TripleO is a program aimed at installing, upgrading and operating OpenStack
clouds using OpenStack's own cloud facilities as the foundations - building on
nova, neutron and heat to automate fleet management at datacentre scale.

%package doc
Summary:          Documentation for OpenStack TripleO
Group:            Documentation

Requires:         %{name} = %{version}-%{release}

BuildRequires:    python-sphinx

%description      doc
TripleO is a program aimed at installing, upgrading and operating OpenStack
clouds using OpenStack's own cloud facilities as the foundations - building on
nova, neutron and heat to automate fleet management at datacentre scale.

This package contains documentation files for TripleO.

%prep
%setup -q -n %{repo_name}-%{commit}

%install
# scripts
install -d -m 755 %{buildroot}/%{_bindir}
install -p -m 755 -t %{buildroot}/%{_bindir} scripts/* 

# rc files
install -d -m 755 %{buildroot}/%{_sysconfdir}/tripleo
install -p -m 644 -t %{buildroot}/%{_sysconfdir}/tripleo cloudprompt
install -p -m 644 -t %{buildroot}/%{_sysconfdir}/tripleo seedrc
install -p -m 644 -t %{buildroot}/%{_sysconfdir}/tripleo undercloudrc
install -p -m 644 -t %{buildroot}/%{_sysconfdir}/tripleo overcloudrc
install -p -m 644 -t %{buildroot}/%{_sysconfdir}/tripleo overcloudrc-user

# templates
install -d -m 755 %{buildroot}/%{_datarootdir}/tripleo/templates
install -p -m 755 -t %{buildroot}/%{_datarootdir}/tripleo/templates templates/*

# libvirt templates
install -d -m 755 %{buildroot}/%{_datarootdir}/tripleo/libvirt-templates
install -p -m 755 -t %{buildroot}/%{_datarootdir}/tripleo/libvirt-templates libvirt-templates/*

# documentation
sphinx-build -b html doc/source doc/build/html
install -d -m 755 %{buildroot}%{_datarootdir}/doc/tripleo/html
cp -r doc/build/html/* %{buildroot}%{_datarootdir}/doc/tripleo/html

%files
%{_bindir}/*
%{_sysconfdir}/tripleo/*
%{_datarootdir}/tripleo/templates/*
%{_datarootdir}/tripleo/libvirt-templates/*

%files doc
%{_datarootdir}/doc/tripleo

%changelog
* Mon Feb 17 2014 James Slagle <jslagle@redhat.com> 0.0.2
- Updates to spec file to match Fedora packaging guidelines.

* Mon Sep 23 2013 Ryan Brady <rbrady@redhat.com> 0.0.1
- Initial RPM build
