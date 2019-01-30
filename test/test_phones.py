import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[1]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)


def test_phones_on_contact_view_page(app):
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(1)
    assert contact_from_edit_page.homephone == contact_from_view_page.homephone
    assert contact_from_edit_page.secondaryphone == contact_from_view_page.secondaryphone
    assert contact_from_edit_page.workphone == contact_from_view_page.workphone
    assert contact_from_edit_page.mobilephone == contact_from_view_page.mobilephone


def clear(phone):
    return re.sub("-() ", "", phone)
