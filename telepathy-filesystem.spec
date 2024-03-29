Name:		telepathy-filesystem
Version:	0.0.2
Release:	1
Summary:	Telepathy filesystem layout
Group:		System/Base
License:	Public Domain
BuildArch:	noarch
Requires:	filesystem

%description
This package provides some directories which are required by other
packages which comprise the Telepathy release.  

%install
mkdir -p %{buildroot}%{_datadir}/telepathy/managers
mkdir -p %{buildroot}%{_datadir}/telepathy/clients
mkdir -p %{buildroot}%{_includedir}/telepathy-1.0
%files
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/managers
%dir %{_datadir}/telepathy/clients
%dir %{_includedir}/telepathy-1.0
