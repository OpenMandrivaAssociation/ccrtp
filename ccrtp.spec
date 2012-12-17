%define api	2.0
%define major	0
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} -d

Summary: 	Common C++ RTP stack
Name: 	 	ccrtp
Version: 	2.0.5
Release: 	1
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnu.org/software/ccrtp/
Source0:	ftp://ftp.gnu.org/pub/gnu/ccrtp/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/pub/gnu/ccrtp/%{name}-%{version}.tar.gz.sig

BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	pkgconfig(libccgnu2)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(ucommon)

%description
Common C++ RTP stack

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries
Provides:	%{name} = %{EVRD}
Obsoletes:	%{mklibname ccrtp 1} < %{EVRD}

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{devname}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname -d ccrtp 1.5}

%description -n %{devname}
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
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_infodir}/*

