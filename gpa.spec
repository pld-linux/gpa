Summary:	Gnu Privacy Assistant - Graphical Frontend for the GnuPG
Summary(pl.UTF-8):	Gnu Privacy Assistant - Graficzny Frontend GnuPG
Name:		gpa
Version:	0.9.2
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/gpa/%{name}-%{version}.tar.bz2
# Source0-md5:	8b17eb0c9b7d579a63693c2d378b40b7
URL:		http://www.gnupg.org/related_software/gpa/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gpgme-devel >= 1:1.2.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libassuan-devel >= 1.1.0
BuildRequires:	libgpg-error-devel >= 1.4
BuildRequires:	pkgconfig
Requires:	gnupg
Requires:	gpgme >= 1:1.2.0
Requires:	gtk+2 >= 2:2.10.0
Requires:	libassuan >= 1.1.0
Requires:	libgpg-error >= 1.4
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
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	GPG=/usr/bin/gpg
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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gpa
%{_datadir}/%{name}
%{_mandir}/man1/gpa.1*
%{_desktopdir}/gpa.desktop
%{_pixmapsdir}/gpa.png
