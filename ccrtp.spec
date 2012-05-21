%define api 2.0
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary: 	Common C++ RTP stack
Name: 	 	ccrtp
Version: 	2.0.3
Release: 	1
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnu.org/software/ccrtp/
Source0:	ftp://ftp.gnu.org/pub/gnu/ccrtp/%{name}-%{version}.tar.gz
BuildRequires:	ucommon-devel
BuildRequires:	libCommonC++-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	doxygen

%description
Common C++ RTP stack

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries
Provides:	%{name} = %{EVRD}
Obsoletes:	%{mklibname ccrtp 1} < %{EVRD}

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides: 	lib%{name}-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname -d ccrtp 1.5}

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
export CXXFLAGS="-fpermissive %{optflags}"
%configure2_5x
%make LIBTOOL=%_bindir/libtool

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_infodir}/*
