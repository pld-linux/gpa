Summary:	Gnu Privacy Assistant - Graphical Frontend for the GnuPG
Summary(pl):	Gnu Privacy Assistant - Graficzny Frontend GnuPG
Name:		gpa
Version:	0.6.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/gpa/%{name}-%{version}.tar.gz
URL:		http://www.gnupg.org/
BuildRequires:	pkgconfig
BuildRequires:	gpgme-devel >= 0.4.0
BuildRequires:	gtk+2-devel >= 2.0.0
Requires:	gnupg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPA (GNU Privacy Assistant) is a graphical frontend for the GNU
Privacy Guard (GnuPG). GPA can be used to encrypt, decrypt and sign
files, to verify signatures and to manage the private and public keys.

%description -l pl
GPA (GNU Privacy Assistant) jest graficzn� nak�adk� programu Gnu
Privacy Guard (GnuPG). GPA mo�e by� u�yte do szyfrowania,
deszyfrowania i podpisywania plik�w, to weryfikacji podpis�w, oraz to
zarz�dzania zar�wno publicznymi, jak i prywatnymi kluczami.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/locale
