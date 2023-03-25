from RPLCD.gpio import CharLCD


def test_missing_numbering_mode(mocker, charlcd_kwargs):
    kwargs = {
        'pin_rs': 15,
        'pin_rw': 18,
        'pin_e': 16,
        'pins_data': [21, 22, 23, 24],
    }
    try:
        CharLCD(**kwargs)
    except ValueError as ex:
        assert 'https://gist.github.com/dbrgn/77d984a822bfc9fddc844f67016d0f7e' in str(ex)
    else:
        assert False, 'ValueError not raised'
