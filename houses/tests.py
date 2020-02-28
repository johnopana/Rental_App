from django.test import TestCase
from .models import Profile,House,Owner



class ProfileTestClass(TestCase):
    #Set up method

    def setUp(self):

        self.new_profile = Profile(user_id=2,name="Titus",bio="just testing", email='titusouko@gmail.com',profile_pic="image.jpeg")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)

    def tearDown(self):
        Profile.objects.all().delete()

class HouseTestClass(TestCase):

    def setUp(self):
        self.new_owner=Owner(first_name='Peter',last_name='Okumu',address="mwmama", email="peter@gmail.com",phone='0789456765', owner_pic='owner.png')
        self.new_owner.save()
        self.new_house=House(house_no='3F',registry_no="938348H",house_location="lavington",house_pic='image.png',house_type="rental", no_of_rooms=5, price=22000, owner=self.new_owner)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_house,House))

    def test_save_house(self):
        self.new_house.save_house()
        house = House.objects.all()
        self.assertTrue(len(house)>0)

    def test_delete_house(self):
        self.new_house.save_house()
        self.new_house.delete_house()
        house = House.objects.all()
        self.assertTrue(len(house)==0)

    def test_update_house_type_method(self):
        self.new_house.save_house()
        new_name = 'rental'
        update = self.new_house.update_house(self.new_house.id,new_name)
        self.assertEqual(update,new_name)


    def test_find_method(self):
        self.new_house.save_house()
        house = self.new_house.find_house(self.new_house.id)
        self.assertEqual(house.house_location,'lavington')

    def tearDown(self):
        House.objects.all().delete()

class OwnerTestClass(TestCase):

    def setUp(self):
        self.new_owner=Owner(first_name='Peter',last_name='Okumu',address="mwmama", email="peter@gmail.com",phone='0789456765', owner_pic='owner.png')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_owner,Owner))

    def test_save_owner(self):
        self.new_owner.save_owner()
        owner = Owner.objects.all()
        self.assertTrue(len(owner)>0)



    def test_delete_owner(self):
        self.new_owner.save_owner()
        self.new_owner.delete_owner()
        owner = Owner.objects.all()
        self.assertTrue(len(owner) is 0)

    def tearDown(self):
        Owner.objects.all().delete()
