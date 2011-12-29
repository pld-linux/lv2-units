Summary:	LV2 Units extension - units for LV2 values
Summary(pl.UTF-8):	Rozszerzenie LV2 Units - jednostki dla wartości LV2
Name:		lv2-units
Version:	5.4
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	5eb0ed26e6fb25e5543150f7fefc71f8
URL:		http://lv2plug.in/ns/extensions/units/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
Requires:	lv2core >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 Units extension defines a number of units for use in audio
processing.

%description -l pl.UTF-8
Rozszerzenie LV2 Units definiuje wiele jednostek mających zastosowanie
przy przetwarzaniu dźwięku.

%package devel
Summary:	Development files for LV2 Units extension
Summary(pl.UTF-8):	Pliki programistyczne rozszerzenia LV2 Units
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core-devel >= 6.0

%description devel
Development files for LV2 Units extension.

%description devel -l pl.UTF-8
Pliki programistyczne rozszerzenia LV2 Units.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%dir %{_libdir}/lv2/units.lv2
%{_libdir}/lv2/units.lv2/lv2-units.doap.ttl
%{_libdir}/lv2/units.lv2/units.ttl
%{_libdir}/lv2/units.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
#%{_libdir}/lv2/units.lv2/units.h
%{_includedir}/lv2/lv2plug.in/ns/extensions/units
%{_pkgconfigdir}/lv2-lv2plug.in-ns-extensions-units.pc
