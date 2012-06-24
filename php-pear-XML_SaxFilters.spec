%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       SaxFilters
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - A framework for building XML filters using the SAX API
Summary(pl):	%{_pearname} - tworzenie filtr�w XML za pomoc� API SAX
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8661db8e5a38dbcd3c78b3fad288b34d
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_SaxFilters provides a foundation for using Sax filters in PHP. The
original code base was developed by Luis Argerich and published at
http://phpxmlclasses.sourceforge.net/show_doc.php?class=class_sax_filters.html.
Luis discussed how SaxFilters work, using the Sourceforge classes as
an example, in Chapter 10 of Wrox "PHP 4 XML". Luis kindly gave
permission to modify the code and license for inclusion in PEAR.

This version of the Sax Filters makes significant changes to Luis's
original code (backwards compatibility is definately broken),
seperating abstract classes from interfaces, providing interfaces for
data readers and writers and providing methods to help parse XML
documents recursively with filters (for example
AbstractFilter::setParent()) for documents where the structure can
vary significantly.

Sax Filtering is an approach to making parsing XML documents with Sax
modular and easy to maintain. The parser delegates events to a child
filter which may in turn delegate events to another filter. In general
it's possible to implement filters for a document which are as
flexible and powerful as DOM.

This class has in PEAR status: %{_status}.

%description -l pl
XML_SaxFilters dostarcza podstawy do u�ycia filtr�w Sax w PHP.
Originalny kod zosta� opracowany przez Luisa Argericha i opublikowany
pod adresem
http://phpxmlclasses.sourceforge.net/show_doc.php?class=class_sax_filters.html.
Luis podda� dyskusji spos�b, w jaki dzia�aj� SaxFilters, u�ywaj�c jako
przyk�adu klas Sourceforge, w rozdziale 10 "PHP 4 XML" wydawnictwa
Wrox. Luis zezwoli� na modyfikacj� kodu i licencji tak, aby klasa ta
mog�a zosta� do��czona do PEAR.

Ta wersja Filtr�w Sax wprowadza znacz�ce zmiany w stosunku do
oryginalnego kodu Luisa (wsteczna zgodno�� nie zosta�a zachowana),
oddzielaj�c abstrakcyjne klasy od interfejsu, dostarczaj�c interfejsy
do odczytu i zapisu danych oraz metody wspomagaj�ce rekursywne
parsowanie dokument�w XML (na przyk��d AbstractFilter::setParent())
dla dokument�w, kt�rych struktura mo�e si� znacz�co r�ni�.

Celem filtrowania Sax jest sprawienie, i� parsowanie dokumetn�w b�dzie
modularne i �atwe do zarz�dzania. Parser wysy�a zdarzenia to filtra
dziecka, kt�re z kolei mo�e wys�a� zdarzenia do innego filtra. Mo�liwe
jest zaimplementowanie filtr�w, kt�re b�d� tak elastyczne i pot�ne
jak DOM.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{,%{_subclass}}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
