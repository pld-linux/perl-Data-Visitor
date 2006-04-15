#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Visitor
Summary:	Data::Visitor - Visitor style traversal of Perl data structures
Summary(pl):	Data::Visitor - przechodzenie struktur danych Perla w stylu Visitor
Name:		perl-Data-Visitor
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/N/NU/NUFFIN/Data-Visitor-0.04.tar.gz
# Source0-md5:	44e1ff9daccb68954857c144761e320a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Test-MockObject >= 1.04
BuildRequires:	perl-Test-use-ok
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a simple visitor implementation for Perl values.

It has a main dispatcher method, visit, which takes a single Perl
value and then calls the methods appropriate for that value.

%description -l pl
Ten modu³ to prosta implementacja visitor dla warto¶ci perlowych.

Ma g³ówn± metodê przekierowuj±c± - visit, która przyjmuje pojedyncz±
warto¶æ perlow±, a nastêpnie wywo³uje metody odpowiednie dla tej
warto¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Data/*.pm
%{perl_vendorlib}/Data/Visitor
%{_mandir}/man3/*
