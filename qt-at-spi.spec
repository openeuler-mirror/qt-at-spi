Name:    	qt-at-spi
Version: 	0.3.1
Release: 	1
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
%{qmake_qt4}
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
* Thu Feb 18 2021 weidong <weidong@uniontech.com> - 0.3.1-1
- Initial package 
