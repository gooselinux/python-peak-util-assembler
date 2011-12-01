%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global packagename BytecodeAssembler

Name:           python-peak-util-assembler
Version:        0.5.1
Release:        1%{?dist}
Summary:        Generate Python code objects by "assembling" bytecode

Group:          Development/Languages
License:        Python or ZPLv2.1
URL:            http://pypi.python.org/pypi/BytecodeAssembler
Source0:        http://pypi.python.org/packages/source/B/%{packagename}/%{packagename}-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel
BuildRequires:  python-nose

Requires:       python-decoratortools >= 1.2
Requires:       python-peak-util-symbols >= 1.0

%description
peak.util.assembler is a simple bytecode assembler module that handles most
low-level bytecode generation details like jump offsets, stack size tracking,
line number table generation, constant and variable name index tracking, etc.
That way, you can focus your attention on the desired semantics of your
bytecode instead of on these mechanical issues.

In addition to a low-level opcode-oriented API for directly generating specific
Python bytecodes, this module also offers an extensible mini-AST framework for
generating code from high-level specifications.  This framework does most of
the work needed to transform tree-like structures into linear bytecode
instructions, and includes the ability to do compile-time constant folding.

%prep
%setup -q -n %{packagename}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%check
nosetests

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*

%changelog
* Wed Jul 14 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.1-1
- rebase to 0.5.1
- specfile cleanups
Resolves: rhbz#613190

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.5-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5-2
- Rebuild for Python 2.6

* Sun Aug  3 2008 Luke Macken <lmacken@redhat.com> - 0.5-1
- Initial package for Fedora
