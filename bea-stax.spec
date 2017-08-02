%{?scl:%scl_package bea-stax}
%{!?scl:%global pkg_name %{name}}

# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global apiver  1.0.1

Summary:        Streaming API for XML
URL:            http://stax.codehaus.org/Home
Source0:        http://dist.codehaus.org/stax/distributions/stax-src-%{version}.zip
Source1:        http://dist.codehaus.org/stax/jars/stax-%{version}.pom
Source2:        http://dist.codehaus.org/stax/jars/stax-api-%{apiver}.pom
Name:           %{?scl_prefix}bea-stax
Version:        1.2.0
Release:        14.1%{?dist}
License:        ASL 1.1 and ASL 2.0
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}javapackages-local
BuildRequires:  %{?scl_prefix}ant
BuildRequires:  %{?scl_prefix}xerces-j2
BuildRequires:  %{?scl_prefix}xalan-j2

%description
The Streaming API for XML (StAX) is a groundbreaking
new Java API for parsing and writing XML easily and
efficiently.

%package api
Summary:        The StAX API

%description api
%{summary}

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
%{summary}

%prep
%setup -q -c -n %{pkg_name}-%{version}

# Convert CR+LF to LF
%{__sed} -i 's/\r//' ASF2.0.txt

cp -p %{SOURCE1} pom.xml

# Incorrectly scoped
%pom_remove_dep :junit

%build
ant all javadoc

%install
%mvn_file ':{*}' bea-@1
%mvn_package :stax-api api
%mvn_alias :stax-api javax.xml.stream:stax-api
%mvn_artifact pom.xml build/stax-%{version}-dev.jar
%mvn_artifact %{SOURCE2} build/stax-api-%{apiver}.jar

%mvn_install -J build/javadoc

%files -f .mfiles
%license ASF2.0.txt

%files api -f .mfiles-api
%license ASF2.0.txt

%files javadoc -f .mfiles-javadoc
%license ASF2.0.txt

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.2.0-14.1
- Automated package import and SCL-ization

* Wed Mar 22 2017 Michael Simacek <msimacek@redhat.com> - 1.2.0-14
- Install with XMvn

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-9
- Use .mfiles generated during build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 28 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-6
- Remove unneeded patch

* Wed Nov 14 2012 Jaromir Capik <jcapik@redhat.com> - 1.2.0-5
- ASL 1.1 was missing

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 29 2011 Jaromir Capik <jcapik@redhat.com> - 1.2.0-2
- Symlink "-ri" created for backward compatibility

* Thu Sep 29 2011 Jaromir Capik <jcapik@redhat.com> - 1.2.0-1
- Update to 1.2.0
- Introduction of POM files and depmaps

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2.0-0.8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 7 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.2.0-0.7.rc1
- BR java 1.6.0.

* Thu Oct 7 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.2.0-0.6.rc1
- Drop gcj support.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2.0-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.2.0-0.3.rc1
- drop repotag
- fix license

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.2.0-0.2.rc1.2jpp.1
- Autorebuild for GCC 4.3

* Mon Feb 12 2007 Vivek Lakshmanan <vivekl@redhat.com> 0:1.2.0-0.1.rc1.2jpp.1.fc7
- Use new naming convention
- Add ASF2.0.txt as doc for api and main package
- Remove post/postun magic for javadoc
- Add BR on ant, xerces-j2 and xalan-j2
- Add conditional patch to make the package build under ecj/gcj

* Wed Jan 18 2006 Fernando Nasser <fnasser@redhat.com> 0:1.2.0-0.rc1.2jpp
- First JPP 1.7 build

* Wed Jan 18 2006 Deepak Bhole <dbhole@redhat.com> 0:1.2.0-0.rc1.1jpp
- Change source zip, and build the ri jars
- Use setup macro in prep
- First version all under APL
- New package name
- Demo still not yet available under the APL; will be in an update

* Tue Apr 26 2005 Fernando Nasser <fnasser@redhat.com> 0:1.0-2jpp_2rh
- First Red Hat build

* Wed Oct 20 2004 David Walluck <david@jpackage.org> 0:1.0-2jpp
- fix build

* Thu Sep 09 2004 Ralph Apel <r.apel at r-apel.de> 0:1.0-1jpp
- First JPackage build 
- Note: there is a stax project starting at codehaus
