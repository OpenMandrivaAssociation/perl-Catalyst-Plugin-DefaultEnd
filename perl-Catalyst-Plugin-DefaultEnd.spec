%define upstream_name	 Catalyst-Plugin-DefaultEnd
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Sensible default end action for Catalyst
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 5.20
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This action implements a sensible default end action, which will forward to the
first available view, unless status is set to 3xx, or there is a response body.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%buildroot

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README Changes
%perl_vendorlib/Catalyst
%_mandir/*/*
