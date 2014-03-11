Name:		openstack-tripleo-image-elements
Summary:	OpenStack TripleO Image Elements for diskimage-builder
Version:	0.6.0
Release:	3%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:	http://tarballs.openstack.org/tripleo-image-elements/tripleo-image-elements-%{version}.tar.gz

# git format-patch -1 8475d117d722bcbf919eb0f332f34c0dc7ace36b
Patch0001:	0001-Ability-to-add-create-dir-service-separately.patch
# git format-patch -1 865c02f71483195c8f27ec94689833eb00049df2
Patch0002:	0002-Add-create-dir-service-for-neutron.patch
# git format-patch -1 6cdec90acb28c62fa83b64611e8e8f8b5416c46e
Patch0003:	0003-Add-create-dir-service-for-nova.patch
# git format-patch -1 a2464f6635a322d003c4b4316c030e914cea42dd
Patch0004:	0004-Fix-neutron-package-install.patch
# git format-patch -1 eed1086f703609203b805f11bfe803c96cc8b8c6
Patch0005:	0005-Correct-owner-for-glance-api-log-file.patch
# git format-patch -1 9691188d6bd16d23db049fd769c9371365541d6e
Patch0006:	0006-Fix-glance-package-install-config.patch
# git format-patch -1 c579d9a6fcf80fcf407de6d603f127ef1953e25b
Patch0007:	0007-Add-fedora-rdo-icehouse-element.patch
# git format-patch -1 38c01c8470fafcb44c3d2eeb742b32d100148e88
Patch0008:	0008-Fix-typo.patch
# git format-patch -1 c2225e463aace57a5e1de9b70d5410c1620bc3ce
Patch0009:	0009-Install-lvm2-package-for-cinder.patch
# git format-patch -1 8d04847f5a0c841dd000877b5abf3ff5aa902293
Patch0010:	0010-Common-cinder-install-code.patch
# git format-patch -1 4d9c0e9573269f53a8f833539b6d56dd6936432b
Patch0011:	0011-Use-os-svc-restart-for-cinder-api.patch
# git format-patch -1 82d54ee87ba5ceed4000d4c86e042dbbe4c6e0e4
Patch0012:	0012-Remove-unneeded-chown-of-var-run-nova.patch
# git format-patch -1 566d60ad703852b40f13c810063fb365f95620d4
Patch0013:	0013-Add-create-dir-service-for-neutron-ovs-agent.patch
# git format-patch -1 88033ad64b3597f3cdc1b3c101b42076687e0c6a
Patch0014:	0014-Add-missing-x.patch
# git format-patch -1 cf07365002d83c5a5b9cd266a45acd0023c84610
Patch0015:	0015-Install-openstack-swift-object.patch
# git format-patch -1 d46a0a82626eb76b0aaafebbecc04a9ed729fad8
Patch0016:	0016-Add-needed-swift-storage-dirs-for-packaged-install.patch
# git format-patch -1 b13d01ec4bbac3e4b5e72b007cd3caa32b212d37
Patch0017:	0017-Add-missing-x.patch

BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-d2to1
BuildRequires:	python-pbr

Requires:	diskimage-builder

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
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1

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
* Tue Mar 11 2014 James Slagle <jslagle@redhat.com> - 0.6.0-3
- Update based on review feedback
- Added patch 0017-Add-missing-x.patch

* Mon Feb 24 2014 James Slagle <jslagle@redhat.com> - 0.6.0-2
- Add patches for swift package support.

* Thu Feb 20 2014 James Slagle <jslagle@redhat.com> - 0.6.0-1
- Update to 0.6.0 upstream release.

* Mon Feb 17 2014 James Slagle <jslagle@redhat.com> - 0.5.1-1
- Initial rpm build.
