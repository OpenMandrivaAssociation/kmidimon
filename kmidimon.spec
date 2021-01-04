Summary:	KDE MIDI Monitor for ALSA Sequencer
Name:		kmidimon
Version:	0.7.6
Release:	1
License:	GPLv2+
Group:		Sound
Url:		http://kmetronome.sourceforge.net/kmidimon/
#Source0:	http://sourceforge.net/projects/kmidimon/files/%{version}/%{name}-%{version}.tar.bz2

#Instead release, use latest git (git is still in active developing): https://sourceforge.net/p/kmidimon/code/HEAD/tree/trunk/
# For easy to use git as source, use source mirror from here. They even create source package:
Source0:	https://github.com/KottV/kmidimon/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:  qmake5
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(drumstick-alsa)
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:  cmake(Qt5LinguistTools)

%description
KMidimon is a MIDI monitor for the ALSA sequencer, based on the drumstick
library. It monitors events coming from a MIDI external port or application or
loaded from standard MIDI Files.

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_mandir}/man1/%{name}.1.xz
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/*/*
%{_datadir}/apps/*/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake

%make_build

%install
%make_install -C build

desktop-file-install --vendor="" \
		--add-category Application \
		--remove-category Music \
		--dir %{buildroot}%{_kde_applicationsdir} %{buildroot}%{_kde_applicationsdir}/%{name}.desktop

%find_lang %{name} --with-html --with-man

