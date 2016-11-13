import datetime

from django.test import TestCase

# Create your tests here.
from django.urls.base import reverse
from django.utils import timezone

from polls.models import Question


def create_questions(question_text, days):
    """
    Creates a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    :param question_text: Question Text
    :param days: Publish Date
    :return: Question
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no question exists a correct message should appear.
        :return: No polls are available
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with past pub_date should show in the Index View
        :return: Questions
        """
        create_questions(question_text="Past Question?", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['question_list'], ['<Question: Past Question?>'])


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        :return: False
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        :return: False
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_publish_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        :return: True
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
