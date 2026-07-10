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
Requires(pre):	texlive-tlpkg
Requires:	texlive(charissil)
Requires:	texlive(doulossil)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides all the necessary LaTeX frontends for the Bangla
language and comes with some fonts of its own.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/fonts/truetype
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bangla
%dir %{_datadir}/texmf-dist/fonts/truetype/public
%dir %{_datadir}/texmf-dist/tex/latex/bangla
%dir %{_datadir}/texmf-dist/fonts/truetype/public/bangla
%doc %{_datadir}/texmf-dist/doc/latex/bangla/README
%doc %{_datadir}/texmf-dist/doc/latex/bangla/bangla.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bangla/bangla.tex
%{_datadir}/texmf-dist/fonts/truetype/public/bangla/fontkalpurush.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/bangla/fontshimanto.ttf
%{_datadir}/texmf-dist/tex/latex/bangla/bangla.sty
%{_datadir}/texmf-dist/tex/latex/bangla/banglamap.tex
