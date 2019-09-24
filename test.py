import pytest


@pytest.fixture
def init():
    from little_world import Country
    from little_world import Walker
    class Map:
        pass

    init_map = Map()
    init_map.greg = Walker("Greg")
    init_map.bill = Walker("Bill")
    init_map.england = Country("England")
    init_map.scotland = Country("Scotland")
    init_map.northern_ireland = Country("Northern Ireland")
    return init_map


def test_person_addition_works(init):
    init.greg + init.bill


def test_person_country_addition_works(init):
    init.greg + init.england


def test_country_addition_works(init):
    init.scotland + init.england


@pytest.fixture
def mini_map(init):
    init.england + init.scotland
    init.bill + init.england
    init.greg + init.england
    init.bill + init.greg
    return init


def test_adding_countries_twice(mini_map, capsys):
    mini_map.england + mini_map.scotland
    capture = capsys.readouterr()
    assert capture.out is not ''


def test_adding_walkers_twice(mini_map, capsys):
    mini_map.bill + mini_map.greg
    capture = capsys.readouterr()
    assert capture.out is not ''


def test_adding_countries_and_walkers_twice(mini_map, capsys):
    mini_map.bill + mini_map.england
    capture = capsys.readouterr()
    assert capture.out is not ''


def test_join_countries_connection_count_self(mini_map):
    assert mini_map.england.connection_count == 1


def test_join_countries_connection_count_other(mini_map):
    assert mini_map.scotland.connection_count == 1


def test_join_walkers_love_self(mini_map):
    assert mini_map.greg.love == 1


def test_join_walkers_love_other(mini_map):
    assert mini_map.bill.love == 1


def test_join_walkers_lovers_self(mini_map):
    assert mini_map.bill.lovers is not []


def test_join_walker_and_country_home(mini_map):
    assert "England" in mini_map.greg.home


def test_join_walker_and_country_citizens(mini_map):
    assert not mini_map.england.citizens == 0


def test_join_countries_connection_list_self(mini_map):
    assert mini_map.england.connection_list is not []


def test_join_countries_connection_list_other(mini_map):
    assert mini_map.scotland.connection_list is not []


@pytest.fixture
def mini_map_subbed(mini_map):
    mini_map.scotland - mini_map.england
    mini_map.greg - mini_map.bill
    mini_map.greg - mini_map.england
    mini_map.bill - mini_map.england
    return mini_map


def test_separate_countries_connection_count(mini_map_subbed):
    assert mini_map_subbed.scotland.connection_count == 0


def test_separate_countries_connection_list(mini_map_subbed):
    assert mini_map_subbed.scotland.connection_list == []


def test_country_doesnt_separate_twice(mini_map_subbed, capsys):
    mini_map_subbed.scotland - mini_map_subbed.england
    capture = capsys.readouterr()
    assert capture.out is not ''


def test_walker_and_country_dont_separate_twice(mini_map_subbed, capsys):
    mini_map_subbed.scotland - mini_map_subbed.greg
    capture = capsys.readouterr()
    assert capture.out is not ''


def test_walker_doesnt_separate_twice(mini_map_subbed, capsys):
    mini_map_subbed.greg - mini_map_subbed.bill
    capture = capsys.readouterr()
    assert capture.out is not ''


def test_walker_moves_country(mini_map):
    mini_map.greg.step()
    assert mini_map.england not in mini_map.greg.home
    assert mini_map.greg.home is not []


def test_homeless_walker_cannot_move(mini_map_subbed, capsys):
    mini_map_subbed.greg.step()
    capture = capsys.readouterr()
    assert capture.out is not ''


def test_walker_will_stay_home_if_no_options_available(mini_map):
    mini_map.england - mini_map.scotland
    mini_map.greg.step()
    assert mini_map.england in mini_map.greg.home


