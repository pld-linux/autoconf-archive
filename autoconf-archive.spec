Summary:	The Autoconf Macro Archive
Summary(pl.UTF-8):	Archiwum makr Autoconfa
Name:		autoconf-archive
Version:	2016.09.16
Release:	1
License:	GPL v3+ with exceptions
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/autoconf-archive/%{name}-%{version}.tar.xz
# Source0-md5:	bf19d4cddce260b3c3e1d51d42509071
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/autoconf-archive/
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
# max of AC_PREREQ from ax_*.m4
Requires:	autoconf >= 2.69
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNU Autoconf Archive is a collection of more than 500 macros for
GNU Autoconf that have been contributed as free software by friendly
supporters of the cause from all over the Internet.

%description -l pl.UTF-8
GNU Autoconf Archive to zbiór ponad 500 makr dla GNU Autoconfa,
przekazanych jako oprogramowanie wolnodostępne przez przyjaznych
przypadkowych wspierających z całego Internetu.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

# remove dir file which will be generated by /sbin/install-info
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
# document files are installed another location
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.EXCEPTION ChangeLog NEWS README TODO
%{_aclocaldir}/ax_*.m4
%{_infodir}/autoconf-archive.info*
