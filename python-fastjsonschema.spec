Name:		python-fastjsonschema
Version:	2.21.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/f/fastjsonschema/fastjsonschema-%{version}.tar.gz
Summary:	Fastest Python implementation of JSON schema
URL:		https://pypi.org/project/fastjsonschema/
License:	BSD
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Fastest Python implementation of JSON schema

%prep
%autosetup -p1 -n fastjsonschema-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/fastjsonschema
%{py_sitedir}/fastjsonschema-*.*-info
