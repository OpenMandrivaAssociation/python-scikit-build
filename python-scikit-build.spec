Name:		python-scikit-build
Version:	0.18.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/scikit-build/scikit_build-%{version}.tar.gz
Summary:	Improved build system generator for Python C/C++/Fortran/Cython extensions
URL:		https://pypi.org/project/scikit-build/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildArch:	noarch

%description
Improved build system generator for Python C/C++/Fortran/Cython extensions

%prep
%autosetup -p1 -n scikit_build-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/skbuild
%{py_sitedir}/scikit_build-*.*-info
