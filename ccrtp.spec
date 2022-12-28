%define major	3
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d
%define oldlibname	%mklibname %{name} 3

Summary:	Common C++ RTP stack
Name:		ccrtp
Version:	2.1.2
Release:	2
License:	GPLv2+
Group:		System/Libraries
Url:		https://www.gnu.org/software/ccrtp/
Source0:	https://ftp.gnu.org/pub/gnu/ccrtp/%{name}-%{version}.tar.gz
Source1:	https://ftp.gnu.org/pub/gnu/ccrtp/%{name}-%{version}.tar.gz.sig
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	pkgconfig(libccgnu2)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(ucommon)

%description
Common C++ RTP stack.

#----------------------------------------------------------------------------

%package -n 	%{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n %{libname}
Dynamic libraries from %{name}.

%files -n %{libname}
%{_libdir}/libccrtp.so.%{major}*

#----------------------------------------------------------------------------

%package -n 	%{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
# Intentionally unversioned, because libname should not contain version number
Obsoletes:	%{oldlibname}

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libccrtp.so
%{_libdir}/pkgconfig/*.pc
%{_infodir}/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
export CXXFLAGS="-fpermissive %{optflags}"
%configure
%make_build
# disable or we have 4.7.2/../../../../lib64/crti.o: No such file or directory
# why we use this?
# LIBTOOL=% _bindir/libtool

%install
%make_install

