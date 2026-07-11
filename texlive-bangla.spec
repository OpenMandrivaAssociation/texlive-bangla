%global tl_name bangla
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	A comprehensive Bangla LaTeX package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/bengali/bangla
License:	lppl1.3c ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangla.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangla.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(charissil)
Requires:	texlive(doulossil)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides all the necessary LaTeX frontends for the Bangla
language and comes with some fonts of its own.

