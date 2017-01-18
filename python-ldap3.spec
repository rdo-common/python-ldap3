%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%global modname ldap3

Name:           python-%{modname}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Strictly RFC 4511 conforming LDAP V3 pure Python client

License:        LGPLv2+
URL:            https://github.com/cannatag/ldap3
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

Patch0001:      0001-unbundle-ssl.patch
Patch0002:      0002-unbundle-ordereddict.patch

BuildArch:      noarch

%global _description \
ldap3 is a strictly RFC 4510 conforming LDAP V3 pure Python client library.

%description %{_description}

%package     -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-setuptools
Requires:       python-pyasn1
%else
BuildRequires:  python2-setuptools
Requires:       python2-pyasn1
%endif

%description -n python2-%{modname} %{_description}

Python 2 version.

%if %{with python3}
%package     -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-pyasn1

%description -n python3-%{modname} %{_description}

Python 3 version.
%endif

%prep
%autosetup -n %{modname}-%{version} -p1
# remove bundled ssl
rm -vf %{modname}/utils/tls_backport.py docs/manual/source/%{modname}.utils.tls_backport.rst
# remove bundled ordereddict
rm -vf %{modname}/utils/ordDict.py

%build
%py2_build
%if %{with python3}
%py3_build
%endif

%install
%py2_install
%if %{with python3}
%py3_install
%endif

%files -n python2-%{modname}
%license COPYING.LESSER.txt
%doc README.rst
%{python2_sitelib}/%{modname}-*.egg-info/
%{python2_sitelib}/%{modname}/

%if %{with python3}
%files -n python3-%{modname}
%license COPYING.LESSER.txt
%doc README.rst
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/
%endif

%changelog
* Wed Jan 18 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Mon Jan 02 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.1-1
- Update to 2.1.1
- Modernize spec

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.8.6-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Michal Cyprian <mcyprian@redhat.com> - 0.9.8.6-3
- Replace macro define with global

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

 * Wed Jul 08 2015 Michal Cyprian <mcyprian@redhat.com> - 0.9.8.6-1
 - Initial release of RPM package
