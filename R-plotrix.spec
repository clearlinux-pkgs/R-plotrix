#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-plotrix
Version  : 3.8.1
Release  : 39
URL      : https://cran.r-project.org/src/contrib/plotrix_3.8-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/plotrix_3.8-1.tar.gz
Summary  : Various Plotting Functions
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n plotrix
cd %{_builddir}/plotrix

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611428740

%install
export SOURCE_DATE_EPOCH=1611428740
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plotrix
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plotrix
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plotrix
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc plotrix || :


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
