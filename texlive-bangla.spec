Name:		texlive-bangla
Version:	65786
Release:	1
Summary:	A comprehensive Bangla LaTeX package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bangla
License:	lppl1.3c ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bangla.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bangla.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides all the necessary LaTeX frontends for the
Bangla language and comes with some fonts of its own.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bangla
%{_texmfdistdir}/fonts/truetype/public/bangla
%doc %{_texmfdistdir}/doc/latex/bangla

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
