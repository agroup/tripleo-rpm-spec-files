%global gitinfo a617.g3d6b1d4

Name:		tripleo-image-elements
Summary:	Elements for diskimage-builder targeting Openstack/Heat images
Version:	0.0.1
Release:	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:	https://github.com/cybertron/tripleo-puppet-elements/releases/download/%{version}/tripleo-image-elements-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python-setuptools

Requires: diskimage-builder

%prep
%setup -q -n %{name}-%{version}.%{gitinfo}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%description
Components of TripleO that are responsible for building disk images.

%files
%doc LICENSE
%doc README.md
%doc AUTHORS
%doc ChangeLog
%doc docs/ci.md
%{python_sitelib}/tripleo_image_elements*
%{_datadir}/%{name}

%changelog
* Tue Sep 17 2013 Ben Nemec <bnemec@redhat.com> - 0.0.1-1
- First build of puppetized image elements
