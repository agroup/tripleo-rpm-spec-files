Name:		openstack-tripleo-image-elements
Summary:	OpenStack TripleO Image Elements for diskimage-builder
Version:    0.6.0
Release:    1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:    http://tarballs.openstack.org/tripleo-image-elements/tripleo-image-elements-%{version}.tar.gz

Patch0001:  0001-Ability-to-add-create-dir-service-separately.patch
Patch0002:  0002-Add-create-dir-service-for-neutron.patch
Patch0003:  0003-Add-create-dir-service-for-nova.patch
Patch0004:  0004-Fix-neutron-package-install.patch
Patch0005:  0005-Correct-owner-for-glance-api-log-file.patch
Patch0006:  0006-Fix-glance-package-install-config.patch
Patch0007:  0007-Add-fedora-rdo-icehouse-element.patch
Patch0008:  0008-Fix-typo.patch
Patch0009:  0009-Install-lvm2-package-for-cinder.patch
Patch0010:  0010-Common-cinder-install-code.patch
Patch0011:  0011-Use-os-svc-restart-for-cinder-api.patch
Patch0012:  0012-Remove-unneeded-chown-of-var-run-nova.patch
Patch0013:  0013-Add-create-dir-service-for-neutron-ovs-agent.patch
Patch0014:  0014-Add-missing-x.patch

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
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1

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
* Thu Feb 20 2014 James Slagle <jslagle@redhat.com> - 0.6.0-1
- Update to 0.6.0 upstream release.

* Mon Feb 17 2014 James Slagle <jslagle@redhat.com> - 0.5.1-1
- Initial rpm build.
