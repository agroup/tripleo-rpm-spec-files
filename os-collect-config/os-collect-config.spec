Name:           os-collect-config
Version:        0.1.2
Release:        1%{?dist}
Summary:        Collect and cache metadata, run hooks on changes.

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.service

BuildArch:	noarch
BuildRequires:	python-setuptools

Requires:	python-setuptools
Requires:	python-argparse
Requires:	python-d2to1
Requires:	python-eventlet
Requires:	python-keystoneclient
Requires:	python-requests
Requires:	python-iso8601
Requires:	python-lxml
Requires:	python-six

%description
Python util to collect openstack heat metadata

%prep

%setup -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Install systemd service
install -p -D -m 0644 %{S:1} %{buildroot}%{_unitdir}/%{name}.service

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/os_collect_config/tests

%pre
if [ $1 -gt 1 ]; then
  # Upgrade - stop previous instance of os-collect-config 
  systemctl stop %{name}.service
fi

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-collect-config
%{python_sitelib}/os_collect_config*.egg-info
%{python_sitelib}/os_collect_config
%{_unitdir}/%{name}.service

%changelog
* Tue Oct 15 2013 Lucas Alvares Gomes <lgomes@redhat.com> - 0.1.2-1
- Update to version 0.1.2
* Tue Sep 06 2013 Lucas Alvares Gomes <lgomes@redhat.com> - 0.0.1-1
- Initial version
