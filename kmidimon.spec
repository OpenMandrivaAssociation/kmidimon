Name:		kmidimon
Version:	0.7.4
Release:	%mkrel 69.1
License:	GPLv2+ 
Summary:	KDE MIDI Monitor for ALSA Sequencer
# different group in different mdv version: to be fixed
Group:		Sound
URL:		http://kmetronome.sourceforge.net/kmidimon/
Source0:	http://sourceforge.net/projects/kmidimon/files/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	kdesdk4-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(alsa) >= 1.0.0
BuildRequires:	pkgconfig(drumstick-alsa) >= 0.5.0
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
# The BReqs below are not present in the author's spec file: redundant?
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libart-2.0)
Requires:	oxygen-icon-theme
# end of the BRs not present in the source spec file
Requires:	drumstick >= 0.5.0

%description
KMidimon is a MIDI monitor for the ALSA sequencer, based on the drumstick
library. It monitors events coming from a MIDI external port or application or
loaded from standard MIDI Files.


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

%{find_lang} %{name} --with-html


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null


%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_mandir}/man1/%{name}.1.xz
%{_bindir}/%{name}
# Already provided by find_lang macro
#{_datadir}/doc/HTML/en/%%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/*/*
%{_datadir}/apps/*/*


%changelog
* Fri Feb 01 2013 Giovanni Mariani <mc2374@mclink.it> 0.7.4-69.1
- Imported on Rosa 2012.1 from a MIB package
- Fixed Source0 URL and archive type