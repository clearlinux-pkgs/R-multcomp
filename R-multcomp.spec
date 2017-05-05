#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-multcomp
Version  : 1.4.6
Release  : 13
URL      : https://cran.r-project.org/src/contrib/multcomp_1.4-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/multcomp_1.4-6.tar.gz
Summary  : Simultaneous Inference in General Parametric Models
Group    : Development/Tools
License  : GPL-2.0
Requires: R-lme4
Requires: R-lmtest
Requires: R-mvtnorm
Requires: R-sandwich
BuildRequires : R-TH.data
BuildRequires : R-lme4
BuildRequires : R-lmtest
BuildRequires : R-mvtnorm
BuildRequires : R-sandwich
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n multcomp

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492804762

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492804762
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library multcomp
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library multcomp


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/multcomp/CITATION
/usr/lib64/R/library/multcomp/DESCRIPTION
/usr/lib64/R/library/multcomp/INDEX
/usr/lib64/R/library/multcomp/MCMT/MCMT.R
/usr/lib64/R/library/multcomp/MCMT/MCMT.Rout
/usr/lib64/R/library/multcomp/MCMT/MCMT.Rout.save
/usr/lib64/R/library/multcomp/MCMT/MCMT.rda
/usr/lib64/R/library/multcomp/MCMT/multcomp.sas
/usr/lib64/R/library/multcomp/Meta/Rd.rds
/usr/lib64/R/library/multcomp/Meta/data.rds
/usr/lib64/R/library/multcomp/Meta/demo.rds
/usr/lib64/R/library/multcomp/Meta/features.rds
/usr/lib64/R/library/multcomp/Meta/hsearch.rds
/usr/lib64/R/library/multcomp/Meta/links.rds
/usr/lib64/R/library/multcomp/Meta/nsInfo.rds
/usr/lib64/R/library/multcomp/Meta/package.rds
/usr/lib64/R/library/multcomp/Meta/vignette.rds
/usr/lib64/R/library/multcomp/NAMESPACE
/usr/lib64/R/library/multcomp/NEWS
/usr/lib64/R/library/multcomp/R/multcomp
/usr/lib64/R/library/multcomp/R/multcomp.rdb
/usr/lib64/R/library/multcomp/R/multcomp.rdx
/usr/lib64/R/library/multcomp/data/Rdata.rdb
/usr/lib64/R/library/multcomp/data/Rdata.rds
/usr/lib64/R/library/multcomp/data/Rdata.rdx
/usr/lib64/R/library/multcomp/demo/Ch_Appl.R
/usr/lib64/R/library/multcomp/demo/Ch_GLM.R
/usr/lib64/R/library/multcomp/demo/Ch_Intro.R
/usr/lib64/R/library/multcomp/demo/Ch_Misc.R
/usr/lib64/R/library/multcomp/demo/Ch_Theory.R
/usr/lib64/R/library/multcomp/deprecated/deprecated.R
/usr/lib64/R/library/multcomp/deprecated/multcomp-deprecated.Rd
/usr/lib64/R/library/multcomp/deprecated/multcomp-oldtests.R
/usr/lib64/R/library/multcomp/deprecated/multcomp-oldtests.Rout.save
/usr/lib64/R/library/multcomp/doc/chfls1.R
/usr/lib64/R/library/multcomp/doc/chfls1.Rnw
/usr/lib64/R/library/multcomp/doc/chfls1.pdf
/usr/lib64/R/library/multcomp/doc/generalsiminf.R
/usr/lib64/R/library/multcomp/doc/generalsiminf.Rnw
/usr/lib64/R/library/multcomp/doc/generalsiminf.pdf
/usr/lib64/R/library/multcomp/doc/index.html
/usr/lib64/R/library/multcomp/doc/multcomp-examples.R
/usr/lib64/R/library/multcomp/doc/multcomp-examples.Rnw
/usr/lib64/R/library/multcomp/doc/multcomp-examples.pdf
/usr/lib64/R/library/multcomp/help/AnIndex
/usr/lib64/R/library/multcomp/help/aliases.rds
/usr/lib64/R/library/multcomp/help/multcomp.rdb
/usr/lib64/R/library/multcomp/help/multcomp.rdx
/usr/lib64/R/library/multcomp/help/paths.rds
/usr/lib64/R/library/multcomp/html/00Index.html
/usr/lib64/R/library/multcomp/html/R.css
/usr/lib64/R/library/multcomp/multcomp_VA.R
/usr/lib64/R/library/multcomp/multcomp_coxme.R
