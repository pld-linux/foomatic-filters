#
# Conditional build:
%bcond_with	ppr	# ppr support disabled until we have ppr.spec in working shape
#
Summary:	System for using free software printer drivers
Summary(pl.UTF-8):	System umożliwiający używanie darmowych sterowników drukarek
Name:		foomatic-filters
Version:	4.0.17
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.openprinting.org/download/foomatic/%{name}-%{version}.tar.gz
# Source0-md5:	b05f5dcbfe359f198eef3df5b283d896
URL:		http://www.linuxfoundation.org/en/OpenPrinting/Database/Foomatic
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
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

%package -n cups-filter-foomatic
Summary:	cupsomatic - CUPS filter
Summary(pl.UTF-8):	cupsomatic - filtr do CUPS
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}
Requires:	cups
Obsoletes:	cups-foomatic
Obsoletes:	foomatic-cups

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
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-file-converter-check
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

ln -sf %{_bindir}/foomatic-rip $RPM_BUILD_ROOT%{_ulibdir}/cups/filter/cupsomatic

%if %{without ppr}
%{__rm} -r $RPM_BUILD_ROOT%{_ulibdir}/ppr
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README USAGE
%dir %{_sysconfdir}/foomatic
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/foomatic/direct
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/foomatic/filter.conf
%attr(755,root,root) %{_bindir}/foomatic-rip
%{_mandir}/man1/foomatic-rip.1*

%files -n cups-filter-foomatic
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/cups/backend/beh
%attr(755,root,root) %{_ulibdir}/cups/filter/cupsomatic
%attr(755,root,root) %{_ulibdir}/cups/filter/foomatic-rip

%if %{with ppr}
%files ppr
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/ppr/interfaces/foomatic-rip
%attr(755,root,root) %{_ulibdir}/ppr/lib/foomatic-rip
%endif
