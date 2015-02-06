Summary:	Active ICMP fingerprinting tool
Name:		xprobe2
Version:	0.3
Release:	9
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


%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.3-8mdv2011.0
+ Revision: 664863
- mass rebuild

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.3-7mdv2010.0
+ Revision: 446266
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-6mdv2009.1
+ Revision: 298456
- rebuilt against libpcap-1.0.0

* Mon Sep 15 2008 Michael Scherer <misc@mandriva.org> 0.3-5mdv2009.0
+ Revision: 284907
- rebuild, thanks to patch 1 to fix missing include
- fix license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jun 26 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3-1mdv2008.0
+ Revision: 44619
- 0.3
- drop upstream patches; P0
- new url


* Tue Oct 31 2006 Michael Scherer <misc@mandriva.org> 0.2-5mdv2007.0
+ Revision: 74744
- Rebuild for new suffix
- fix build with new coreutils ( or i think so, because it was working before )
- Bunzip patch
- Import xprobe2

