import os
from conans import ConanFile, CMake
from conans.tools import download, unzip
from glob import glob
class EigenConan(ConanFile):
    name = "eigen3"
    description = "Eigen is a C++ template library for linear algebra"
    version = "3.3.7"
    generators = "cmake"
    settings = None #header only
    url="http://github.com/bilke/conan-eigen3"
    license="http://eigen.tuxfamily.org/index.php?title=Main_Page#License"


    def source(self):
        zip_name = "eigen-%s.zip" % self.version
        download("https://gitlab.com/libeigen/eigen/-/archive/%s/%s" % (self.version,zip_name),zip_name)
        unzip(zip_name)
        os.unlink(zip_name)
        os.rename(glob("eigen-eigen-*")[0], "eigen")

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="eigen")
        return cmake

    def build(self):

        cmake = self.configure_cmake()
        cmake.build()


    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.name = "Eigen3"
        self.cpp_info.includedirs = ['include/eigen3', 'include/unsupported']
