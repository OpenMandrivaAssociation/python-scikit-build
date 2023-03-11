Name:		python-scikit-build
Version:	0.16.7
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/scikit-build/scikit-build-%{version}.tar.gz
Summary:	Improved build system generator for Python C/C++/Fortran/Cython extensions
URL:		https://pypi.org/project/scikit-build/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Improved build system generator for Python C/C++/Fortran/Cython extensions

%prep
%autosetup -p1 -n scikit-build-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/skbuild
%{py_sitedir}/scikit_build-*.*-info
