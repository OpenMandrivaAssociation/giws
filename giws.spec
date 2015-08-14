Summary:	Generate C++ class wrappers to call Java methods/objects
Name:		giws
Version:	2.0.2
Release:	2
License:	CeCILL
Group:		Development/Python
Url:		http://www.scilab.org/giws/
Source0:	http://www.scilab.org/giws/download/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python2)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Giws is basically doing the same stuff as SWIG but the opposite.
Calling Java from C/C++ can be tricky: JNI calls are complicated 
especially when dealing with non primivite types or arrays, 
performance issues must be kept in mind all the time, 
the code can be redundant (checking exceptions, checking returns
of operations...).
Giws hides this complexity through a C++ class which wraps the
Java class.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS README LICENSE CHANGELOG
%{_bindir}/*
%py2_puresitedir/*


%changelog
* Fri Jan 21 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2011.0
+ Revision: 632073
- Update to giws 1.2.0

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 1.0.5-3mdv2011.0
+ Revision: 590803
- rebuild for py 2.7

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Wed Nov 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.5-1mdv2010.1
+ Revision: 464836
- update to new version 1.0.5

* Sat Aug 29 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.3-1mdv2010.0
+ Revision: 422298
- update to new version 1.0.3

* Sat May 09 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2010.0
+ Revision: 373875
- update to new version 1.0.2

* Sun Dec 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-2mdv2009.1
+ Revision: 320117
- rebuild for python-2.6

* Fri Nov 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-1mdv2009.1
+ Revision: 305596
- add source and spec files
- Created package structure for giws.

