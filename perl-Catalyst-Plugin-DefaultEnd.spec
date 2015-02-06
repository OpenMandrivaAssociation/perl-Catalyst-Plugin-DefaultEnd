%define upstream_name	 Catalyst-Plugin-DefaultEnd
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Sensible default end action for Catalyst
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Catalyst) >= 5.20
BuildRequires:	perl(Module::Build)
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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 681034
- add br
- mass rebuild

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 461720
- update to 0.08

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 401760
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2010.0
+ Revision: 370011
- update to new version 0.07

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.06-3mdv2009.0
+ Revision: 136677
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-3mdv2008.0
+ Revision: 86005
- rebuild


* Thu Jun 29 2006 Scott Karns <scottk@mandriva.org> 0.06-2mdv2007.0
- Rebuild

* Thu Apr 27 2006 Scott Karns <scottk@mandriva.org> 0.06-1mdk
- 0.06

* Fri Mar 31 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.05-1mdk
- 0.05

* Thu Jan 12 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.04-1mdk
- Initial MDV RPM

