Summary:        tauOS GTK/GNOME Shell Themes
Name:           tau-helium
Version:        1.1
Release:        20
License:        GPLv3
URL:            https://tauos.co
Source0:        %{name}-%{version}.tar.gz
Source1:        README.md
Source2:        LICENSE
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
* Sun May 22 2022 Lains <lainsce@airmail.cc> - 1.1-20
- Remove platform-specific css classes and things
- Focus only on tau HIG and basic GTK theming.

* Sat May 21 2022 Lains <lainsce@airmail.cc> - 1.1-19
- Fix typography in general, again.

* Fri May 20 2022 Lains <lainsce@airmail.cc> - 1.1-18
- Fix typography in general.

* Fri May 20 2022 Lains <lainsce@airmail.cc> - 1.1-17
- Fix bg color in Helium-dark GNOME Shell.

* Thu May 19 2022 Lains <lainsce@airmail.cc> - 1.1-16
- Fix more oops.

* Thu May 19 2022 Lains <lainsce@airmail.cc> - 1.1-15
- Fix some oops.

* Wed May 18 2022 Lains <lainsce@airmail.cc> - 1.1-14
- Bring in the tauOS HIG widgetry and stuff.

* Tue May 17 2022 Lains <lainsce@airmail.cc> - 1.1-13
- Make the dark theme content block color not too stark.

* Mon May 16 2022 Lains <lainsce@airmail.cc> - 1.1-12
- Finalize and fix inconsistencies in the Helium GNOME Shell themes

* Sun May 15 2022 Lains <lainsce@airmail.cc> - 1.1-11
- Fix Helium Light GNOME Shell theme

* Fri May 13 2022 Lains <lainsce@airmail.cc> - 1.1-10
- Refine some GTK stuff

* Tue May 10 2022 Lains <lainsce@airmail.cc> - 1.1-9
- Refine some GTK stuff

* Tue May 10 2022 Lains <lainsce@airmail.cc> - 1.1-8
- Finish GTK4 theme

* Mon May 9 2022 Lains <lainsce@airmail.cc> - 1.1-7
- Start GTK4 theme

* Mon May 9 2022 Lains <lainsce@airmail.cc> - 1.1-6
- More improvements in styling

* Mon May 9 2022 Lains <lainsce@airmail.cc> - 1.1-5
- Improvements in styling to match Shell with GTK theme

* Mon May 9 2022 Lains <lainsce@airmail.cc> - 1.1-4
- GNOME shell theme wasn't being installed

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