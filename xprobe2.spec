Summary:	Active ICMP fingerprinting tool
Name:		xprobe2
Version:	0.3
Release:	%mkrel 7
License:	GPLv2+
Group:		Networking/Other
URL:		http://xprobe.sourceforge.net/
Source0:	http://kent.dl.sourceforge.net/sourceforge/xprobe/%{name}-%{version}.tar.gz
Patch:      xprobe2-0.3-fix-compilation.patch
BuildRequires:	libpcap-devel
BuildRequires:	glib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Xprobe2 is an active operating system fingerprinting tool with a different
approach to operating system fingerprinting. Xprobe2 rely on fuzzy
signature matching, probabilistic guesses, multiple matches simultaneously,
and a signature database.

%prep

%setup -q
%patch -p0

chmod 644 docs/* AUTHORS CHANGELOG COPYING CREDITS README TODO

%build

%configure2_5x \
    --bindir=%{_sbindir}

%make 

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/*.txt docs/*.pdf docs/*.xsd AUTHORS CHANGELOG COPYING CREDITS README TODO
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_sbindir}/*
%{_mandir}/man1/* 
