#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-plotrix
Version  : 3.8.4
Release  : 60
URL      : https://cran.r-project.org/src/contrib/plotrix_3.8-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/plotrix_3.8-4.tar.gz
Summary  : Various Plotting Functions
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# plotrix
`plotrix` is an `R` package that provides many plotting, labeling, and axis &
color scaling functions.

%prep
%setup -q -n plotrix
pushd ..
cp -a plotrix buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699901702

%install
export SOURCE_DATE_EPOCH=1699901702
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/plotrix/CITATION
/usr/lib64/R/library/plotrix/DESCRIPTION
/usr/lib64/R/library/plotrix/INDEX
/usr/lib64/R/library/plotrix/Meta/Rd.rds
/usr/lib64/R/library/plotrix/Meta/data.rds
/usr/lib64/R/library/plotrix/Meta/demo.rds
/usr/lib64/R/library/plotrix/Meta/features.rds
/usr/lib64/R/library/plotrix/Meta/hsearch.rds
/usr/lib64/R/library/plotrix/Meta/links.rds
/usr/lib64/R/library/plotrix/Meta/nsInfo.rds
/usr/lib64/R/library/plotrix/Meta/package.rds
/usr/lib64/R/library/plotrix/NAMESPACE
/usr/lib64/R/library/plotrix/NEWS
/usr/lib64/R/library/plotrix/R/plotrix
/usr/lib64/R/library/plotrix/R/plotrix.rdb
/usr/lib64/R/library/plotrix/R/plotrix.rdx
/usr/lib64/R/library/plotrix/data/death_reg.rda
/usr/lib64/R/library/plotrix/data/l2010.rda
/usr/lib64/R/library/plotrix/data/soils.rda
/usr/lib64/R/library/plotrix/demo/plotrix.R
/usr/lib64/R/library/plotrix/help/AnIndex
/usr/lib64/R/library/plotrix/help/aliases.rds
/usr/lib64/R/library/plotrix/help/paths.rds
/usr/lib64/R/library/plotrix/help/plotrix.rdb
/usr/lib64/R/library/plotrix/help/plotrix.rdx
/usr/lib64/R/library/plotrix/html/00Index.html
/usr/lib64/R/library/plotrix/html/R.css
