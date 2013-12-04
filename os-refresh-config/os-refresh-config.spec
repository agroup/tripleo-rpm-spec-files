Name:           os-refresh-config
Version:        0.0.2
Release:        1%{?dist}
Summary:        Refresh system configuration

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-setuptools

Requires:	python-setuptools
Requires:	python-argparse

%description
Python util to refresh openstack config changes to service

%prep

%setup -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/os_refresh_config/tests

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-refresh-config
%{python_sitelib}/os_refresh_config*.egg-info
%{python_sitelib}/os_refresh_config

%changelog
* Tue Oct 15 2013 Lucas Alvares Gomes <lgomes@redhat.com> - 0.0.2-1
- Update to version 0.0.2
* Tue Sep 06 2013 Lucas Alvares Gomes <lgomes@redhat.com> - 0.0.1-1
- Initial version
