from conans import ConanFile, tools

class LibtorrentPythonTestConan(ConanFile):
    requires = "LibtorrentPython/1.1.4@lola/libtorrent"

    def test(self):
      # self.conanfile_directory
      with tools.pythonpath(self):
            import libtorrent
            print("Libtorrent version: %s" % libtorrent.version)
