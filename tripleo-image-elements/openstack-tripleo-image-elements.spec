Name:		openstack-tripleo-image-elements
Summary:	OpenStack TripleO Image Elements for diskimage-builder
Version:    0.5.1
Release:    1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:    http://tarballs.openstack.org/tripleo-image-elements/tripleo-image-elements-master.tar.gz

Patch0001:  0001-Add-create-dir-service-for-neutron.patch
Patch0002:  0002-Add-create-dir-service-for-nova.patch
Patch0003:  0003-Fix-neutron-package-install.patch
Patch0004:  0004-Correct-owner-for-glance-api-log-file.patch
Patch0005:  0005-Fix-glance-package-install-config.patch
Patch0006:  0006-Add-fedora-rdo-icehouse-element.patch
Patch0007:  0007-Fix-typo.patch
Patch0008:  0008-Install-lvm2-package-for-cinder.patch
Patch0009:  0009-Common-cinder-install-code.patch
Patch0010:  0010-Add-missing-x.patch

BuildArch: noarch
BuildRequires: python
BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-d2to1
BuildRequires: python-pbr

Requires: diskimage-builder

%description
OpenStack TripleO Image Elements is a collection of elements for
diskimage-builder that can be used to build OpenStack images for the TripleO
program.

%prep
%setup -q -n tripleo-image-elements-0.0.1.dev148.ga84a463

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1

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

%files
%doc LICENSE
%doc README.md
%doc AUTHORS
%doc ChangeLog
%{python_sitelib}/tripleo_image_elements*
%{_datadir}/tripleo-image-elements

%changelog
* Mon Feb 17 2014 James Slagle <jslagle@redhat.com> - 0.5.1-1
- Initial rpm build.
