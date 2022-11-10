from dataclasses import dataclass

from ..interfaces import LocationState, ContactRate, SimTime, SimTimeTuple, BusinessLocationState, EssentialBusinessBaseLocation, NonEssentialBusinessBaseLocation, NonEssentialBusinessLocationState

__all__ = ['Bus', 'BusState']

@dataclass
class BusState(NonEssentialBusinessLocationState):
    contact_rate: ContactRate = ContactRate(0, 2, 1, 0, 0.3, 0.25)
    open_time = SimTimeTuple = SimTimeTuple(hours=tuple(range(8, 9)), week_days=tuple(range(0, 5))) 

class Bus(NonEssentialBusinessBaseLocation[BusState]):
    '''Class that implements a standard Bus location. '''
    state_type = BusState
