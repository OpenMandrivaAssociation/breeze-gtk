%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
%undefine _empty_manifest_terminate_build

Summary:	The Breeze theme for GTK+ windows
Name:		breeze-gtk
Version:	5.26.3
Release:	1
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
# FIXME this is a really weird issue: On aarch64, the
# build fails with a crash in pycairo, but as soon as
# any sort of debugging is enabled, the problem goes
# away.
# This is obviously not the right "fix" - but in the
# mean time, it does allow the package to be built and
# if the problem returns, at least we'll get some
# information about it.
Patch0:		debug.patch
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
Supplements:	gtk+2.0
Supplements:	gtk2-modules

%description
This package contains a version of the KDE Breeze theme for GTK applications
and environments, such as GNOME.

%files
%{_datadir}/themes/Breeze
%{_datadir}/themes/Breeze-Dark

#-----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
