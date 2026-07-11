%global tl_name inlinelabel
%global tl_revision 63853

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.1
Release:	%{tl_revision}.1
Summary:	Assign equation numbers to inline equations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/inlinelabel
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinelabel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinelabel.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can assign equation numbers to inline equations. When
Japanese is supported, you can switch to circled equation numbers.

