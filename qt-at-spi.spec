Name:    	qt-at-spi
Version: 	0.3.1
Release: 	2
Summary: 	Qt plugin that bridges Qt's accessibility API to AT-SPI2 

License: 	LGPLv2+
URL:     	https://gitorious.org/qt-at-spi
Source0: 	qt-at-spi-qt-at-spi-v%{version}.tar.gz
Source1: 	qt-at-spi.sh

BuildRequires: 	gcc-c++ pkgconfig(atspi-2) pkgconfig(QtDBus) >= 4.8.0 pkgconfig(QtGui) pkgconfig(QtXml)

%{?_qt4:Requires: %{_qt4}%{?_isa} >= %{_qt4_version}}

%description
This is a Qt plugin that bridges Qt's accessibility API to AT-SPI2.
With recent versions of AT-SPI2 this should make Qt applications accessible
with the help of tools such as Gnome's Orca screen-reader.

%package help
Summary: Documentation for %{name}
BuildArch: noarch
%description help
%{summary}.


%prep
%setup -q -n %{name}-%{name}

install -m644 -p %{SOURCE1} .


%build
%if "%toolchain" == "clang"
	export CFLAGS="$CFLAGS -Wno-error=deprecated-copy-with-user-provided-copy -Wno-error=sometimes-uninitialized"
	export CXXFLAGS="$CXXFLAGS -Wno-error=deprecated-copy-with-user-provided-copy -Wno-error=sometimes-uninitialized"
	%{qmake_qt4} -spec %{_libdir}/qt4/mkspecs/unsupported/linux-clang
%else
	%{qmake_qt4}
%endif
%make_build

# build docs
pushd doc
qdoc3 qatspi.qdocconf
popd


%install
make install INSTALL_ROOT=%{buildroot}


%files
%doc README
%doc qt-at-spi.sh
%license LICENSE
%dir %{_qt4_plugindir}/accessiblebridge/
%{_qt4_plugindir}/accessiblebridge/libqspiaccessiblebridge.so

%files help
%doc doc/html/*


%changelog
* Tue Jun 20 2023 yoo <sunyuechi@iscas.ac.cn> - 0.3.1-2
- fix clang build error

* Thu Feb 18 2021 weidong <weidong@uniontech.com> - 0.3.1-1
- Initial package 
