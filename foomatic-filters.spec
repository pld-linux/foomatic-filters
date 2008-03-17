#
%bcond_with	ppr	# ppr support disabled until we have ppr.spec in working shape
#
%include	/usr/lib/rpm/macros.perl
%define		snap	20080317
Summary:	System for using free software printer drivers
Summary(pl.UTF-8):	System umożliwiający używanie darmowych sterowników drukarek
Name:		foomatic-filters
Version:	3.0.%{snap}
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-3.0-%{snap}.tar.gz
# Source0-md5:	7a39b08e1a8b1b63917277a021d403eb
URL:		http://www.linuxprinting.org/foomatic.html
BuildRequires:	a2ps
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_ulibdir	%{_prefix}/lib

%description
Foomatic is a system for using free software printer drivers with
common spoolers on Unix. It supports LPD, PDQ, CUPS, the VA Linux LPD,
LPRng, PPR, and direct spooler-less printing and any free software
driver for which execution data has been entered in the database.

%description -l pl.UTF-8
Foomatic to system pozwalający na używanie wolnodostępnych sterowników
drukarek z popularnymi uniksowymi serwerami wydruków. Obsługuje LPD,
PDQ, CUPS, VA Linux LPD, LPRng, PPR i bezpośrednie drukowanie bez
kolejkowania oraz dowolny wolnodostępny sterownik, dla którego
parametry zostały wprowadzone do bazy danych.

%package gswrapper
Summary:	foomatic wrapper for ghostscript
Summary(pl.UTF-8):	wrapper dla ghostscripta do użycia z foomatic
Group:		Applications/System
Requires:	a2ps
Requires:	ghostscript
Obsoletes:	foomatic-gswrapper

%description gswrapper
A little Ghostscript regularization script. It massages arguments to
make Ghostscript execute properly as a filter, with output on stdout
and errors etc on stderr.

NOTE: This script is needed in a few situations only and may not work
with some Ghostscript versions. Moreover in some situations his
presence in the system may have effect that Your printer will not
print. So - Do not install this package if You don't know what You're
doing.

%description gswrapper -l pl.UTF-8
Mały skrypt uzdatniający Ghostscripta. Obrabia parametry tak, żeby
Ghostscript działał właściwie jako filtr, generując dane wyjściowe na
stdout, a błędy na stderr.

UWAGA: Ten skrypt jest potrzebny tylko w kilku przypadkach i może nie
działac z niektórymi wersjami Ghostscripta. Ponadto w niektórych
sytuacjach jego obecność w systemie może spowodować, że drukarka nie
będzie drukowała. Tak więc - nie instaluj tego pakietu, jeśli nie
wiesz, co robisz.

%package -n cups-filter-foomatic
Summary:	cupsomatic - CUPS filter
Summary(pl.UTF-8):	cupsomatic - filtr do CUPS
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}
Requires:	cups
Obsoletes:	foomatic-cups
Obsoletes:	cups-foomatic

%description -n cups-filter-foomatic
Cupsomatic is intended to be used as a CUPS filter for printers
defined in a PPD file (CUPS-O-Matic or PPD-O-Matic) obtained from the
Linux Printing Database.

%description -n cups-filter-foomatic -l pl.UTF-8
Cupsomatic jest filtrem do CUPS dla drukarek zdefiniowanych w pliku
PPD (CUPS-O-Matic lub PPD-O-Matic), uzyskanym z Linux Printing
Database.

%package ppr
Summary:	ppromatic - PPR interface
Summary(pl.UTF-8):	ppromatic - interfejs do PPR
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}
Requires:	ppr
Obsoletes:	foomatic-ppr

%description ppr
ppromatic is intended to be used as a PPR interface for printers
defined in a PPD-O-Matic PPD file obtained from the Linux Printing
Database.

%description ppr -l pl.UTF-8
ppromatic jest interfejsem do PPR dla drukarek zdefiniowanych w pliku
PPD (PPD-O-Matic) uzyskanym z Linux Printing Database.

%prep
%setup -q -n %{name}-3.0-%{snap}

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

ln -sf %{_bindir}/foomatic-rip $RPM_BUILD_ROOT%{_ulibdir}/cups/filter/cupsomatic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README USAGE
%dir %{_sysconfdir}/foomatic
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/foomatic/direct
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/foomatic/filter.conf
%attr(755,root,root) %{_bindir}/foomatic-rip
%{_mandir}/man1/foomatic-rip*

%files gswrapper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/foomatic-gswrapper
%{_mandir}/man1/foomatic-gswrapper*

%files -n cups-filter-foomatic
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/cups/backend/beh
%attr(755,root,root) %{_ulibdir}/cups/filter/*

%if %{with ppr}
%files ppr
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/ppr/interfaces/foomatic-rip
%attr(755,root,root) %{_ulibdir}/ppr/lib/foomatic-rip
%endif
