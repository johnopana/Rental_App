import pytest
from django.db import transaction, IntegrityError
from .models import Profile,House,Owner


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Profile()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Profile(user_id=1,name="Titus",bio="just testing", email='titusouko@gmail.com',profile_pic="image.jpeg")
@pytest.fixture
def test_instance(wallet):
    assert (isinstance(wallet,Profile))

@pytest.mark.django_db
def test_save_method(wallet):
    wallet.save_profile()
    assert Profile.objects.count()==1

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return House()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return House(house_no='3F',registry_no="938348H",house_location="lavington",house_pic='image.png',house_type="rental", no_of_rooms=5, price=22000, owner=self.new_owner)
@pytest.fixture
def test_instance(wallet):
    assert (isinstance(wallet,House))

@pytest.mark.django_db
def test_save_method(wallet):
    wallet.save_house()
    assert House.objects.count()==1



@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Owner()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Owner(first_name='Peter',last_name='Okumu',address="mwmama", email="peter@gmail.com",phone='0789456765', owner_pic='owner.png')
def test_instance(wallet):
    assert (isinstance(wallet,Owner))

@pytest.mark.django_db
def test_save_method(wallet):
    wallet.save_owner()
    assert Owner.objects.count()==1
