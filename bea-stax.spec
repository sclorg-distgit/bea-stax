%global pkg_name bea-stax
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

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

%global mainver 1.2.0
%global apiver  1.0.1

Summary:        Streaming API for XML
URL:            http://stax.codehaus.org/Home
Source0:        http://dist.codehaus.org/stax/distributions/stax-src-1.2.0.zip
Source1:        http://dist.codehaus.org/stax/jars/stax-1.2.0.pom
Source2:        http://dist.codehaus.org/stax/jars/stax-api-1.0.1.pom
Name:           %{?scl_prefix}%{pkg_name}
Version:        %{mainver}
Release:        9.7%{?dist}
License:        ASL 1.1 and ASL 2.0
BuildArch:      noarch

BuildRequires:          %{?scl_prefix}javapackages-tools
BuildRequires:          %{?scl_prefix}ant
BuildRequires:          %{?scl_prefix}xerces-j2
BuildRequires:          %{?scl_prefix}xalan-j2

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
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

# Convert CR+LF to LF
%{__sed} -i 's/\r//' ASF2.0.txt
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
export CLASSPATH=`pwd`/build/stax-api-%{apiver}.jar
ant all javadoc
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
# jar
install -Dpm 0644 build/stax-api-%{apiver}.jar %{buildroot}%{_javadir}/%{pkg_name}-api.jar
install -Dpm 0644 build/stax-%{version}-dev.jar %{buildroot}%{_javadir}/%{pkg_name}.jar
# the following symlink can be removed once no package needs "bea-stax-ri"
ln -s %{pkg_name}.jar %{buildroot}%{_javadir}/%{pkg_name}-ri.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# pom
install -Dpm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{pkg_name}.pom
install -Dpm 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP-%{pkg_name}-api.pom

%add_maven_depmap JPP-%{pkg_name}.pom %{pkg_name}.jar
%add_maven_depmap -f api -a "javax.xml.stream:stax-api" JPP-%{pkg_name}-api.pom %{pkg_name}-api.jar
%{?scl:EOF}

%files
%doc ASF2.0.txt
%{_javadir}/%{pkg_name}.jar
%{_javadir}/%{pkg_name}-ri.jar
%{_mavenpomdir}/JPP-%{pkg_name}.pom
%{_mavendepmapfragdir}/%{pkg_name}


%files api
%doc ASF2.0.txt
%{_javadir}/%{pkg_name}-api.jar
%{_mavenpomdir}/JPP-%{pkg_name}-api.pom
%{_mavendepmapfragdir}/%{pkg_name}-api

%files javadoc
%doc ASF2.0.txt
%doc %{_javadocdir}/*

%changelog
* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-9.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-9.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-9.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-9.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-9.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-9.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-9.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.0-9
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-8
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

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
