Summary:	Tool to recompress and modify the structure of a DVD
Summary(pl.UTF-8):	Narzędzie do przepakowywania i modyfikowania struktury DVD
Name:		vamps
Version:	0.99
Release:	3
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/vamps/%{name}-%{version}.tar.gz
# Source0-md5:	63d61f2dd5c9df2eb2ad948164a56bae
Patch0:		%{name}-stdint.patch
URL:		http://vamps.sourceforge.net/
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vamps reduces the size of DVD compliant MPEG2 program streams by
selectively copying audio and subpicture tracks and by resizing the
embedded elementary video stream. The shrink factor may be either
specified for the video elementary stream only or for the video ES
only or for the full PS.

%description -l pl.UTF-8
Vamps zmniejsza rozmiar strumieni programowych MPEG2 zgodnych z DVD
poprzez wybiórcze kopiowanie ścieżek dźwiękowych i podobrazów oraz
zmiane rozmiaru osadzonego podstawowego strumienia obrazu.
Współczynnik zmniejszenia może być podany tylko dla podstawowego
strumienia obrazu lub tylko dla ES, lub dla pełnego PS.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fomit-frame-pointer -DHAVE_BUILTIN_EXPECT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install vamps/vamps $RPM_BUILD_ROOT%{_bindir}
install play_cell/play_cell $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
