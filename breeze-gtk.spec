Summary:	The Breeze theme for GTK+ windows
Name:		breeze-gtk
Version:	5.5.0.1
Release:	1
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildArch:	noarch
Conflicts:	gnome-breeze < 0.0.2
Obsoletes:	gnome-breeze < 0.0.2
Provides:	gnome-breeze = 0.0.2

%description
This package contains a version of the KDE Breeze theme for GTK applications
and environments, such as GNOME.

%files

#-----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
