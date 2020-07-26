#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MooX
%define		pnam	TypeTiny
Summary:	MooX::TypeTiny - Optimized type checks for Moo + Type::Tiny
Name:		perl-MooX-TypeTiny
Version:	0.002003
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	11d27986dff550f2e2cdb9d3a6c26469
URL:		https://metacpan.org/release/MooX-TypeTiny
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Class-Method-Modifiers
BuildRequires:	perl-Moo >= 2.004
BuildRequires:	perl-Type-Tiny >= 1.010002
BuildRequires:	perl-Test-Fatal >= 0.003
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module optimizes Moo type checks when used with Type::Tiny to perform
better.  It will automatically apply to isa checks and coercions that use
Type::Tiny.  Non-Type::Tiny isa checks will work as normal.

This is done by inlining the type check in a more optimal manner that is
specific to Type::Tiny rather than the general mechanism Moo usually uses.

With this module, setters with type checks should be as fast as an equivalent
check in Moose.

It is hoped that eventually this type inlining will be done automatically,
making this module unnecessary.

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
%doc Changes README
%{perl_vendorlib}/MooX/TypeTiny.pm
%{perl_vendorlib}/MooX/TypeTiny
%{_mandir}/man3/MooX::TypeTiny.3*
