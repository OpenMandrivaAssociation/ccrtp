%define api 1.6
%define major 1
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary: 	Common C++ RTP stack
Name: 	 	ccrtp
Version: 	1.6.2
Release: 	%mkrel 3
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnu.org/software/ccrtp/
Source0:	ftp://ftp.gnu.org/pub/gnu/ccrtp/%{name}-%{version}.tar.gz
BuildRequires:	autoconf2.5
BuildRequires:	libCommonC++-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	doxygen
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Common C++ RTP stack

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries
Provides:	%{name} = %version
Obsoletes:	%{mklibname ccrtp 1} < %{version}-%{release}

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
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
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%post -n %{develname}
%_install_info %{name}.info

%postun -n %{develname}
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_infodir}/*


