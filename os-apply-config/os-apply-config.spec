Name:           os-apply-config
Version:        0.1.2
Release:        1%{?dist}
Summary:        Config files from cloud metadata

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-setuptools

Requires:	pystache
Requires:	python-setuptools
Requires:	python-argparse
Requires:	python-anyjson

%description
Python util to apply openstack heat metadata to files

%prep

%setup -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/os_apply_config/tests

%files
%doc README.md
%doc LICENSE
%{_bindir}/os-apply-config
%{_bindir}/os-config-applier
%{python_sitelib}/os_apply_config*.egg-info
%{python_sitelib}/os_apply_config

%changelog
* Tue Oct 15 2013 Lucas Alvares Gomes <lgomes@redhat.com> - 0.1.2-1
- Update to version 0.1.2
* Tue Sep 06 2013 Lucas Alvares Gomes <lgomes@redhat.com> - 0.0.1-1
- Initial version
