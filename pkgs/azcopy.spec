%global debug_package %{nil}

Name:           azcopy
Version:        10.23.0
Release:        1%{?dist}
Summary:        AzCopy v10 is a command-line utility that you can use to copy data to and from containers and file shares in Azure Storage accounts.

Group:          Application/System
License:        MIT
URL:            https://github.com/Azure/azure-storage-azcopy
Source0:        https://github.com/Azure/azure-storage-azcopy/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang
Requires:       golang

%description
AzCopy v10 is a command-line utility that you can use to copy data to and from containers and file shares in Azure Storage accounts.

%prep
%setup -q -n azure-storage-azcopy-%{version}

%build
export GOARCH=amd64 GOOS=linux
go build -o ./build/azcopy_linux_amd64

%install
mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
install -m 755 ./build/azcopy_linux_amd64 ${RPM_BUILD_ROOT}/%{_bindir}/azcopy

%files
%{_bindir}/azcopy
%doc ChangeLog.md LICENSE NOTICE.txt README.md

%changelog
* Thu Feb 01 2024 Rio Fujita <rifujita@microsoft.com> - 10.23.0-1
- Update to 10.23.0

* Wed Jan 25 2023 Rio Fujita <rifujita@microsoft.com> - 10.17.0-1
- Update to 10.17.0

* Fri Aug 05 2022 Rio Fujita <rifujita@microsoft.com> - 10.16.0-1
- Update to 10.16.0

* Fri Apr 15 2022 Rio Fujita <rifujita@microsoft.com> - 10.14.1-1
- Update to 10.14.1

* Tue Mar 01 2022 Rio Fujita <rifujita@microsoft.com> - 10.14.0-1
- Rebase to 10.14

* Tue Nov 09 2021 Rio Fujita <rifujita@microsoft.com> - 10.13.0-1
- First build for RHEL8.4
