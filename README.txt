lazycopy v.0.0.1

Author: Solomon Hykes <solomon.hykes@dotcloud.com>
License : see LICENSE file.
Url: http://bitbucket.org/dotcloud/lazycopy

Description:
------------

lazycopy is a simple command-line tool to copy directories lazily. Data will be copied on-write.

The copy-on-write magic is made possible by AUFS, a wonderful filesystem by Junjiro R. Okajima.


Requirements:
-------------

lazycopy will only work on a system with aufs (version 1 or 2) installed. See http://aufs.sf.net for instructions.

