%global commit d305ad25f2538d829465092146de5cdfb4a803d8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global alphatag 20140220git
%global repo_name tripleo-incubator

Name:			openstack-tripleo
Version:		0.0.1
Release:		1.%{alphatag}%{?dist}
Summary:		OpenStack TripleO

Group:			Applications/System
License:		ASL 2.0
URL:			https://wiki.openstack.org/wiki/TripleO
Source0:		https://github.com/openstack/%{repo_name}/archive/%{commit}.tar.gz

# Upstream patch: https://review.openstack.org/#/c/74452/
Patch0001:		0001-Add-shebang.patch
# Upstream switched to oslosphinx in https://review.openstack.org/#/c/73353/,
# but that does not yet exist in Fedora.
Patch0002:		0002-Switch-back-to-oslo.sphinx.patch

BuildArch:		noarch

BuildRequires:		python-sphinx
BuildRequires:		python-oslo-sphinx

%description
TripleO is a program aimed at installing, upgrading and operating OpenStack
clouds using OpenStack's own cloud facilities as the foundations - building on
nova, neutron and heat to automate fleet management at datacenter scale.

%package doc
Summary:		Documentation for OpenStack TripleO
Group:			Documentation

Requires:		%{name} = %{version}-%{release}

BuildArch:		noarch

BuildRequires:		python-sphinx

%description	doc
TripleO is a program aimed at installing, upgrading and operating OpenStack
clouds using OpenStack's own cloud facilities as the foundations - building on
nova, neutron and heat to automate fleet management at datacentre scale.

This package contains documentation files for TripleO.

%prep
%setup -q -n %{repo_name}-%{commit}

%patch0001 -p1
%patch0002 -p1

%install
# scripts
install -d -m 755 %{buildroot}/%{_bindir}
install -p -m 755 -t %{buildroot}/%{_bindir} scripts/* 
# extract-docs.awk and extract-docs are only used for building docs, we don't
# need them installed
rm -f %{buildroot}/%{_bindir}/extract-docs*

# rc files
install -d -m 755 %{buildroot}/%{_sysconfdir}/tripleo
install -p -m 644 -t %{buildroot}/%{_sysconfdir}/tripleo cloudprompt
install -p -m 644 -t %{buildroot}/%{_sysconfdir}/tripleo seedrc
install -p -m 644 -t %{buildroot}/%{_sysconfdir}/tripleo undercloudrc
install -p -m 644 -t %{buildroot}/%{_sysconfdir}/tripleo overcloudrc
install -p -m 644 -t %{buildroot}/%{_sysconfdir}/tripleo overcloudrc-user

# templates
install -d -m 755 %{buildroot}/%{_datarootdir}/tripleo/templates
install -p -m 644 -t %{buildroot}/%{_datarootdir}/tripleo/templates templates/*

# libvirt templates
install -d -m 755 %{buildroot}/%{_datarootdir}/tripleo/libvirt-templates
install -p -m 644 -t %{buildroot}/%{_datarootdir}/tripleo/libvirt-templates libvirt-templates/*

# documentation
sphinx-build -b html doc/source doc/build/html
install -d -m 755 %{buildroot}%{_datarootdir}/doc/tripleo/html
cp -r doc/build/html/* %{buildroot}%{_datarootdir}/doc/tripleo/html

%files
%doc LICENSE README.md
%{_bindir}/*
%config %{_sysconfdir}/tripleo
%{_datarootdir}/tripleo

%files doc
%{_datarootdir}/doc/tripleo

%changelog
* Mon Feb 17 2014 James Slagle <jslagle@redhat.com> 0.0.1-1.20140211git
- Updates to spec file to match Fedora packaging guidelines.

* Mon Sep 23 2013 Ryan Brady <rbrady@redhat.com> 0.0.1-1
- Initial RPM build
