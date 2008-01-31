%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	SaxFilters
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a framework for building XML filters using the SAX API
Summary(pl.UTF-8):	%{_pearname} - tworzenie filtrów XML za pomocą API SAX
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	5
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	205e7ab8b5fcc63e131ad6c96f7aa09c
URL:		http://pear.php.net/package/XML_SaxFilters/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
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

%description -l pl.UTF-8
XML_SaxFilters dostarcza podstawy do użycia filtrów Sax w PHP.
Originalny kod został opracowany przez Luisa Argericha i opublikowany
pod adresem
http://phpxmlclasses.sourceforge.net/show_doc.php?class=class_sax_filters.html.
Luis poddał dyskusji sposób, w jaki działają SaxFilters, używając jako
przykładu klas Sourceforge, w rozdziale 10 "PHP 4 XML" wydawnictwa
Wrox. Luis zezwolił na modyfikację kodu i licencji tak, aby klasa ta
mogła zostać dołączona do PEAR.

Ta wersja Filtrów Sax wprowadza znaczące zmiany w stosunku do
oryginalnego kodu Luisa (wsteczna zgodność nie została zachowana),
oddzielając abstrakcyjne klasy od interfejsu, dostarczając interfejsy
do odczytu i zapisu danych oraz metody wspomagające rekursywne
parsowanie dokumentów XML (na przykład AbstractFilter::setParent())
dla dokumentów, których struktura może się znacząco różnić.

Celem filtrowania Sax jest sprawienie, iż parsowanie dokumetnów będzie
modularne i łatwe do zarządzania. Parser wysyła zdarzenia to filtra
dziecka, które z kolei może wysłać zdarzenia do innego filtra. Możliwe
jest zaimplementowanie filtrów, które będą tak elastyczne i potężne
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
