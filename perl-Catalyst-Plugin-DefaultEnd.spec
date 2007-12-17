%define module	Catalyst-Plugin-DefaultEnd
%define name	perl-%module
%define	modprefix Catalyst

%define version	0.06
%define	rel	3
%define release	%mkrel %{rel}

Summary:	Sensible default end action for Catalyst
Name:		%name
Version:	%version
Release:	%release
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%module/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%module-%version.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 5.20
BuildArch:	noarch

%description
This action implements a sensible default end action, which will forward to the
first available view, unless status is set to 3xx, or there is a response body.

%prep
%setup -q -n %module-%version

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%buildroot

%files
%defattr(644,root,root,755)
%doc README Changes
%perl_vendorlib/%{modprefix}
%_mandir/*/*

%clean
rm -rf %{buildroot}

