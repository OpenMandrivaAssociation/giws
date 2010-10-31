Summary:	Generate C++ class wrappers to call Java methods/objects
Name:		giws
Version:	1.0.5
Release:	%mkrel 3
License:	CeCILL
Group:		Development/Python
Url:		http://www.scilab.org/giws/
Source0:	http://www.scilab.org/giws/download/%{name}-%{version}.tar.gz
BuildRequires:	python-devel
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
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS README LICENSE CHANGELOG
%{_bindir}/*
%py_puresitedir/*
