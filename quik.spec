Summary:	Disk bootstrap and installer for Linux/PPC
Name:		quik
Version:	2.0e
Release:	0.2
License:	GPL
Group:		Applications/System
URL:		http://penguinppc.org/projects/quik/
Source0:	http://penguinppc.org/projects/quik/%{name}-%{version}.tar.gz
Patch0:		%{name}-install.patch
Requires:	pmac-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	e2fsprogs-devel
BuildRequires:	e2fsprogs-static
Provides:	bootloader
Obsoletes:	yaboot
ExclusiveArch:	ppc

%description
The quik package provides the functionality necessary for booting a
Linux/PPC PowerMac or CHRP system from disk. It includes first and
second stage disk bootstrap and a program for installing the first
stage bootstrap on the root disk.

%prep
%setup -q
%patch0 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install -d $RPM_BUILD_ROOT/%{_sbindir}

install man/quikconfig.8 $RPM_BUILD_ROOT/%{_mandir}/man8/
install debian/quikconfig $RPM_BUILD_ROOT/%{_sbindir}/

#install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-boot
#install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-boot/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/quik
%attr(755,root,root) %{_sbindir}/quikconfig
%attr(644,root,root) /boot/first.b
%attr(644,root,root)/boot/second.b
%attr(644,root,root)/boot/second
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
%{_mandir}/man?/*
