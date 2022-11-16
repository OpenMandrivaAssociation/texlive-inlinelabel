Name:		texlive-inlinelabel
Version:	63853
Release:	1
Summary:	Assign equation numbers to inline equations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/inlinelabel
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinelabel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinelabel.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can assign equation numbers to inline equations.
When Japanese is supported, you can switch to circled equation
numbers.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/inlinelabel
%doc %{_texmfdistdir}/doc/latex/inlinelabel

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
