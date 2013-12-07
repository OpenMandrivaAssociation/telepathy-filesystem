Name:           telepathy-filesystem
Version:        0.0.1
Release:        9
Summary:        Telepathy filesystem layout

Group:          System/Base
License:        Public Domain
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
Requires:       filesystem

%description
This package provides some directories which are required by other
packages which comprise the Telepathy release.  

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/telepathy/managers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/managers



%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-7mdv2011.0
+ Revision: 670674
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-6mdv2011.0
+ Revision: 607987
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-5mdv2010.1
+ Revision: 524189
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.0.1-4mdv2010.0
+ Revision: 427290
- rebuild

* Tue Jan 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-3mdv2009.1
+ Revision: 331932
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 13 2007 Olivier Thauvin <nanardon@mandriva.org> 0.0.1-2mdv2008.1
+ Revision: 108426
- rebuild


(none)