import mock
import pytest


# Mock RPi.GPIO module (https://m.reddit.com/r/Python/comments/5eddp5/mock_testing_rpigpio/)
MockRPi = mock.MagicMock()
modules = {
    'RPi': MockRPi,
    'RPi.GPIO': MockRPi.GPIO,
}
patcher = mock.patch.dict('sys.modules', modules)
patcher.start()


# Provide default kwargs for a CharLCD instance
@pytest.fixture
def charlcd_kwargs():
    import RPi.GPIO as GPIO
    return {
        'numbering_mode': GPIO.BOARD,
        'pin_rs': 15,
        'pin_rw': 18,
        'pin_e': 16,
        'pins_data': [21, 22, 23, 24],
    }
