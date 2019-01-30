# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    # symbols = string.ascii_letters+string.digits + string.punctuation + ' '*10
    symbols = string.ascii_letters+string.digits + ' '*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string('name', 10), header=random_string('header', 20), footer=random_string('footer', 20))
    for i in range(5)
    # for name in ["", random_string('name', 10)]
    # for header in ["", random_string('header', 20)]
    # for footer in ["", random_string('footer', 20)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



"""
def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
"""




"""    
def test_add_new_user(app):
    app.session.login(username="admin", password="secret")
    app.new_user.create(fName="FirstName", mName="MiddleName", lName="LastName", nickName="NickName", photo="C:\\fakepath\\0cb40312-3390-415a-8000-eb9d0667ce6c.jpg",
                        title="Title", company="Company", address="Address", hTel="80291111111", mTel="80292222222", wTel="80293333333", eMail="email@email.com",
                        homepage="http://localhost.ru", sAddress="Sec Address", sHome="Sec Home", sNotes="Sec Notes")
    app.session.logout()
"""
