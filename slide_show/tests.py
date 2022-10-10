from django.test import TestCase

from slide_show.models import SlideShow, Slide
from users.models import CustomUser


class SlideShowTest(TestCase):
    def setUp(self):
        self.user = CustomUser()
        self.user.save()

        self.slide_show = SlideShow(
            title="asdasd",
            description="a description",
            user=self.user,
            secret_number=1234
        )
        self.slide_show.save()

    def test_clone_a_slide_show_increment_the_number_of_slides_in_1(self):
        secret_number = self.slide_show.secret_number

        self.slide_show.clone_slide_show()

        self.assertTrue(SlideShow.objects.count(), 2)
        self.assertTrue(self.slide_show.user, self.user)
        self.assertNotEqual(self.slide_show.secret_number, secret_number)

    def test_when_edit_a_slide_show_the_secret_number_dont_change(self):
        secret_number = self.slide_show.secret_number
        user = self.slide_show.user
        title = self.slide_show.title

        self.slide_show.set_new_title("a new title for slide")
        self.slide_show.save()

        self.assertEqual(self.slide_show.secret_number, secret_number)
        self.assertEqual(self.slide_show.user, user)
        self.assertNotEqual(self.slide_show.title, title)

    def test_a_new_slide_show_has_not_slides(self):
        self.assertEqual(len(self.slide_show.slides()), 0)

    def test_add_two_slides_to_a_slide_show_and_the_lend_of_their_slides_is_two(self):
        slide_1 = Slide(
            slide_show=self.slide_show,
            title="title from slide one"
        )
        slide_1.save()

        slide_2 = Slide(
            slide_show=self.slide_show,
            title="title from slide two"
        )
        slide_2.save()

        self.assertEqual(len(self.slide_show.slides()), 2)
