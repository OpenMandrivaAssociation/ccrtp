%define major 0
%define libname %mklibname %{name} %major
%define develname %mklibname %{name} -d

Summary: 	Common C++ RTP stack
Name: 	 	ccrtp
Version: 	1.6.0
Release: 	%mkrel 1
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

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} = %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 

%description -n %{develname}
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


