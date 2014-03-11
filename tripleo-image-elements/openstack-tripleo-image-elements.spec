Name:		openstack-tripleo-image-elements
Summary:	OpenStack TripleO Image Elements for diskimage-builder
Version:	0.6.2
Release:	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:	http://tarballs.openstack.org/tripleo-image-elements/tripleo-image-elements-%{version}.tar.gz

# These have merged to master in tripleo-image-elements, but we don't yet have
# a rease for them.
# git format-patch c38c247e53b7812cfab5a36b26ddbc1a880d4df6^1...319c0a66fcb4113dec8a87247e338130573f36ae
Patch0001:      0001-Common-cinder-install-code.patch
Patch0002:      0002-Use-os-svc-restart-for-cinder-api.patch
Patch0003:      0003-Remove-unneeded-chown-of-var-run-nova.patch
Patch0004:      0004-Add-create-dir-service-for-neutron-ovs-agent.patch
Patch0005:      0005-Add-missing-x.patch
# git format-patch -1 4eccc8cc10eb7ae0ae9d24f7d5d02be4c05b0881
Patch0006:	0006-Make-log_file-and-notifier_strategy-configurable.patch

# The next 3 reviews have not merged upstream yet, but we need them.
# git review -d 76579 
# git format-patch -1 1105e565a0917feada1a7e74bf5fe49d8fb3a161
Patch0007:	0007-Work-around-missing-kombu-requirement-for-keystone.patch
# git format-patch -1 bddd2908b3f9758a8c6be9594599200101f5d7bb
Patch0008:	0008-Stop-using-the-os-svc-install-n-c-options.patch
# git format-patch -1 bddd2908b3f9758a8c6be9594599200101f5d7bb
Patch0009:	0009-Link-db-sync-utilities-to-usr-local-bin.patch

BuildArch:      noarch
BuildRequires:  python
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python-pbr

Requires:       diskimage-builder

%description
OpenStack TripleO Image Elements is a collection of elements for
diskimage-builder that can be used to build OpenStack images for the TripleO
program.

%prep
%setup -q -n tripleo-image-elements-%{version}

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

# remove .git-keep-empty files that get installed
find %{buildroot} -name .git-keep-empty | xargs rm -f

# These are the scripts created by our patches, but the patches don't bring +x
# along with them, so to avoid some rpmlint errors, +x them here. Once patches
# are marged upstream, these lines can be removed.
chmod +x %{buildroot}/%{_datarootdir}/tripleo-image-elements/neutron-dhcp-agent/install.d/neutron-package-install/80-neutron-dhcp-agent
chmod +x %{buildroot}/%{_datarootdir}/tripleo-image-elements/neutron-server/install.d/neutron-package-install/76-neutron
chmod +x %{buildroot}/%{_datarootdir}/tripleo-image-elements/fedora-rdo-icehouse/pre-install.d/10-rdo-icehouse-repo
chmod +x %{buildroot}/%{_datarootdir}/tripleo-image-elements/cinder/install.d/73-cinder
chmod +x %{buildroot}/%{_datarootdir}/tripleo-image-elements/swift-storage/install.d/76-swift-dirs

%files
%doc LICENSE
%doc README.md
%doc AUTHORS
%doc ChangeLog
%{python_sitelib}/tripleo_image_elements*
%{_datadir}/tripleo-image-elements

%changelog
* Tue Mar 11 2014 James Slagle <jslagle@redhat.com> - 0.6.2-1
* Bump to 0.6.2
- Remove some patchs that have merged upstream
- Spec file updates based on review

* Mon Feb 24 2014 James Slagle <jslagle@redhat.com> - 0.6.0-2
* Add patches for swift package support.

* Thu Feb 20 2014 James Slagle <jslagle@redhat.com> - 0.6.0-1
- Update to 0.6.0 upstream release.

* Mon Feb 17 2014 James Slagle <jslagle@redhat.com> - 0.5.1-1
- Initial rpm build.
