%define		module	pyaudio
Summary:	Python bindings for PortAudio
Name:		python-%{module}
Version:	0.2.4
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://people.csail.mit.edu/hubert/pyaudio/packages/%{module}-%{version}.tar.gz
# Source0-md5:	623809778f3d70254a25492bae63b575
URL:		http://people.csail.mit.edu/hubert/pyaudio/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-libs
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyAudio provides Python bindings for PortAudio, the cross-platform
audio I/O library. With PyAudio, you can easily use Python to play
and record audio on a variety of platforms.

PyAudio is designed to work with the PortAudio v19 API 2.0. Note that
PyAudio currently only supports blocking-mode audio I/O.

%prep
%setup -q -n PyAudio-%{version}

%build
# CC/CFLAGS is only for arch packages - remove on noarch packages
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README docs/*
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/PyAudio-*.egg-info
