class Bird:
    def __init__(self, kind, call):
        # made kind and call private with _kind and _call
        self._kind = kind
        self._call = call
    
    def do_call(self):
        print 'a %s goes %s' % (self._kind, self._call)


owl = Bird('Owl', 'Twir Twoo!')
print owl._kind

# The parrot class inherits and re-uses the methods from the Bird class
class Parrot(Bird):
    def __init__(self):
        # add specialised behaviour, and 
        # overide exisiting methods:
        Bird.__init__(self, 'Parrot', 'Kah!')
        # parrots can learn phrases, so we 
        # initialise an empty set in the initializer
        self.learned_phrases = set()
    #This is a method specific to the Parrot class 
    #which allows it to learn a phrase, and adds it 
    #to the set.
    def learn_phrase(self, phrase):
        self.learned_phrases.add(phrase)
    #We override the do_call method of the parent class 
    #so that the learned phrases are printed after the call.
    def do_call(self):
        Bird.do_call(self)
        print '\n'.join(self.learned_phrases)