%global modname ldap3

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{modname}
Version:        2.4.1
Release:        3%{?dist}
Summary:        Strictly RFC 4511 conforming LDAP V3 pure Python client

License:        LGPLv2+
URL:            https://github.com/cannatag/ldap3
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

Patch0002:      0002-unbundle-ordereddict.patch

BuildArch:      noarch

%global _description \
ldap3 is a strictly RFC 4510 conforming LDAP V3 pure Python client library.

%description %{_description}

%package     -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-pyasn1
Requires:       python-backports-ssl_match_hostname

%description -n python2-%{modname} %{_description}

Python 2 version.

%if 0%{?with_python3}
%package     -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-pyasn1
Requires:       python2-backports-ssl_match_hostname

%description -n python3-%{modname} %{_description}

Python 3 version.
%endif

%prep
%autosetup -n %{modname}-%{version} -p1
# remove bundled ordereddict
rm -vf %{modname}/utils/ordDict.py

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-%{modname}
%license COPYING.LESSER.txt
%doc README.rst
%{python2_sitelib}/%{modname}-*.egg-info/
%{python2_sitelib}/%{modname}/

%if 0%{?with_python3}
%files -n python3-%{modname}
%license COPYING.LESSER.txt
%doc README.rst
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/
%endif

%changelog
* Tue Jan 30 2018 Alfredo Moralejo <amoralej@redhat.com> - 2.4.1-3
- Fixed dependencies names for CentOS.

* Tue Jan 30 2018 Alfredo Moralejo <amoralej@redhat.com> - 2.4.1-2
- Disable python3 builds for non-Fedora builders.

* Tue Jan 23 2018 Igor Gnatenko <ignatenko@redhat.com> - 2.4.1-1
- Update to 2.4.1

* Thu Nov 16 2017 Michal Cyprian <mcyprian@redhat.com> - 2.4-1
- Update to 2.4

* Tue Oct 24 2017 Michal Cyprian <mcyprian@redhat.com> - 2.3-3
- Remove no longer necessary unbundle-ssl patch
Resolves: rhbz#1494151

* Thu Sep 21 2017 Ralph Bean <rbean@redhat.com> - 2.3-2
- Fix patch to require correct backports package name on el7.

* Wed Sep 20 2017 Michal Cyprian <mcyprian@redhat.com> - 2.3-1
- Update to 2.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Michal Cyprian <mcyprian@redhat.com> - 2.2.3-1
- Update to 2.2.3

* Sun Mar 19 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Thu Feb 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

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
