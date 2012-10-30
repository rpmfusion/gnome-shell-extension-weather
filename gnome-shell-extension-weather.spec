%global git f7c4aea
%global uuid weather@gnome-shell-extensions.gnome.org
%global github Neroth-gnome-shell-extension-weather
%global checkout git%{git}

Name:           gnome-shell-extension-weather
Version:        0
Release:        0.9.%{checkout}%{?dist}
Summary:        An extension for displaying weather notifications in GNOME Shell

Group:          User Interface/Desktops
License:        GPLv3+
URL:            https://github.com/Neroth/gnome-shell-extension-weather
Source0:        https://github.com/Neroth/gnome-shell-extension-weather/tarball/master/%{github}-%{git}.tar.gz
BuildArch:      noarch

BuildRequires:  autoconf >= 2.53, automake >= 1.9, desktop-file-utils, glib2-devel, gnome-common >= 3.1.0, intltool >= 0.25
Requires:       gnome-shell >= 3.4.0, seed

%description
gnome-shell-extension-weather is a simple extension for displaying weather 
informations from several cities in GNOME Shell. Currently, the weather report 
including forecast for today and tomorrow is fetched from Yahoo! Weather.

%prep
%setup -q -n %{github}-%{git}
rm -rf debian

%build
NOCONFIGURE=1 ./autogen.sh
%configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
desktop-file-install --add-category="GNOME" --remove-category="System" --delete-original --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/weather-settings.desktop

%postun
if [ $1 -eq 0 ] ; then
        %{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc COPYING README.md
%{_datadir}/applications/weather-settings.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.weather.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
* Tue Oct 30 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 0-0.9.gitf7c4aea
- Update to latest upstream version (now compatible with Gnome 3.6)
- Update requirements (at least version 3.4 of Gnome Shell is required)

* Mon Oct 22 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 0-0.8.git6c1d6ab
- Update to latest upstream version

* Sat Oct 13 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 0-0.7.git734987b
- Update to latest upstream version

* Sat Aug 25 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 0-0.6.git5be82f2
- Update to latest upstream version

* Sun Aug 19 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 0-0.5.gitb9358f2
- Correct spec file

* Sat Aug 18 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 0-0.4.gitb9358f2
- Update to latest upstream version

* Wed Aug 01 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 0-0.3.git393203b
- Update to latest upstream version

* Mon Jun 04 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 0-0.2.git5c61d80
- Update to latest upstream version
- Add command to remove directory "debian"

* Wed May 30 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 0-0.1.gitb86397a
- Initial package for Fedora
