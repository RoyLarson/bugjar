import bugjar


def test_get_git_changeset():
    datetimestr = bugjar.get_git_changeset()
    print(datetimestr)
    assert datetimestr
    assert datetimestr == '20160927034814'


def test_init_version():
    version = bugjar.VERSION
    print(version)
    assert version


if __name__ == '__main__':
    test_init_version()
    test_get_git_changeset()
