%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif

%define pypi_name ldap3

Name:       python-%{pypi_name}
Version:    0.9.8.6
Release:    1%{?dist}
Summary:    Strictly RFC 4511 conforming LDAP V3 pure Python client

License:    LGPLv2+
URL:        https://pypi.python.org/pypi/%{pypi_name}/%{version}
Source0:    https://pypi.python.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

Patch0:     ssl_unbundle.patch

BuildArch:  noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%if %{with python3}
BuildRequires:  python3-devel
%endif # with pyhton3

Requires:   python-pyasn1

%description
python-%{pypi_name} is a strictly RFC 4511 conforming LDAP V3 pure Python client. 
The same codebase works with Python, Python 3, PyPy and PyPy3.

%if %{with python3}
%package    -n python3-%{pypi_name}
Summary:    Strictly RFC 4511 conforming LDAP V3 pure Python3 client


Requires:   python3-pyasn1

%description -n python3-%{pypi_name}
pyhton3-%{pypi_name} is a strictly RFC 4511 conforming LDAP V3 pure Python client. 
The same codebase works with Python, Python 3, PyPy and PyPy3.

%endif # with python3


%prep
%setup -qc
mv %{pypi_name}-%{version}/ python2
pushd python2
%patch0 -p1
rm -r %{pypi_name}.egg-info/
popd

%if %{with python3}
cp -a python2 python3
%endif # with python3


%build
pushd python2
%{__python2} setup.py build
popd
 
%if %{with python3}
pushd python3
%{__python3} setup.py build
 popd
%endif # with python3

%install
%if %{with python3}
pushd python3
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif # with python3

pushd python2
 %{__python2} setup.py install -O1 --skip-build --root %{buildroot}
popd


%files
%doc python2/README.rst python2/_version.json
%license python2/COPYING.txt python2/COPYING.LESSER.txt python2/LICENSE.txt
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}*.egg-info

%if %{with python3}
%files -n python3-%{pypi_name}
%doc python3/README.rst  python3/_version.json
%license python3/COPYING.txt python3/COPYING.LESSER.txt python3/LICENSE.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info
%endif # with python3

%changelog
 * Wed Jul 08 2015 Michal Cyprian <mcyprian@redhat.com> - 0.9.8.6-1
 - Initial release of RPM package
