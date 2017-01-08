import mock


# Mock RPi.GPIO module (https://m.reddit.com/r/Python/comments/5eddp5/mock_testing_rpigpio/)
MockRPi = mock.MagicMock()
modules = {
    'RPi': MockRPi,
    'RPi.GPIO': MockRPi.GPIO,
}
patcher = mock.patch.dict('sys.modules', modules)
patcher.start()
