%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	SaxFilters
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a framework for building XML filters using the SAX API
Summary(pl):	%{_pearname} - tworzenie filtrów XML za pomoc± API SAX
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	3
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	205e7ab8b5fcc63e131ad6c96f7aa09c
URL:		http://pear.php.net/package/XML_SaxFilters/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
Requires:	php-pear-XML_HTMLSax
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

In PEAR status of this package is: %{_status}.

%description -l pl
XML_SaxFilters dostarcza podstawy do u¿ycia filtrów Sax w PHP.
Originalny kod zosta³ opracowany przez Luisa Argericha i opublikowany
pod adresem
http://phpxmlclasses.sourceforge.net/show_doc.php?class=class_sax_filters.html.
Luis podda³ dyskusji sposób, w jaki dzia³aj± SaxFilters, u¿ywaj±c jako
przyk³adu klas Sourceforge, w rozdziale 10 "PHP 4 XML" wydawnictwa
Wrox. Luis zezwoli³ na modyfikacjê kodu i licencji tak, aby klasa ta
mog³a zostaæ do³±czona do PEAR.

Ta wersja Filtrów Sax wprowadza znacz±ce zmiany w stosunku do
oryginalnego kodu Luisa (wsteczna zgodno¶æ nie zosta³a zachowana),
oddzielaj±c abstrakcyjne klasy od interfejsu, dostarczaj±c interfejsy
do odczytu i zapisu danych oraz metody wspomagaj±ce rekursywne
parsowanie dokumentów XML (na przyk³ad AbstractFilter::setParent())
dla dokumentów, których struktura mo¿e siê znacz±co ró¿niæ.

Celem filtrowania Sax jest sprawienie, i¿ parsowanie dokumetnów bêdzie
modularne i ³atwe do zarz±dzania. Parser wysy³a zdarzenia to filtra
dziecka, które z kolei mo¿e wys³aæ zdarzenia do innego filtra. Mo¿liwe
jest zaimplementowanie filtrów, które bêd± tak elastyczne i potê¿ne
jak DOM.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
