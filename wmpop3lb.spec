%define name		wmpop3lb
%define version 2.4.2
%define release %mkrel 7

Summary: 	POP3 mail box checker
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Graphical desktop/WindowMaker
Source0:	%{name}%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
URL:		http://www.jourdain.org/wmpop3/wmpop3lb%{version}.tar.gz
BuildRequires:	X11-devel, xpm-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

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

%setup -n %{name}%{version}
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
