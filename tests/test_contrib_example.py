"""The worked example of a contribution (docs/example-contribution/) stays valid, and the
README's list of MCP tools stays in step with the server."""
import importlib.util
import os
import sys
import unittest

import jsonschema

LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EX = os.path.join(LAB, "docs", "example-contribution")


class ContribExample(unittest.TestCase):
    def test_front_matter_and_pinned_premises(self):
        from tp.model import parse_entity_text
        from tp.schema import ENTITY
        meta, _, errs = parse_entity_text(open(os.path.join(EX, "entity.md"), encoding="utf-8").read())
        self.assertEqual(errs, [])
        jsonschema.validate(meta, ENTITY)
        self.assertEqual(meta["ai_involved"], "yes")
        for pin in meta["derivations"][0]["uses"]:
            pid, ver = pin.split("@")
            path = os.path.join(LAB, "store", "claims", pid, "entity.md")
            self.assertTrue(os.path.exists(path), pid)
            pmeta, _, _ = parse_entity_text(open(path, encoding="utf-8").read())
            self.assertEqual(str(pmeta["version"]), ver, f"{pid} is pinned at {ver}")

    def test_its_check_passes(self):
        sys.path.insert(0, os.path.join(LAB, "lib"))
        try:
            import tp_premise
            tp_premise.configure(os.path.join(LAB, "store"))
            spec = importlib.util.spec_from_file_location("example_check", os.path.join(EX, "check.py"))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            self.assertTrue(mod.check_null_vectors_square_to_zero())
        finally:
            sys.path.remove(os.path.join(LAB, "lib"))

    def test_readme_lists_every_tool(self):
        from tp.mcp_server import tool_list
        readme = open(os.path.join(LAB, "README.md"), encoding="utf-8").read()
        section = readme.split("## The MCP server", 1)[1].split("\n## ", 1)[0]
        missing = [t["name"] for t in tool_list() if t["name"] not in section]
        self.assertEqual(missing, [], "add these tools to the README's MCP section")


if __name__ == "__main__":
    unittest.main()
