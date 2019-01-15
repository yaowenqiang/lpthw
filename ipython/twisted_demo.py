from twisted.internet import reactor,protocol
import sys

class PortCheckerProtocol(protocol.Protocol):
    def __init__(self):
        print("Created a new protocol")


    def connectionMade(self):
        print("Connection made")
        reactor.stop()




class PortCheckerclientFactory(protocol.ClientFactory):
    protocol = PortCheckerProtocol

    def clientconnectionFailed(self, connector, reason):
        print(f"Connection failed because {reason}")
        reactor.stop()


if __name__ == '__main__':
    host, port = sys.argv[1].split(':')

    factory = PortCheckerclientFactory()

    print(f"testing {sys.argv[1]}")

    reactor.connectTCP(host, int(port), factory)

    reactor.run()
