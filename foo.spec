Name:           foo
Version:        0.1.0
Release:        1%{?dist}
Summary:        foo

License:        MIT
URL:            https://github.com/nikromen/foo
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch: noarch


%description
%{summary}


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 bin/%(name) %{buildroot}%{_bindir}


%files
%license LICENSE
%doc README.MD
%{_bindir}/%(name)



%changelog
* Tue Mar 14 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com>
- something
