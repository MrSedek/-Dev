from model.group import Group
from timeit import timeit
def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))
    # us_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    # db_list = db.get_group_list()
    print(timeit(lambda : db.get_group_list(), number=1000))
    assert False
    # assert sorted(us_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)