# -*- coding: utf-8 -*-
from model.group import Group, maxsize

def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="NewGroup1", header="NewGroupHeader", footer="NewGroupFooter")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





"""    
def test_add_new_user(app):
    app.session.login(username="admin", password="secret")
    app.new_user.create(fName="FirstName", mName="MiddleName", lName="LastName", nickName="NickName", photo="C:\\fakepath\\0cb40312-3390-415a-8000-eb9d0667ce6c.jpg",
                        title="Title", company="Company", address="Address", hTel="80291111111", mTel="80292222222", wTel="80293333333", eMail="email@email.com",
                        homepage="http://localhost.ru", sAddress="Sec Address", sHome="Sec Home", sNotes="Sec Notes")
    app.session.logout()
"""
