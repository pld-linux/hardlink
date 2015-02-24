Summary:	Create a tree of hardlinks
Name:		hardlink
Version:	1.0
Release:	2
License:	GPL+
Group:		Base
URL:		http://pkgs.fedoraproject.org/gitweb/?p=hardlink.git
Source0:	%{name}.c
Source1:	%{name}.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hardlink is used to create a tree of hard links. It's used by kernel
installation to dramatically reduce the amount of diskspace used by
each kernel package installed.

%prep
%setup -q -c -T
install -pm 644 %{SOURCE0} hardlink.c

%build
%{__cc} %{rpmcflags} hardlink.c -o hardlink

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_sbindir}}

install hardlink $RPM_BUILD_ROOT%{_sbindir}/hardlink
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/hardlink.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/hardlink
%{_mandir}/man1/hardlink.1*
