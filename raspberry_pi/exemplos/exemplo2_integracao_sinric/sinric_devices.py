
def power_state(device_id, state):
    print(device_id, state)
    return True, state
 
switch_callbacks = {
    'powerState': power_state
}