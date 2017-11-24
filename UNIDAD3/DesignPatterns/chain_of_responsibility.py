"""Name: Jose Antonio Enriquez Cabrera.
   Group: GITI9072."""
class Handler: #abtrsct handler
    """abstract handler"""
    def __init__(self, successor):
        self.successor = successor #define who is the next handler

    def handler(self, request):
        handler = self._hardler(request) #If handler , stop hare

        #Otherwise , keep going
        if not handler:
            self._successor.handler(request)

    def _handler(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler): #Inherits form the abstract handler
    """Concrete handler 1"""
    def _handler(self, request):
        if 0 < request <= 10: #provide  a condition sor handling
            print("request {} handler 1".format(request))
            return True #indicate that the request has been handler

class DefaultHandler(Handler): #Inherits from the abstract  handler
    """Default Handler"""

    def _handler(self, request):
        """If there is not  handler avaliable """
        #No condition checking since this a deafault handler
        print("End of chain, no handler for {}".format(request))
        return True #Indicates that the reques has been handler

class Client: #using handlers
    def __init__(self):
      self.handler = ConcreteHandler(DefaultHandler(None)) #Create handlers and use them is a sequense you want
                                                            #Note that the default handler has no successor
    def delegate(self, requests): #send yours requests one at a time for handlers  to handler
        for request in requests:
            self.handler .handler(request)

# Create  a client
c = Client()
#Create requests
requests = [2, 5, 30]
#send the requests
c.delegate(requests)