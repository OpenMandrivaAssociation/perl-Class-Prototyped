%define modname	Class-Prototyped
%define modver 1.13

Summary:	Fast prototype-based OO programming in Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Class/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Fast prototype-based OO programming in Perl

%package GraphViz
Summary:	Graph a Perl object structure with GraphViz
Group:		Development/Perl
Requires:	%{name} = %{EVRD}

%description GraphViz
Graph a Perl object structure with GraphViz

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
%exclude %{perl_vendorlib}/Class/Prototyped/Graph.pm
%{_mandir}/man3/*

%files GraphViz
%{perl_vendorlib}/Class/Prototyped/Graph.pm
