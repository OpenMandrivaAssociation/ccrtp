%define major 1.5
%define libname %mklibname %{name} %major

#%define __libtoolize /bin/true

Summary: 	Common C++ RTP stack
Name: 	 	ccrtp
Version: 	1.5.1
Release: 	%mkrel 2
License:	GPL
Group:		System/Libraries
URL:		http://www.gnu.org/software/ccrtp/
Source0:	ftp://ftp.gnu.org/pub/gnu/ccrtp/%{name}-%{version}.tar.bz2
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
Provides:	%{name}
Obsoletes:	%{name} = %{version}-%{release}

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%{name}-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
export CXXFLAGS="-fpermissive"$CXXFLAGS
%configure2_5x
%make
										
%install
rm -rf %{buildroot}

%makeinstall

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libname}-devel
%_install_info %{name}.info

%postun -n %{libname}-devel
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_infodir}/*


