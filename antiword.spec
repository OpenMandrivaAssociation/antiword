%define name antiword
%define version 0.37
%define release %mkrel 8

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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 antiword %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -a Resources/* %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
bzip2 Docs/*.1
cp Docs/*.1.bz2 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Docs/COPYING Docs/FAQ Docs/ReadMe Docs/Netscape
%{_bindir}/*
%{_mandir}/*/*
%{_libdir}/%{name}

