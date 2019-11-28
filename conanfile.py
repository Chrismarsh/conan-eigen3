import os
from conans import ConanFile, CMake
from conans.tools import download, unzip

class Eigen3Conan(ConanFile):
    name = "eigen3"
    description = "Eigen is a C++ template library for linear algebra"
    version = "3.3.7"
    generators = "cmake"
    # exports = ["FindEigen3.cmake"]
    url="http://github.com/bilke/conan-eigen3"
    license="http://eigen.tuxfamily.org/index.php?title=Main_Page#License"

    def source(self):
        zip_name = "%s.zip" % self.version
        download("http://bitbucket.org/eigen/eigen/get/%s" % zip_name , zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="eigen-eigen-323c052e1731")
        return cmake

    def build(self):

        cmake = self.configure_cmake()
        cmake.build()


    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        return
        # self.cpp_info.includedirs = ['.', './unsupported']
