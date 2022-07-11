from unittest import TestCase

from human_readable_json import MarkdownGenerator


class TestMarkdownGenerator(TestCase):
    def test_build_link(self):
        self.assertEqual(MarkdownGenerator.build_link(dir="core", mod="file_core"),
                         '[See core  file_core](core.md#file-core)')
