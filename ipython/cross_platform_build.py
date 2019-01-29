from fingerprinting import fingerprint
from subprocess import call


os = fingerprint()
# Get epm keyword correct

epm_keyword = {'debian':'deb','redhat':'rpm', 'SunOS':'pkg','osx':'osx'}
platform_cmd =  epm_keyword[os]
call([f'epm -f {platform_cmd} helloEPM helloepm.list'], shell=True)
