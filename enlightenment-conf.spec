Summary:	Enlightenment Configuration applet.
Name:		enlightenment-conf
Version:	0.15
Release:	4
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) /usr/X11R6/bin/*
