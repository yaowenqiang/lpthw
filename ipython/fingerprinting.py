import platform

'''
Finterprints the following operation systems:
* MAC OS X
* Ubuntu
* Red Hat/Cent OS
* FreeBSD
* SunOS
'''

class OpSysType(object):
    """Determines OS type using platform module"""

    def __getattr__(self, attr):
        if attr == 'osx':
            return 'osx'
        elif attr == 'rhel':
            return 'redHat'
        elif attr == 'ubu':
            return 'ubuntu'
        elif attr == 'debian':
            return 'debian'
        elif attr == 'fbsd':
            return "FreeBSD"
        elif attr == 'unknown_linux':
            return 'unknown'
        else:
            raise  AttributeError


    def linuxType(self):
        '''Uses various methods to datetime Linux Type'''

        if platform.dist()[0] == self.rhel:
            return self.rhel
        elif platform.dist()[0] == self.ubu:
            return self.ubu
        elif platform.dist()[0] == self.debian:
            return self.debian
        else:
            return self.unknown_linux


    def queryOS(self):
        if platform.system() == 'Darwin':
            return self.osx
        elif platform.system() == 'Linux':
            return self.linuxType()
        elif platform.system() == self.fbsd:
            return self.fbsd


def fingerprint():
    type = OpSysType()
    print(type.queryOS())

if __name__ == '__main__':
    fingerprint()



