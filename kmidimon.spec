Summary:	KDE MIDI Monitor for ALSA Sequencer
Name:		kmidimon
Version:	0.7.5
Release:	2
License:	GPLv2+
Group:		Sound
Url:		http://kmetronome.sourceforge.net/kmidimon/
Source0:	http://sourceforge.net/projects/kmidimon/files/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(alsa) >= 1.0.0
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(drumstick-alsa) >= 0.5.0
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(x11)
Requires:	drumstick >= 0.5.0
Requires:	oxygen-icon-theme

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
%setup -q
# make sure that the bundled drumstick isn't used
rm -rf drumstick

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

desktop-file-install --vendor="" \
		--add-category Application \
		--remove-category Music \
		--dir %{buildroot}%{_kde_applicationsdir} %{buildroot}%{_kde_applicationsdir}/%{name}.desktop

%find_lang %{name} --with-html --with-man

