%define	use_ccache	1
%define	ccachedir	~/.ccache-OOo%{mdvsuffix}
			%{?_with_ccache: %global use_ccache 1}
			%{?_without_ccache: %global use_ccache 0}
%define	debug_package	%{nil}
%define	distsuffix	mib

Name:		kmidimon
Version:	0.7.4
Release:	%mkrel 69.1
License:	GPLv2+ 
Summary:	KDE MIDI Monitor for ALSA Sequencer
# different group in different mdv version: to be fixed
Group:		Sound
URL:		http://kmetronome.sourceforge.net/kmidimon/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(alsa) >= 1.0.0
BuildRequires:	drumstick-devel >= 0.5.0
BuildRequires:	kdelibs4-devel
BuildRequires:	kdesdk4-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	desktop-file-utils
# The BRs below are not present in the author's spec file
##Redundant?
##Need to cover also xorg
BuildRequires:	X11-devel
BuildRequires:	pkgconfig(libart-2.0)
Requires:	oxygen-icon-theme
# end of the BRs not present in the source spec file
Requires:	drumstick >= 0.5.0

%description
KMidimon is a MIDI monitor for the ALSA sequencer, based on the drumstick
library. It monitors events coming from a MIDI external port or application
or loaded from Standard MIDI Files.


%prep
%setup -q
# make sure bundled drumstick isn't used
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
* Sun Dec 30 2012 Giovanni Mariani <mc2374@mclink.it> 0.7.4-69.1
- Rebuilt for Rosa 2012.1 by the MIB

* Wed May 23 2012 Giovanni Mariani <mc2374@mclink.it> 0.7.4-69.1mib2010.2
- Rebuild for new KDE and Mdv 2010.2

* Sun Oct 03 2010 Giovanni Mariani <mc2374@mclink.it> 0.7.4-69.1mib2010.1
- New release 0.7.4 for MIB 2010.1
- Renamed the spec file
- Removed useless Packager and Vendor tags (already defined in .rpmmacros)
- Adjusted the License tag value
- Removed Source1 (use the source provided .desktop file)
- Made the BuildRoot tag compliant with wiki specs
- Removed obsolete BuildRequires for arts-devel (KDE 4 use pulse sound daemon)
- Added BR and version info for drumstick-devel (see ChangeLog file in the sources)
- Removed drumstick in-source to make use of the system installed one
- Added Requires an version info for the drumstick package containing
  the mime-defs for the files handled by the program
- Added BRs for needed pkgconfig, libdbus-devel, qt4-devel, kdesdk4-devel (see README files)
- Removed deprecated "$" macro for build root
- Used the "{name}" macro instead of directly "kmidimon" all time
- Redone the Description text
- Made use of "cmake_kde4" and "makeinstall_std" macros

* Sun Feb 27 2010 Beppe Florin <symbianflo@fastwebnet.it> 0.7.2-69mib
+ Imported from fedora
- New release
- MIB (Mandriva Italia Backport) - http://mib.pianetalinux.org

* Tue Nov 24 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.1-1
- updated to version 0.7.1, updated post scripts

* Wed Jul 16 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- tweaked spec file for building on CentOS

* Tue Jul 14 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.1-1
- updated to 0.5.1
- add proper dependencies for building on fc9

* Fri Feb  1 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- built on CentOS

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.0-1
- updated to version 0.5.0
- updated desktop categories
- now builds with cmake

* Tue Dec 12 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.1-2
- spec file tweaks, build for fc6

* Thu Sep  7 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.1-1
- updated to 0.4.1

* Fri Aug 19 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3-1
- updated to version 0.3

* Wed May  4 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1-1
- initial build.
