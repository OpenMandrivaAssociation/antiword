%define debug_package %{nil}

Summary:	MS Word to ASCII/Postscript converter
Name:		antiword
Version:	0.37
Release:	20
License:	GPLv2
Group:		Text tools 
Url:		https://www.winfield.demon.nl/
Source0:	http://www.winfield.demon.nl/linux/%{name}-%{version}.tar.bz2
Patch0:		antiword-find-my-files.patch
# Fix buffer overflow with malformed input files (patch from Debian, Debian
# bug #407015)
Patch1:		10_fix_buffer_overflow_wordole_c.dpatch
BuildRequires:	bzip2

%description
Antiword is a free MS-Word reader for Linux, BeOS and RISC OS. It converts
the documets from Word 6, 7, 97 and 2000 to ASCII and Postscript. Antiword
tries to keep the layout of the document intact.

%prep
%setup -q
%autopatch -p1

sed -i -e 's|PKGBASEDIR_SUBSTITUTE_FROM_SPECFILE|\"%{_libdir}\"|g' options.c
# Use standard CFLAGS
sed -i -e "s/OPT\t=/#OPT\t=/" Makefile*
chmod a+r * Resources/* Docs/*

%build
OPT="%{optflags}" %make all

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 antiword %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -a Resources/* %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
bzip2 Docs/*.1
cp Docs/*.1.bz2 %{buildroot}%{_mandir}/man1

%files
%doc Docs/COPYING Docs/FAQ Docs/ReadMe Docs/Netscape
%{_bindir}/*
%{_mandir}/*/*
%{_libdir}/%{name}

