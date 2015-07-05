'''
Created on Nov 24, 2014

@author: aborgo
'''

class Publisher:
    def __init__(self):
        self.subscribers  = []
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
    def publish(self, s):
        sub_list = self.subscribers.copy()
        for subscriber in sub_list:
            subscriber(s)
            

if __name__ == '__main__':

    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self.name = name
            self.publisher = publisher
            publisher.subscribe(self.process)
            self.count = 0
        def process(self, s):
            print(self, ":", s.upper())
            self.count += 1
            if self.count > 2:
                self.publisher.unsubscribe(self.process)
        def __repr__(self):
            return self.name

    publisher = Publisher()
    for i in range(6): 
        newsub = SimpleSubscriber("Sub"+str(i), publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)

