
%define name	metapixel
%define version	1.0.2
%define rel	2

Summary:	Photomosaic generator
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPLv2+
Group:		Graphics
URL:		http://www.complang.tuwien.ac.at/schani/metapixel/
Source:		http://www.complang.tuwien.ac.at/schani/metapixel/files/metapixel-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	ungif-devel
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	zlib-devel

%description
Metapixel is a program for generating photomosaics.  It can generate
classical photomosaics, in which the source image is viewed as a
matrix of equally sized rectangles for each of which a matching
image is substitued, as well as collage-style photomosaics, in which
rectangular parts of the source image at arbitrary positions (i.e.
not aligned to a matrix) are substituted by matching images.

%prep
%setup -q

%build
%make OPTIMIZE="%{optflags}"

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_mandir}/man1
make install BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS metapixelrc
%{_bindir}/metapixel*
%{_mandir}/man1/metapixel.1*

