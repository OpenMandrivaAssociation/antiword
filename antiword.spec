%define name antiword
%define version 0.37
%define release %mkrel 9

Summary: MS Word to ASCII/Postscript converter
Name: %{name}
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
URL: http://www.winfield.demon.nl/
Patch0: antiword-find-my-files.patch
# Fix buffer overflow with malformed input files (patch from Debian, Debian
# bug #407015)
Patch1:	10_fix_buffer_overflow_wordole_c.dpatch
License: GPL 
Group: Text tools 
BuildRequires: bzip2
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Antiword is a free MS-Word reader for Linux, BeOS and RISC OS. It converts
the documets from Word 6, 7, 97 and 2000 to ASCII and Postscript. Antiword
tries to keep the layout of the document intact.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
perl -pi -e 's|PKGBASEDIR_SUBSTITUTE_FROM_SPECFILE|\"%{_libdir}\"|g' options.c
# Use standard CFLAGS
sed -i -e "s/OPT\t=/#OPT\t=/" Makefile*
chmod a+r * Resources/* Docs/*

%build
OPT="%{optflags}" %make all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 antiword $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -a Resources/* $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
bzip2 Docs/*.1
cp Docs/*.1.bz2 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Docs/COPYING Docs/FAQ Docs/ReadMe Docs/Netscape
%{_bindir}/*
%{_mandir}/*/*
%{_libdir}/%{name}



%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.37-8mdv2011.0
+ Revision: 662766
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 0.37-7mdv2011.0
+ Revision: 603179
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.37-6mdv2010.1
+ Revision: 521984
- rebuilt for 2010.1

* Sat Jun 06 2009 Frederik Himpe <fhimpe@mandriva.org> 0.37-5mdv2010.0
+ Revision: 383304
- Add patch from Debian fixing buffer overflow
- Build with standard CFLAGS

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 0.37-4mdv2009.1
+ Revision: 364680
- rediff my file patch

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.37-4mdv2009.0
+ Revision: 220349
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.37-3mdv2008.1
+ Revision: 148448
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Apr 25 2007 Adam Williamson <awilliamson@mandriva.org> 0.37-2mdv2008.0
+ Revision: 18109
- rebuild for the modern era, slight updates to spec to suit modern policies


* Sun Jan 15 2006 Marcel Pol <mpol@mandriva.org> 0.37-1mdk
- From Moreno Manzini <moreno.mg@gmail.com>
  - 0.37

* Wed May 25 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.36.1-1mdk
- 0.36.1

* Wed Nov 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.36-1mdk
- 0.36
- regenerate & rename patch

* Tue Dec 09 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.35-1mdk
- 0.35

* Fri Mar 21 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.33-1mdk
- 0.33
- regenerate find-my-files patch

