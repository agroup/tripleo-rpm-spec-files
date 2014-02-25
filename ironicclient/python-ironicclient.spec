Name:           python-ironicclient
Version:        0.1.2
Release:        1%{?dist}
Summary:        Python client for Ironic

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-ironicclient
Source0:        https://pypi.python.org/packages/source/p/python-ironicclient/python-ironicclient-0.1.2.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

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

rm -rf python_ironicclient.egg-info
# Let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt


%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
rm -rf %{buildroot}%{python2_sitelib}/python_ironicclient*


%files
%{_bindir}/*
%{python2_sitelib}/ironicclient*
%doc LICENSE README.rst


%changelog

* Tue Feb 25 2014 Angus Thomas <athomas@redhat.com> - 0.1.2-1
- Initial package.
