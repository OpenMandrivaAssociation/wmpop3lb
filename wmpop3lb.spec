%define name		wmpop3lb
%define version 2.4.2
%define release  10

Summary: 	POP3 mail box checker
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Graphical desktop/WindowMaker
Source0:	%{name}%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
URL:		http://www.jourdain.org/wmpop3/wmpop3lb%{version}.tar.gz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)

%description
 WMPop3LB is a multi POP3 accounts mailbox checker. It can connect to up to 6
 POP3 accounts to check if you have mail, get the "From:" and "Subject:" header
 fields of each mail and display them in a 7 lines window. It can list up to 19
 messages per server which can be read by scrolling the window up and down.
 Messages can be deleted directly off the servers by selecting the mails to
 delete and clicking the "delete" button.

 You may configure your .wmpop3rc either by hand or through the graphical
 utility called wmpop3lbcfg
	
%prep

%setup -qn %{name}%{version}
mv wmpop3/.wmpop3rc_test wmpop3/wmpop3rc 

%build
make FLAGS="$RPM_OPT_FLAGS" -C wmpop3

%install
[ -d %buildroot ] && rm -rf %buildroot

install -m 755 -d %buildroot/usr/bin/
install -m 755 wmpop3/%{name} %buildroot/usr/bin/%{name}
install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}
tar xOjf %SOURCE1 %name-16x16.png > %buildroot%{_miconsdir}/%{name}.png
tar xOjf %SOURCE1 %name-32x32.png > %buildroot%{_iconsdir}/%{name}.png
tar xOjf %SOURCE1 %name-48x48.png > %buildroot%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=/usr/bin/%{name}
Icon=%{name}
Categories=Office;Network;Email;
Name=WmPop3lb
Comment=Multiple mailbox monitoring via Pop3 in a dockapp
EOF


%clean
[ -z %buildroot ] || {
    rm -rf %buildroot
}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr (-,root,root)
%doc CHANGE_LOG  COPYING  INSTALL  README wmpop3/wmpop3rc
/usr/bin/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 2.4.2-9mdv2011.0
+ Revision: 634826
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 2.4.2-8mdv2010.0
+ Revision: 434894
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 2.4.2-7mdv2009.0
+ Revision: 262061
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.4.2-6mdv2009.0
+ Revision: 256255
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.4.2-4mdv2008.1
+ Revision: 171174
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Jan 25 2008 Funda Wang <fwang@mandriva.org> 2.4.2-3mdv2008.1
+ Revision: 157774
- fix desktop file

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 2.4.2-2mdv2008.1
+ Revision: 135533
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- use %%mkrel
- import wmpop3lb


* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.4.2-2mdk
- Rebuild

* Thu Apr 29 2004 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 2.4.2-1mdk
- New version 2.4.2

* Mon Feb 11 2002 HA Quôc-Viêt <viet@mandrakesoft.com> 2.0-1mdk
- Initial packaging.
- A sample configuration file is in the doc dir.
