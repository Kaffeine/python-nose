# Adapted from Fedora's packaging (2018-01-16)
# https://src.fedoraproject.org/cgit/rpms/python-nose.git/plain/python-nose.spec

%global modname nose

Name:           python-nose
Version:        1.3.7
Release:        1
BuildArch:      noarch

License:        LGPLv2+ and Public Domain
Summary:        Discovery-based unit test extension for Python
URL:            https://nose.readthedocs.org/en/latest/
Group:          Development/Libraries
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-setuptools

%description
nose extends the test loading and running features of unit test, making
it easier to write, find and run tests.

By default, nose will run tests in files or directories under the
current working directory whose names include "test" or "Test" at a
word boundary (like "test_this" or "functional_test" or "TestClass"
but not "libtest"). Test output is similar to that of unit test, but
also includes captured stdout output from failing tests, for easy
print-style debugging.

These features, and many more, are customizable through the use of
plugins. Plugins included with nose provide support for doctest, code
coverage and profiling, flexible attribute-based test selection,
output capture and more.

%package docs
Summary:        Nose Documentation

%description docs
Documentation for Nose.

This package installs the nose module and nosetests program that can discover
python unit tests.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
install -d %{buildroot}%{_mandir}
mv %{buildroot}%{_prefix}/man/man1 %{buildroot}%{_mandir}

%files
%{_bindir}/nosetests
%{_bindir}/nosetests-2.*
%{python_sitearch}/nose-*.egg-info/
%{python_sitearch}/nose/

%files docs
%doc lgpl.txt
%doc AUTHORS CHANGELOG examples NEWS README.txt
%{_mandir}/man1/nosetests.*
