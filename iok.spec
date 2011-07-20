Summary:	Indic Onscreen Virtual Keyboard
Name:		iok
Version:	1.3.12
Release:	1
License:	GPL v2+
Group:		Applications/System
URL:		http://iok.sourceforge.net
Source0:	https://fedorahosted.org/releases/i/o/iok/%{name}-%{version}.tar.gz
# Source0-md5:	872c12f7c08764ae978efa3fa234f7e9
Patch0:		%{name}-fix-non-standard-keymap-path.patch
BuildRequires:	gettext
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libxml2-devel
BuildRequires:	libunique-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	xkeyboard-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iok is Indic Onscreen Keyboard. It provides virtual Keyboard
functionality. It currently works with Inscript and xkb keymaps for
Indian languages. iok can even try to parse non-inscript keymaps and
show them in iok.

%prep
%setup -q
%patch0 -p0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/iok
%{_desktopdir}/iok.desktop
%{_pixmapsdir}/iok.xpm
%{_mandir}/man1/iok.1*


%clean
rm -rf $RPM_BUILD_ROOT
