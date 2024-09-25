class State:
    def insert_quarter(self):
        pass

    def eject_quarter(self):
        pass

    def turn_crank(self):
        pass

    def dispense(self):
        pass

class NoQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You inserted a quarter.")
        self.gumball_machine.set_state(self.gumball_machine.has_quarter_state)

    def eject_quarter(self):
        print("You haven't inserted a quarter.")

    def turn_crank(self):
        print("You turned, but there's no quarter.")

    def dispense(self):
        print("You need to pay first.")

class HasQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert another quarter.")

    def eject_quarter(self):
        print("Quarter returned.")
        self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)

    def turn_crank(self):
        print("You turned...")
        if self.gumball_machine.count > 1 and self.gumball_machine.is_winner():
            self.gumball_machine.set_state(self.gumball_machine.winner_state)
        else:
            self.gumball_machine.set_state(self.gumball_machine.sold_state)

    def dispense(self):
        print("No gumball dispensed.")

class SoldState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Please wait, we're already giving you a gumball.")

    def eject_quarter(self):
        print("Sorry, you already turned the crank.")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.count > 0:
            self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)
        else:
            print("Oops, out of gumballs!")
            self.gumball_machine.set_state(self.gumball_machine.sold_out_state)

class WinnerState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Please wait, we're already giving you a gumball.")

    def eject_quarter(self):
        print("Sorry, you already turned the crank.")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        print("YOU'RE A WINNER! You get two gumballs for your quarter!")
        self.gumball_machine.release_ball()
        if self.gumball_machine.count == 0:
            self.gumball_machine.set_state(self.gumball_machine.sold_out_state)
        else:
            self.gumball_machine.release_ball()
            if self.gumball_machine.count > 0:
                self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)
            else:
                print("Oops, out of gumballs!")
                self.gumball_machine.set_state(self.gumball_machine.sold_out_state)

class SoldOutState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert a quarter, the machine is sold out.")

    def eject_quarter(self):
        print("You can't eject, you haven't inserted a quarter yet.")

    def turn_crank(self):
        print("You turned, but there are no gumballs.")

    def dispense(self):
        print("No gumball dispensed.")

class GumballMachine:
    def __init__(self, number_gumballs):
        self.sold_out_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.winner_state = WinnerState(self)

        self.count = number_gumballs
        if number_gumballs > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        if self.count > 0:
            print("A gumball comes rolling out the slot...")
            self.count -= 1

    def is_winner(self):
        # Здесь рандомное определение победителя, можно заменить на любое другое условие
        import random
        return random.randint(0, 9) == 0

    def __str__(self):
        return f"Gumball Machine [balls: {self.count}, state: {self.state.__class__.__name__}]"

def test_gumball_machine():
    gumball_machine = GumballMachine(5)

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.eject_quarter()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

test_gumball_machine()
