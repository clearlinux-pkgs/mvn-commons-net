#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-net
Version  : 3.1
Release  : 1
URL      : https://repo1.maven.org/maven2/commons-net/commons-net/3.1/commons-net-3.1.jar
Source0  : https://repo1.maven.org/maven2/commons-net/commons-net/3.1/commons-net-3.1.jar
Source1  : https://repo1.maven.org/maven2/commons-net/commons-net/3.1/commons-net-3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-net-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-net package.
Group: Data

%description data
data components for the mvn-commons-net package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-net/commons-net/3.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/commons-net/commons-net/3.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-net/commons-net/3.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/commons-net/commons-net/3.1


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/commons-net/commons-net/3.1/commons-net-3.1.jar
/usr/share/java/.m2/repository/commons-net/commons-net/3.1/commons-net-3.1.pom
