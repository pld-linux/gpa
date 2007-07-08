Summary:	Gnu Privacy Assistant - Graphical Frontend for the GnuPG
Summary(pl.UTF-8):	Gnu Privacy Assistant - Graficzny Frontend GnuPG
Name:		gpa
Version:	0.7.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://wald.intevation.org/frs/download.php/350/%{name}-%{version}.tar.bz2
# Source0-md5:	8ee26d7fe829e81eb8bce2d974a7c500
URL:		http://www.gnupg.org/related_software/gpa/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9.3
BuildRequires:	gettext-devel >= 0.12.1
BuildRequires:	gpgme-devel >= 1:1.1.3
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	pkgconfig
Requires:	gnupg
Requires:	gpgme >= 1:1.1.3
Requires:	gtk+2 >= 2:2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPA (GNU Privacy Assistant) is a graphical frontend for the GNU
Privacy Guard (GnuPG). GPA can be used to encrypt, decrypt and sign
files, to verify signatures and to manage the private and public keys.

%description -l pl.UTF-8
GPA (GNU Privacy Assistant) jest graficzną nakładką dla programu Gnu
Privacy Guard (GnuPG). GPA może być użyte do szyfrowania,
deszyfrowania i podpisywania plików, do weryfikacji podpisów, oraz do
zarządzania zarówno publicznymi, jak i prywatnymi kluczami.

%prep
%setup -q

%build
GPG=%{_bindir}/gpg
export GPG

%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/zh_TW{.Big5,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/gpa.desktop
%{_pixmapsdir}/gpa.png
