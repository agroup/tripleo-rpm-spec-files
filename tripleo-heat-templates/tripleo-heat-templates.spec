%global commit b7f0bb6123f75c87e4da51f6bfa7a92a515a898c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		tripleo-heat-templates
Summary:	Heat templates for TripleO
Version:	0.0.1
Release:	1%{?dist}
License:	None
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:	https://github.com/openstack/tripleo-heat-templates/archive/%{commit}.tar.gz

BuildArch: noarch
BuildRequires: python
BuildRequires: PyYAML

%prep
%setup -q -n %{name}-%{commit}

%build
make overcloud.yaml

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp overcloud.yaml %{buildroot}%{_datadir}/%{name}

%description
TripleO Heat templates

%files
%doc README.md
%{_datadir}/%{name}

%changelog
* Thu Sep 19 2013 Ben Nemec <bnemec@redhat.com> - 0.0.1-1
- First build of tripleo-heat-templates
