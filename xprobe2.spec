%define release 5

Summary:	Active ICMP fingerprinting tool
Name:		xprobe2
Version:	0.2
Release:	%mkrel %release
License:	GPL
Group:		Networking/Other
Source0:	http://www.sys-security.com/archive/tools/%{name}/%{name}-%{version}.tar.bz2 
URL:		http://www.sys-security.com/html/projects/X.html
Patch0:         xprobe2-0.2-gcc33.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  libpcap-devel glib2-devel

%description
Xprobe2 is an active operating system fingerprinting tool with a different 
approach to operating system fingerprinting. Xprobe2 rely on fuzzy 
signature matching, probabilistic guesses, multiple matches simultaneously,
and a signature database.

%prep
%setup -q 
%patch0 -p0

%build
./configure --prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--sysconfdir=%{_sysconfdir}/
%make 

%install
rm -rf %{buildroot}
%makeinstall 
mv  $RPM_BUILD_ROOT/%_bindir/ $RPM_BUILD_ROOT/%_sbindir
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_sbindir/*
%config(noreplace) %_sysconfdir/%name/*
%dir %_sysconfdir/%name/
%_mandir/man1/* 


