from dataclasses import dataclass

from ..interfaces import LocationState, ContactRate, SimTime, SimTimeTuple, LocationRule, globals, BaseLocation, BusinessLocationState, EssentialBusinessBaseLocation

__all__ = ['Bus', 'BusState']

@dataclass
class BusState(BusinessLocationState):
    contact_rate: ContactRate = ContactRate(0, 2, 1, 0, 0.3, 0.25)
    open_time = SimTimeTuple = SimTimeTuple(hours=tuple(range(8, 9)), week_days=tuple(range(0, 5))) 

class Bus(EssentialBusinessBaseLocation[BusState]):
    '''Class that implements a standard Bus location. '''
    state_type = BusState
