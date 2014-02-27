Name:           python-ironicclient
Version:        0.1.2
Release:        2%{?dist}
Summary:        Python client for Ironic

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-ironicclient
Source0:        http://tarballs.openstack.org/python-ironicclient/python-ironicclient-0.1.2.tar.gz

Patch0001:	0001-ironicclient-Remove-runtime-dependency-on-python-pbr.patch
Patch0002:	0002-ironicclient-Prevent-pbr-dependencies-handling.patch

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools

Requires:       python-prettytable
Requires:       python-keystoneclient
Requires:       python-six
Requires:       python-stevedore
Requires:       python-anyjson
Requires:       python-httplib2
Requires:       python-lxml

%description
A python and command line client library for Ironic.

%prep
%setup -q -n %{name}-%{version}

%patch0001 -p1
%patch0002 -p1


%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%{_bindir}/*
%{python2_sitelib}/ironicclient*
%{python2_sitelib}/python_ironicclient*
%doc LICENSE README.rst


%changelog

* Wed Feb 26 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-2
- Added patches to remove pbr dependency
- Updated the source URL
- Removed deletion of python_ironicclient.egg-info

* Tue Feb 25 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-1
- Initial package.
