%global commit 956943e37b91b22d739e9da6fe1a852e44581eff
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global alphatag 20140314git

Name:		instack-undercloud
Version:	0.0.1
Release:	0.1.%{alphatag}%{?dist}
Summary:	Installation tools to install an undercloud via python-instack

Group:		Development/Languages
License:	ASL 2.0
URL:		https://github.com/slagle/instack-undercloud
Source0:	https://github.com/slagle/%{name}/archive/%{commit}.tar.gz

BuildArch:	noarch

Requires:	python-instack


%description
instack-undercloud is a collection of installation tools to install an
undercloud via python-instack. It contains scripts and elements to complete the
installation.


%prep
%setup -q -n %{name}-%{commit}


%build
# nothing to build


%install
# elements
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
cp -ar elements/* %{buildroot}/%{_datadir}/%{name}
# scripts
install -d -m 755 %{buildroot}/%{_bindir}
cp -ar scripts/* %{buildroot}/%{_bindir}
# json files
cp -ar json-files %{buildroot}/%{_datadir}/instack-undercloud


%files
%doc README.md
%doc LICENSE
%doc instack-baremetal.answers.sample
%doc instack-virt.answers.sample
%{_datadir}/instack-undercloud
%{_bindir}/instack-install-undercloud
%{_bindir}/instack-install-undercloud-packages
%{_bindir}/instack-prepare-for-overcloud
%{_bindir}/instack-deploy-overcloud
%{_bindir}/instack-deploy-overcloud-tuskarcli
%{_bindir}/instack-test-overcloud


%changelog
* Thu Mar 13 2014 James Slagle <jslagle@redhat.com> 0.0.1-0.1.20140314git
- All scripts are now prefixed with instack-*
- Add new instack-deploy-overcloud-tuskarcli script
- Use _datadir macro instead of _datarootdir

* Wed Feb 26 2014 James Slagle <jslagle@redhat.com> 0.0.1-0.1.20140226git
- Add scripts for prepare-for-overcloud and test-overcloud

* Mon Feb 24 2014 James Slagle <jslagle@redhat.com> 0.0.1-0.1.20140224git
- Update install-undercloud-packages to account for new element location

* Mon Feb 24 2014 James Slagle <jslagle@redhat.com> 0.0.1-0.1.20140219git
- Use alphatag macro for the release.
- Update path where elements are installed.

* Tue Feb 18 2014 James Slagle <jslagle@redhat.com> 0.0.1-0.1
- Initial rpm build.
