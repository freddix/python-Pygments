Summary:	Generic syntax highlighter for general use
Name:		python-Pygments
Version:	1.6
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/P/Pygments/Pygments-%{version}.tar.gz
# Source0-md5:	a18feedf6ffd0b0cc8c8b0fbdb2027b1
URL:		http://pygments.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A generic syntax highlighter for general use in all kinds of software
such as forum systems, wikis or other applications that need to
prettify source code.

%prep
%setup -qn Pygments-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

install -D docs/pygmentize.1 \
	$RPM_BUILD_ROOT%{_mandir}/man1/pygmentize.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE TODO
%attr(755,root,root) %{_bindir}/pygmentize
%{py_sitescriptdir}/pygments
%{py_sitescriptdir}/*.egg-info
%{_mandir}/man1/pygmentize.1*

