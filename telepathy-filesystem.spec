Name:           telepathy-filesystem
Version:        0.0.1
Release:        %mkrel 3
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

