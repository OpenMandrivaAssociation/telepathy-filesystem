Name:           telepathy-filesystem
Version:        0.0.1
Release:        %mkrel 7
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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/telepathy/managers

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/managers

