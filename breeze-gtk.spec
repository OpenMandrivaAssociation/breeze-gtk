%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	The Breeze theme for GTK+ windows
Name:		breeze-gtk
Version:	5.9.5
Release:	1
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	gtk2-modules
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
%{_libdir}/kconf_update_bin/gtkbreeze5*
%{_datadir}/kconf_update/gtkbreeze5*.upd

#-----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5 -DWITH_GTK3_VERSION=3.20

%build
%ninja -C build

%install
%ninja_install -C build
