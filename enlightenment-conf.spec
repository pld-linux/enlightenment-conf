Summary:	E-conf the Enlightenment configuration tool. 
Summary(pl):	Narzêdzie do konfiguracji Enlightenmenta
Name:		enlightenment-conf
Version:	0.15
Release:	13
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://www.rasterman.com/pub/enlightenment/%{name}-%{version}.tar.gz
Patch0:		%{name}-keybind.patch
Patch1:		%{name}-spelling.patch
Patch2:		%{name}-locale.patch
Patch3:		%{name}-alpha-notrans.patch
Patch4:		%{name}-DESTDIR.patch
Patch5:		%{name}-use_AM_GNU_GETTEXT.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	flex
BuildRequires:	gtk+-devel
BuildRequires:	control-center-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
  
%define		_prefix		/usr/X11R6

%description
The enlightenment-conf package contains a configuration tool for
configuring the Enlightenment window manager. Enlightenment can be
configured in many different ways, so you'll want to install this
configuration tool if you plan to use Enlightenment.

%description -l pl
Pakiet enlightenment-conf zawiera narzêdzie do konfiguracji mened¿era
okien enlightenment. Enlightenment mo¿e byæ skonfigurowany na wiele
ró¿nych sposobów, wiêc jesli chcesz go u¿ywaæ, to powiniene¶
zainstalowaæ ten pakiet

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -f missing
libtoolize -c -f
aclocal -I macros
#autoconf
autoheader
#automake -a -c
%configure2_13 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%dir %{_datadir}/control-center
%dir %{_datadir}/control-center/Workspace
%attr(755,root,root) %{_bindir}/e-conf
%{_datadir}/control-center/Workspace/Enlightenment.desktop
