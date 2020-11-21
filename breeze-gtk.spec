%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	The Breeze theme for GTK+ windows
Name:		breeze-gtk
Version:	5.20.3
Release:	2
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Breeze)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(pycairo)
BuildRequires:	gtk2-modules
BuildRequires:	sassc
Conflicts:	gnome-breeze < 0.0.2
Obsoletes:	gnome-breeze < 0.0.2
Provides:	gnome-breeze = 0.0.2
Requires:	gtk+2.0
Requires:	gtk2-modules

%description
This package contains a version of the KDE Breeze theme for GTK applications
and environments, such as GNOME.

%files
%{_datadir}/themes/Breeze
%{_datadir}/themes/Breeze-Dark

#-----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5 -DWITH_GTK3_VERSION=3.20

%build
%ninja -C build

%install
%ninja_install -C build
