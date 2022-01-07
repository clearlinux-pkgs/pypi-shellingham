#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-shellingham
Version  : 1.4.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/9c/c9/a3e3bc667c8372a74aa4b16649c3466364cd84f7aacb73453c51b0c2c8a7/shellingham-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/9c/c9/a3e3bc667c8372a74aa4b16649c3466364cd84f7aacb73453c51b0c2c8a7/shellingham-1.4.0.tar.gz
Summary  : Tool to Detect Surrounding Shell
Group    : Development/Tools
License  : ISC
Requires: pypi-shellingham-license = %{version}-%{release}
Requires: pypi-shellingham-python = %{version}-%{release}
Requires: pypi-shellingham-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
=============================================
Shellingham: Tool to Detect Surrounding Shell
=============================================

%package license
Summary: license components for the pypi-shellingham package.
Group: Default

%description license
license components for the pypi-shellingham package.


%package python
Summary: python components for the pypi-shellingham package.
Group: Default
Requires: pypi-shellingham-python3 = %{version}-%{release}

%description python
python components for the pypi-shellingham package.


%package python3
Summary: python3 components for the pypi-shellingham package.
Group: Default
Requires: python3-core
Provides: pypi(shellingham)

%description python3
python3 components for the pypi-shellingham package.


%prep
%setup -q -n shellingham-1.4.0
cd %{_builddir}/shellingham-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641578649
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-shellingham
cp %{_builddir}/shellingham-1.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-shellingham/e8f006df7200afbbdd3a2e7a85e487338dc75073
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-shellingham/e8f006df7200afbbdd3a2e7a85e487338dc75073

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*