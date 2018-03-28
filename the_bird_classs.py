class Bird:
    def __init__(self, kind, call):
        # made kind and call private with _kind and _call
        self._kind = kind
        self._call = call
    
    def do_call(self):
        print 'a %s goes %s' % (self.kind, self.call)


owl = Bird('Owl', 'Twir Twoo!')
print owl._kind