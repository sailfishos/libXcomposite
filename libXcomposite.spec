# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       libXcomposite
Summary:    X.Org X11 libXcomposite runtime library
Version:    0.4.3
Release:    0
Group:      System/Libraries
License:    MIT/X11
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source100:  libXcomposite.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(compositeproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(fixesproto)


%description
%{summary}.



%package devel
Summary:    X.Org X11 libXcomposite development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-filesystem

%description devel
%{summary}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXcomposite.so.1
%{_libdir}/libXcomposite.so.1.0.0
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/Xcomposite.h
%{_libdir}/libXcomposite.so
%{_libdir}/pkgconfig/xcomposite.pc
%doc %{_mandir}/man3/X?omposite*.3*
# << files devel

