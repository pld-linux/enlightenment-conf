Summary:	Enlightenment Configuration applet.
Name:		enlightenment-conf
Version:	0.15
Release:	4
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy okien/Narzêdzia
Source:		ftp://www.rasterman.com/pub/enlightenment/%{name}-%{version}.tar.bz2
Patch:		enlightenment-conf-keybind.patch
URL:		http://www.rasterman.com/
Requires:	control-center
BuildRoot:	/tmp/%{name}-%{version}-root

%description
A Configuration tool for easily setting up Enlightenment

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) /usr/X11R6/bin/*

%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/
%lang(ga) /usr/X11R6/share/locale/ga/LC_MESSAGES/
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/
%lang(ja) /usr/X11R6/share/locale/ja/LC_MESSAGES/
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/

%changelog
* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- strip binaries

* Tue Feb 23 1999 The Rasterman <raster@redhat.com>
- Updated to 0.14

* Wed Feb 3 1999 The Rasterman <raster@redhat.com>
- Created for new E-conf standalone module
