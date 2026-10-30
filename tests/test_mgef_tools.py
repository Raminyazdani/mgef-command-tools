import sys
from pathlib import Path
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mgef_tools import commands, main, parse_effects, write_new


class CommandTests(unittest.TestCase):
    def test_records_are_validated_deduplicated_and_sorted(self):
        self.assertEqual(parse_effects(['comment', 'MGEF B (0000000b)', 'MGEF A (0000000A)', 'MGEF A (0000000a)']), ['0000000A', '0000000B'])

    def test_malformed_record_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_effects(['MGEF unsafe (not-a-form-id)'])

    def test_singles_and_pairs(self):
        self.assertEqual(list(commands(['00000001', '00000002'], '000139a3', True)), ['playerenchantobject 000139A3 00000001', 'playerenchantobject 000139A3 00000002', 'playerenchantobject 000139A3 00000001 00000002'])

    def test_large_combination_set_is_rejected_before_output(self):
        with self.assertRaises(ValueError):
            list(commands(['00000001', '00000002'], '000139A3', True, 2))

    def test_item_cannot_inject_commands(self):
        with self.assertRaises(ValueError):
            list(commands(['00000001'], '000139A3\nother-command'))

    def test_output_is_exclusive(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / 'commands.txt'
            p.write_text('preserved', encoding='utf-8')
            with self.assertRaises(FileExistsError):
                write_new(p, ['new'])
            self.assertEqual(p.read_text(encoding='utf-8'), 'preserved')

    def test_cli_uses_explicit_input_and_preserves_it(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / 'effects.txt'
            source = 'MGEF Example (00000001)\n'
            p.write_text(source, encoding='utf-8')
            out = Path(folder) / 'commands.txt'
            self.assertEqual(main([str(p), '--output', str(out)]), 0)
            self.assertEqual(p.read_text(encoding='utf-8'), source)
            self.assertEqual(out.read_text(encoding='utf-8'), 'playerenchantobject 000139A3 00000001\n')


if __name__ == '__main__':
    unittest.main()
