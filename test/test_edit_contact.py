from model.contact import Contact


def test_edit_first_contact_general_info(app):
    old_contact_list = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="TEST"))
    contact = Contact(first_name="EDITED", middle_name="EDITED", last_name="EDITED", nickname="EDITED",
                      title="EDITED", company="EDITED", address="EDITED")
    app.contact.edit_first(contact)
    contact.id = old_contact_list[0].id
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    old_contact_list[0] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


"""
def test_edit_first_contact_phone_info(app):
    old_contact_list = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="TEST"))
    app.contact.edit_first(Contact(home_phone=" EDITED", mobile_phone=" EDITED", work_phone=" EDITED", fax=" EDITED"))
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)


def test_edit_first_contact_email_info(app):
    old_contact_list = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="TEST"))
    app.contact.edit_first(Contact(email1=" EDITED", email2=" EDITED", email3=" EDITED"))
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)


def test_edit_first_contact_other_info(app):
    old_contact_list = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="TEST"))
    app.contact.edit_first(Contact(homepage_link=" EDITED", birthday_day="//div[@id='content']/form/select[1]//option[3]",
                                   birthday_month="//div[@id='content']/form/select[2]//option[3]",
                                   birthday_year=" EDITED", anniversary_day="//div[@id='content']/form/select[3]//option[3]",
                                   anniversary_month="//div[@id='content']/form/select[4]//option[3]",
                                   anniversary_year=" EDITED", secondary_address=" EDITED", home_phone2=" EDITED",
                                   notes=" EDITED"))
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
"""