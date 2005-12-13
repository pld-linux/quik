Summary:	Disk bootstrap and installer for Linux/PPC
Summary(pl):	Bootloader i instalator dla Linuksa na PPC
Name:		quik
Version:	2.0e
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://penguinppc.org/projects/quik/%{name}-%{version}.tar.gz
# Source0-md5:	ebc121539e3e39497e0fd772b12e7418
Patch0:		%{name}-install.patch
Patch1:		%{name}-j-k-diff.patch
Patch2:		%{name}-k-dac.patch
Patch3:		%{name}-glibc-headers.patch
URL:		http://penguinppc.org/projects/quik/
BuildRequires:	e2fsprogs-devel
BuildRequires:	e2fsprogs-static
Requires:	pmac-utils
Provides:	bootloader
ExclusiveArch:	ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	yaboot

%description
The quik package provides the functionality necessary for booting a
OldWorld Linux/PPC PowerMac or CHRP system from disk. It includes
first and second stage disk bootstrap and a program for installing the
first stage bootstrap on the root disk.

%description -l pl
Pakiet quik daje funkcjonalno¶æ niezbêdn± do uruchomienia z dysku
systemu Linux na sprzêcie OldWorld PPC PowerMac lub CHRP. Zawiera
bootloader pierwszego i drugiego etapu oraz program do instalowania
bootloadera pierwszego etapu na g³ównym dysku.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install man/quikconfig.8 $RPM_BUILD_ROOT%{_mandir}/man8
install debian/quikconfig $RPM_BUILD_ROOT%{_sbindir}

#install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-boot
#install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-boot/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/quik
%attr(755,root,root) %{_sbindir}/quikconfig
/boot/first.b
/boot/second.b
/boot/second
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_mandir}/man?/*
