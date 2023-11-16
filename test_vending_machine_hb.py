# Updated by Hudson Brown, 100900963 on November 15, 2023
# for TPRG 2131
# Submitted to Phillip Jarvis on November 16, 2023

from vending_machine_hb import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState
import gpiozero
#import PySimpleGUI as sg
 
def test_VendingMachine():
    # new machine object
    vending = VendingMachine()

    # Add the states - ORG
    # vending.add_state(WaitingState()) 
    # vending.add_state(CoinsState())
    # vending.add_state(DispenseState())
    # vending.add_state(ChangeState())
    # My revisions
    vending.add_state(WaitingState())
    vending.add_state(AddCoinsState())
    vending.add_state(DeliverProductState())
    vending.add_state(CountChangeState())
    # Reset state is "waiting for first coin"
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'
    # test that the first coin causes a transition to 'coins'
    vending.event = "$200" # a twonie
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 200 # pennies, was .total