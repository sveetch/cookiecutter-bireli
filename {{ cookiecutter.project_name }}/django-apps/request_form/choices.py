"""
Choices for model fields and their getters.

* ``get_***_choices()`` is to list available choices;
* ``get_***_default()`` is to get default choice, this is the first item from available
  choices;

You can not add, edit or remove entries just like that or it may result to data loss.

Migration that include fields that use these choices will need to be rewritten to use
these getters instead of Django hardcoded choice list and default.
"""
from django.conf import settings


def get_subject_choices():
    """
    Return choices built from related setting.

    We are defining an empty choice as the first item, you may need to change
    ``get_subject_default`` if you are removing this empty choice and possible other
    usage of choices in further code like the form.
    """
    return tuple([("", "-----")] + [
        (k, v.get("label") or k)
        for k, v in settings.REQUEST_SUBJECTS.items()
    ])


def get_subject_default():
    """
    Return the default value from the first non empty choice.
    """
    choices = get_subject_choices()
    return "" if len(choices) < 2 else choices[1][0]
