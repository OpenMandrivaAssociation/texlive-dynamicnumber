Name:		texlive-dynamicnumber
Version:	38726
Release:	2
Summary:	Dynamically typeset numbers and values in LaTeX through "symbolic links"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dynamicnumber
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dynamicnumber.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dynamicnumber.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dynamicnumber.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package dynamically typesets values generated by different
kinds of scripts in LaTeX through the use of "symbolic links"
(which are not in any way related to the "symbolic links" used
in UNIX systems!). The aim is to reduce errors resulting from
out-of-date numbers by directly setting them in the number
generating file and importing a "symbolic link" into the LaTeX
source file. It can be used to import not only numerical
values, but strings and pieces of code are also possible.
Currently only MATLAB and Python are supported to produce
Dynamic Number list files.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/dynamicnumber
%{_texmfdistdir}/tex/latex/dynamicnumber
%doc %{_texmfdistdir}/doc/latex/dynamicnumber

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
