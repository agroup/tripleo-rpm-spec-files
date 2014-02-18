%global commit 3a72756a6460a0d4a7112c4d7d2f098dd36f488c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global repo_name instack

Name:             python-instack
Version:          0.0.1
Release:          1%{?dist}
Summary:          OpenStack installation tool for diskimage-builder style elements
Group:            Development/Languages
License:          ASL 2.0
URL:              https://github.com/slagle/instack
Source0:          https://github.com/slagle/instack/releases/download/%{version}/instack-%{shortcommit}.tar.gz

BuildArch:        noarch
BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-d2to1
BuildRequires:    python-pbr

Requires:         python-argparse
Requires:         diskimage-builder

%description
Instack is an installation tool for diskimage-builder style elements. It
installs the the elements onto the running system, and can be used to install
OpenStack locally from both diskimage-builder elements and
openstack-tripleo-image-elements.

%prep
%setup -q -n %{repo_name}-%{shortcommit}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.md
%doc LICENSE
%{_bindir}/instack
%{python_sitelib}/instack
%{python_sitelib}/*.egg-info

%changelog
* Tue Feb 18 2014 James Slagle <jslagle@redhat.com>
- Initial rpm build.
