Name:		enlightenment-conf
Version:	0.15
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia 
Summary:	E-conf the Enlightenment configuration tool. 
Source0:	ftp://www.rasterman.com/pub/enlightenment/%{name}-%{version}.tar.gz
Patch0:		enlightenment-conf-keybind.patch
Patch1:		enlightenment-conf-spelling.patch
Patch2:		enlightenment-conf-locale.patch
Patch3:		enlightenment-conf-alpha-notrans.patch
Patch4:		enlightenment-conf-DESTDIR.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
  
%define _prefix /usr/X11R6

%description
The enlightenment-conf package contains a configuration tool for
configuring the Enlightenment window manager. Enlightenment can be
configured in many different ways, so you'll want to install this
configuration tool if you plan to use Enlightenment.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ABOUT-NLS AUTHORS INSTALL README
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_datadir}/control-center
%dir %{_datadir}/control-center/Workspace
%attr(755,root,root) %{_bindir}/e-conf
%doc {ABOUT-NLS,AUTHORS,INSTALL,README}.gz
%{_datadir}/control-center/Workspace/Enlightenment.desktop
