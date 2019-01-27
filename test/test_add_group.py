# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="NewGroupName", header="NewGroupHeader", footer="NewGroupFooter"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


"""    
def test_add_new_user(app):
    app.session.login(username="admin", password="secret")
    app.new_user.create(fName="FirstName", mName="MiddleName", lName="LastName", nickName="NickName", photo="C:\\fakepath\\0cb40312-3390-415a-8000-eb9d0667ce6c.jpg",
                        title="Title", company="Company", address="Address", hTel="80291111111", mTel="80292222222", wTel="80293333333", eMail="email@email.com",
                        homepage="http://localhost.ru", sAddress="Sec Address", sHome="Sec Home", sNotes="Sec Notes")
    app.session.logout()
"""
