%include	/usr/lib/rpm/macros.perl
Summary:	System for using free software printer drivers
Summary(pl):	System umo¿liwiaj±cy u¿ywanie darmowych sterowników drukarek
Name:		foomatic-filters
Version:	3.0.0
Release:	0.1
Epoch:		1
License:	GPL
Group:		Applications/System
URL:		http://www.linuxprinting.org/foomatic.html
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{version}.tar.gz
# Source0-md5: 970e7fed64ee9f56e28ccd798af88918
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Foomatic is a system for using free software printer drivers with
common spoolers on Unix. It supports LPD, PDQ, CUPS, the VA Linux
LPD, LPRng, PPR, and direct spooler-less printing and any free
software driver for which execution data has been entered in the
database.

%description -l pl
Foomatic to system pozwalaj±cy na u¿ywanie wolnodostêpnych
sterowników drukarek z popularnymi uniksowymi serwerami wydruków.
Obs³uguje LPD, PDQ, CUPS, VA Linux LPD, LPRng, PPR i bezpo¶rednie
drukowanie bez kolejkowania oraz dowolny wolnodostêpny sterownik,
dla którego parametry zosta³y wprowadzone do bazy danych.

%package gswrapper
Summary:	foomatic wrapper for ghostscript
Summary(pl):	wrapper dla ghostscripta do u¿ycia z foomatic
Group:		Applications/System
Requires:	ghostscript
Requires:	a2ps
Obsoletes:	foomatic-gswrapper

%description gswrapper
A little Ghostscript regularization script. It massages arguments to
make Ghostscript execute properly as a filter, with output on stdout
and errors etc on stderr.

NOTE: This script is needed in a few situations only and may not work
with some Ghostscript versions. Moreover in some situations his
presence in the system may have effect that Your printer will
not print. So - Do not install this package if You don't know
what You're doing. 

%description gswrapper -l pl
Ma³y skrypt uzdatniaj±cy Ghostscripta. Obrabia parametry tak, ¿eby
Ghostscript dzia³a³ w³a¶ciwie jako filtr, generuj±c dane wyj¶ciowe na
stdout, a b³êdy na stderr.

UWAGA: Ten skrypt jest potrzebny tylko w kilku przypadkach i mo¿e
nie dzia³ac z niektórymi wersjami Ghostscripta. Ponadto w niektórych
sytuacjach jego obecno¶æ w systemie mo¿e spowodowaæ, ¿e drukarka nie
bêdzie drukowa³a. Tak wiêc - nie instaluj tego pakietu, je¶li nie
wiesz, co robisz. 

%package -n cups-filter-foomatic
Summary:	cupsomatic - CUPS filter
Summary(pl):	cupsomatic - filtr do CUPS
Group:		Applications/System
Requires:	cups
Requires:	foomatic-filters = %{version}
Obsoletes:	foomatic-cups
Obsoletes:	cups-foomatic

%description -n cups-filter-foomatic
Cupsomatic is intended to be used as a CUPS filter for printers
defined in a PPD file (CUPS-O-Matic or PPD-O-Matic) obtained from the
Linux Printing Database.

%description -n cups-filter-foomatic -l pl
Cupsomatic jest filtrem do CUPS dla drukarek zdefiniowanych w pliku
PPD (CUPS-O-Matic lub PPD-O-Matic), uzyskanym z Linux Printing
Database.

%package ppr
Summary:	ppromatic - PPR interface
Summary(pl):	ppromatic - interfejs do PPR
Group:		Applications/System
Requires:	foomatic-filters = %{version}
Requires:	ppr
Obsoletes:	foomatic-ppr

%description ppr
ppromatic is intended to be used as a PPR interface for printers
defined in a PPD-O-Matic PPD file obtained from the Linux Printing
Database.

%description ppr -l pl
ppromatic jest interfejsem do PPR dla drukarek zdefiniowanych w pliku
PPD (PPD-O-Matic) uzyskanym z Linux Printing Database.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR="$RPM_BUILD_ROOT"

ln -sf %{_bindir}/foomatic-rip $RPM_BUILD_ROOT%{_libdir}/cups/filter/cupsomatic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README USAGE

%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/foomatic/direct
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/foomatic/filter.conf
%attr(755,root,root) %{_bindir}/foomatic-rip
%{_mandir}/man1/foomatic-rip*

%files gswrapper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/foomatic-gswrapper
%{_mandir}/man1/foomatic-gswrapper*

%files -n cups-filter-foomatic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cups/filter/*

%files ppr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ppr/interfaces/foomatic-rip
%attr(755,root,root) %{_libdir}/ppr/lib/foomatic-rip
