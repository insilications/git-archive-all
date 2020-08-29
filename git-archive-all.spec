#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : git-archive-all
Version  : 1.22.0
Release  : 11
URL      : file:///insilications/build/clearlinux/packages/git-archive-all/git-archive-all-1.22.0.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/git-archive-all/git-archive-all-1.22.0.tar.gz
Summary  : Archive git repository with its submodules.
Group    : Development/Tools
License  : GPL-2.0
Requires: git-archive-all-bin = %{version}-%{release}
Requires: git-archive-all-python = %{version}-%{release}
Requires: git-archive-all-python3 = %{version}-%{release}
Requires: git
Requires: python3-core
BuildRequires : buildreq-distutils3
BuildRequires : findutils
BuildRequires : git
BuildRequires : python3-core
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://img.shields.io/pypi/v/git-archive-all.svg
:target: https://pypi.python.org/pypi/git-archive-all
:alt: PyPI
.. image:: https://img.shields.io/homebrew/v/git-archive-all.svg
:target: https://formulae.brew.sh/formula/git-archive-all
:alt: Homebrew
.. image:: https://travis-ci.org/Kentzo/git-archive-all.svg?branch=master
:target: https://travis-ci.org/Kentzo/git-archive-all
:alt: Travis
.. image:: https://codecov.io/gh/Kentzo/git-archive-all/branch/master/graph/badge.svg
:target: https://codecov.io/gh/Kentzo/git-archive-all/branch/master
:alt: Coverage
.. image:: https://img.shields.io/pypi/pyversions/git-archive-all.svg
:target: https://pypi.python.org/pypi/git-archive-all
:alt: Supported Python versions
.. image:: https://img.shields.io/pypi/implementation/git-archive-all.svg
:target: https://pypi.python.org/pypi/git-archive-all
:alt: Supported Python implementations

%package bin
Summary: bin components for the git-archive-all package.
Group: Binaries

%description bin
bin components for the git-archive-all package.


%package python
Summary: python components for the git-archive-all package.
Group: Default
Requires: git-archive-all-python3 = %{version}-%{release}

%description python
python components for the git-archive-all package.


%package python3
Summary: python3 components for the git-archive-all package.
Group: Default
Requires: python3-core
Provides: pypi(git_archive_all)

%description python3
python3 components for the git-archive-all package.


%prep
%setup -q -n git-archive-all
cd %{_builddir}/git-archive-all

%build
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598702879
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export FCFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export FFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export CFFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export LDFLAGS="-O3 -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native "
export CXXFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -fvisibility-inlines-hidden -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/git-archive-all

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
