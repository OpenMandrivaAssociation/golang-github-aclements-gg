# Run tests in check section
%bcond_without check

# https://github.com/aclements/go-gg
%global goipath         github.com/aclements/go-gg
%global commit          abd1f791f5ee99465ee7cffe771436379d6cee5a

%global common_description %{expand:
gg is a plotting package for Go inspired by the Grammar of Graphics.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Plotting package for Go 
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

Patch0:         0001-Fix-Sprintf-error-with-time-values.patch
Patch1:         0002-Add-missing-format-in-Fatalf.patch

BuildRequires: golang(github.com/aclements/go-moremath/fit)
BuildRequires: golang(github.com/aclements/go-moremath/scale)
BuildRequires: golang(github.com/aclements/go-moremath/stats)
BuildRequires: golang(github.com/aclements/go-moremath/vec)
BuildRequires: golang(github.com/ajstarks/svgo)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%autosetup %{?forgesetupargs} -p1


%install
%goinstall


%if %{with check}
%check
# new_test.go fails
# https://github.com/aclements/go-gg/issues/11
%gochecks -d "table"
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitabd1f79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1-20180422gitabd1f79
- First package for Fedora

