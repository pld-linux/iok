Summary:	Indic Onscreen Virtual Keyboard
Summary(pl.UTF-8):	Indyjska klawiatura wirtualna na ekranie
Name:		iok
Version:	2.1.3
Release:	7
License:	GPL v2+
Group:		X11/Applications
#Source0Dowload: https://pagure.io/iok/releases
Source0:	https://releases.pagure.org/iok/%{name}-%{version}.tar.gz
# Source0-md5:	88ed68410e1b8c218cc576bf5b81b1a1
Patch0:		%{name}-types.patch
URL:		https://iok.sourceforge.net/
BuildRequires:	gettext-tools
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	libunique3-devel >= 3.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	xkeyboard-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iok is Indic Onscreen Keyboard. It provides virtual Keyboard
functionality. It currently works with Inscript and xkb keymaps for
Indian languages. iok can even try to parse non-inscript keymaps and
show them in iok.

%description -l pl.UTF-8
iok (Indic Onscreen Keyboard) to indyjska klawiatura na ekranie.
Zapewnia funkcjonalność wirtualnej klawiatury. Obecnie działa z mapami
klawiszy Inscript i xkb dla języków indyjskich. Potrafi nawet próbować
analizować mapy klawiszy inne niż inscript i wyświetlać je w ioku.

%prep
%setup -q
%patch -P0 -p1

%build
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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/iok
%{_desktopdir}/iok.desktop
%{_iconsdir}/hicolor/*/apps/iok.png
%{_iconsdir}/hicolor/scalable/apps/iok.svg
%{_mandir}/man1/iok.1*
