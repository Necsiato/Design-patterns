class Duck:
    def quack(self):
        pass

    def fly(self):
        pass


class Turkey:
    def gobble(self):
        pass

    def fly(self):
        pass

class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()


class MallardDuck(Duck):
    def quack(self):
        print("Quack!")

    def fly(self):
        print("I'm flying!")


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("I'm flying a short distance")

def duck_interaction(duck):
    duck.quack()
    duck.fly()

if __name__ == "__main__":
    duck = MallardDuck()
    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)

    print("The Turkey says:")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck says:")
    duck_interaction(duck)

    print("\nThe TurkeyAdapter says:")
    duck_interaction(turkey_adapter)
