Name:           ros-kinetic-octomap
Version:        1.8.1
Release:        0%{?dist}
Summary:        ROS octomap package

Group:          Development/Libraries
License:        BSD
URL:            http://octomap.github.io
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-catkin
BuildRequires:  cmake

%description
The OctoMap library implements a 3D occupancy grid mapping approach, providing
data structures and mapping algorithms in C++. The map implementation is based
on an octree. See http://octomap.github.io for details.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Jan 13 2017 Armin Hornung <armin@hornung.io> - 1.8.1-0
- Autogenerated by Bloom

* Thu Apr 21 2016 Armin Hornung <armin@hornung.io> - 1.8.0-0
- Autogenerated by Bloom

* Tue Mar 29 2016 Armin Hornung <armin@hornung.io> - 1.7.2-1
- Autogenerated by Bloom

* Sat Mar 26 2016 Armin Hornung <armin@hornung.io> - 1.7.2-0
- Autogenerated by Bloom

* Thu Mar 24 2016 Armin Hornung <armin@hornung.io> - 1.7.1-0
- Autogenerated by Bloom

