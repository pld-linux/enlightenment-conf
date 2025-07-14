Summary:	E-conf the Enlightenment configuration tool
Summary(pl.UTF-8):	Narzędzie do konfiguracji Enlightenmenta
Name:		enlightenment-conf
Version:	0.15
Release:	14
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://www.rasterman.com/pub/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	ad87526c1e86088e5ba851c36eb70b13
Patch0:		%{name}-keybind.patch
Patch1:		%{name}-spelling.patch
Patch2:		%{name}-locale.patch
Patch3:		%{name}-alpha-notrans.patch
Patch4:		%{name}-DESTDIR.patch
Patch5:		%{name}-use_AM_GNU_GETTEXT.patch
Patch6:		%{name}-configure.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	control-center1-devel
BuildRequires:	flex
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The enlightenment-conf package contains a configuration tool for
configuring the Enlightenment window manager.

%description -l pl.UTF-8
Pakiet enlightenment-conf zawiera narzędzie do konfiguracji zarządcy
okien enlightenment.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{_datadir}/control-center/Workspace
%attr(755,root,root) %{_bindir}/e-conf
%{_datadir}/control-center/Workspace/Enlightenment.desktop
