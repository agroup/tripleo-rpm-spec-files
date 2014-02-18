Name:		openstack-tripleo-image-elements
Summary:	OpenStack TripleO Image Elements for diskimage-builder
Version:    0.5.1
Release:    1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:    http://tarballs.openstack.org/tripleo-image-elements/tripleo-image-elements-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python-setuptools

Requires: diskimage-builder

%description
OpenStack TripleO Image Elements is a collection of elements for
diskimage-builder that can be used to build OpenStack images for the TripleO
program.

%prep
%setup -q -n tripleo-image-elements-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%files
%doc LICENSE
%doc README.md
%doc AUTHORS
%doc ChangeLog
%{python_sitelib}/tripleo_image_elements*
%{_datadir}/tripleo-image-elements

%changelog
* Mon Feb 17 2013 James Slagle <jslagle@redhat.com> - 
- Initial rpm build.
