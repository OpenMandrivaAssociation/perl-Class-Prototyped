%define modname	Class-Prototyped
%define modver 1.13

Summary:	Fast prototype-based OO programming in Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Class/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Fast prototype-based OO programming in Perl

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
%make test

%install
%make_install

%files
%doc README
%{perl_vendorlib}/Class/*
%{_mandir}/man3/*
