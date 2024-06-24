Summary:	Gnu Privacy Assistant - Graphical Frontend for the GnuPG
Summary(pl.UTF-8):	Gnu Privacy Assistant - Graficzny Frontend GnuPG
Name:		gpa
Version:	0.10.0
Release:	2
License:	GPL v3+
Group:		X11/Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/gpa/%{name}-%{version}.tar.bz2
# Source0-md5:	d0ee0086aea0ad1f61f81dae9a71c253
Patch0:		%{name}-am.patch
URL:		https://www.gnupg.org/related_software/gpa/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	gpgme-devel >= 1:1.9.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libassuan-devel >= 1:2.4.2
BuildRequires:	libgpg-error-devel >= 1.27
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	gnupg
Requires:	gpgme >= 1:1.9.0
Requires:	gtk+2 >= 2:2.10.0
Requires:	libassuan >= 1:2.4.2
Requires:	libgpg-error >= 1.27
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
%patch0 -p1

# use newer system versions
%{__rm} m4/{gpg-error.m4,gpgme.m4,libassuan.m4}

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	GPG=/usr/bin/gpg \
	--disable-silent-rules
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
