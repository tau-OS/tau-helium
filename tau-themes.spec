Summary:        tauOS GTK/GNOME Shell Themes
Name:           tau-helium
Version:        1.1
Release:        3
License:        GPLv3
URL:            https://tauos.co
Source0:        README.md
Source1:        LICENSE
Source2:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  sassc
BuildRequires:  meson
BuildRequires:  ninja-build

%description
A set of GTK/GNOME Shell Themes for tauOS

%prep
%autosetup

%build
%meson
%meson_build

%install
# Install licenses
mkdir -p licenses
install -pm 0644 %SOURCE1 licenses/LICENSE
install -pm 0644 %SOURCE0 README.md
%meson_install

%files
%license licenses/LICENSE
%doc README.md
%{_datadir}/themes/Helium/*
%{_datadir}/themes/Helium-dark/*

%changelog
* Sun May 8 2022 Lains <lainsce@airmail.cc> - 1.1-3
- Perhaps this is needed

* Sun May 8 2022 Lains <lainsce@airmail.cc> - 1.1-2
- Let's roll our own gtk theme

* Wed May 4 2022 Lains <lainsce@airmail.cc> - 1.1-1.7.2
- Get Helium GNOME Shell theme here

* Tue May 3 2022 Lains <lainsce@airmail.cc> - 1.1-1.7.1
- Get Helium GNOME Shell theme here

* Thu Apr 21 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1.7
- Update adw-gtk3 to v1.7
- Update Build System

* Thu Apr 7 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-2
- Add accent colours

* Thu Apr 7 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Initial Release
