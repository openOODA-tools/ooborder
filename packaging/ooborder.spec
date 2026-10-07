Name:           ooborder
Version:        0.1.0
Release:        1%{?dist}
Summary:        Wraps stdin text blocks inside configurable border frames with titles.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooborder
Source0:        ooborder-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooborder is a sovereign, capability-bounded PANEL BORDER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooborder
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooborder-uninstall

%files
/usr/bin/ooborder
/usr/bin/ooborder-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
