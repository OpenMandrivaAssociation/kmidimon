Summary:		QT MIDI Monitor for ALSA Sequencer
Name:		kmidimon
Version:		1.4.1
Release:		1
License:		GPLv2+
Group:		Sound
Url:		https://kmidimon.sourceforge.io/index.shtml
Source0:	http://sourceforge.net/projects/kmidimon/files/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:		cmake >= 3.16
BuildRequires:		desktop-file-utils
BuildRequires:		gettext
BuildRequires:		gzip-utils
BuildRequires:		cmake(Qt6LinguistTools)
BuildRequires:		pkgconfig(alsa)
BuildRequires:		pkgconfig(dbus-1)
BuildRequires:		pkgconfig(drumstick-alsa) >= 2.10.0
BuildRequires:		pkgconfig(libart-2.0)
BuildRequires:		pkgconfig(Qt6Core) >= 6.2
BuildRequires:		pkgconfig(Qt6Core5Compat)
BuildRequires:		pkgconfig(Qt6Gui)
BuildRequires:		pkgconfig(Qt6Widgets)
BuildRequires:		pkgconfig(x11)

%description
KMidimon is a MIDI monitor for the ALSA sequencer, based on the drumstick
library. It monitors events coming from a MIDI external port or application or
loaded from standard MIDI Files.

%files
%doc AUTHORS ChangeLog COPYING NEWS.md README.md TODO.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/net.sourceforge.%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/metainfo/net.sourceforge.%{name}.metainfo.xml
%{_mandir}/man1/%{name}.1*
%{_mandir}/ja/man1/%{name}.1*
%{_docdir}/%{name}/*/%{name}/index.html

#----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
# Building the docs needs pandoc and we don't have it yet
%cmake -DUSE_QT5=OFF  -DBUILD_DOCS=OFF
%make_build


%install
%make_install -C build

desktop-file-edit --add-category Application --remove-category Music \
					%{buildroot}%{_datadir}/applications/net.sourceforge.%{name}.desktop

# Fix gzipped-svg-icon
(
cd %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
zcat %{name}.svgz > %{name}.svg && rm -f %{name}.svgz
)
