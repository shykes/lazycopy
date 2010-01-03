
import os
import sys

import aufs

class Copy(aufs.AUFS):

    def create(self):
        if not os.path.exists(self.changes):
            os.makedirs(self.changes)

    def get_aufsdir(self):
        return os.path.join(self.mountpoint, ".aufs")
    aufsdir = property(get_aufsdir)

    def get_changes(self):
        return os.path.join(self.aufsdir, "0")
    changes = property(get_changes)

    def get_sources(self):
        return [path for (path, access) in self.layers if access == "ro"]

    def set_sources(self, sources):
        self.create()
        if sources:
            self.layers = [(self.changes, "rw")] + [(path, "ro") for path in sources]
        else:
            self.layers = []

    sources = property(get_sources, set_sources)
