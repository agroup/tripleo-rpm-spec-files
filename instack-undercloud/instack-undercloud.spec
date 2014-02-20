%global commit 45a841bbdab1cfeab839c19cf4a247a2d325a905
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global repo_name instack-undercloud

Name:		instack-undercloud
Version:	0.0.1
Release:	1%{?dist}
Summary:	Installation tools to install an undercloud via python-instack

Group:		Development/Languages
License:	ASL 2.0
URL:		https://github.com/slagle/instack-undercloud
Source0:        https://github.com/slagle/%{repo_name}/archive/%{commit}.tar.gz

BuildArch:      noarch

Requires:	python-instack


%description
instack-undercloud is a collection of installation tools to install an
undercloud via python-instack. It contains scripts and elements to complete the
installation.


%prep
%setup -q -n %{repo_name}-%{commit}


%build
# nothing to build


%install
# elements
install -d -m 755 %{buildroot}/%{_datarootdir}/instack-undercloud
cp -ar elements %{buildroot}/%{_datarootdir}/instack-undercloud
# scripts
install -d -m 755 %{buildroot}/%{_bindir}
cp -ar scripts/* %{buildroot}/%{_bindir}
# json files
cp -ar json-files %{buildroot}/%{_datarootdir}/instack-undercloud


%files
%doc README.md
%doc LICENSE
%doc instack-baremetal.answers.sample
%doc instack-virt.answers.sample
%{_datarootdir}/instack-undercloud
%{_bindir}/install-undercloud
%{_bindir}/install-undercloud-packages
%{_bindir}/deploy-overcloud
%{_bindir}/overcloud


%changelog
* Tue Feb 18 2014 James Slagle <jslagle@redhat.com>
- Initial rpm build.
