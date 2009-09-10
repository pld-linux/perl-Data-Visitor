#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Visitor
Summary:	Data::Visitor - Visitor style traversal of Perl data structures
Summary(pl.UTF-8):	Data::Visitor - przechodzenie struktur danych Perla w stylu Visitor
Name:		perl-Data-Visitor
Version:	0.26
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	21639399af614325fff06621b338e064
URL:		http://search.cpan.org/dist/Data-Visitor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Any::Moose) >= 0.09
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl-Test-MockObject >= 1.04
BuildRequires:	perl-Tie-ToObject >= 0.01
BuildRequires:	perl-namespace-clean >= 0.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a simple visitor implementation for Perl values.

It has a main dispatcher method, visit, which takes a single Perl
value and then calls the methods appropriate for that value.

%description -l pl.UTF-8
Ten moduł to prosta implementacja visitor dla wartości perlowych.

Ma główną metodę przekierowującą - visit, która przyjmuje pojedynczą
wartość perlową, a następnie wywołuje metody odpowiednie dla tej
wartości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Data/*.pm
%{perl_vendorlib}/Data/Visitor
%{_mandir}/man3/*
