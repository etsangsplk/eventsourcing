import unittest

from eventsourcing.infrastructure.stored_event_repos.with_python_objects import PythonObjectsStoredEventRepository


class PythonObjectsRepoTestCase(unittest.TestCase):

    @property
    def stored_event_repo(self):
        try:
            return self._stored_event_repo
        except AttributeError:
            stored_event_repo = PythonObjectsStoredEventRepository(
                always_write_entity_version=True,
                always_check_expected_version=True,
            )
            self._stored_event_repo = stored_event_repo
            return stored_event_repo
