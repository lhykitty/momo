import subprocess
import sys
from pathlib import Path

import mini_momo


def test_mini_momo_module_and_public_exports():
    assert mini_momo.Momo is not None
    assert mini_momo.FakeModelClient is not None
    assert not hasattr(mini_momo, "MiniAgent")
    result = subprocess.run([sys.executable, "-m", "mini_momo", "--help"], capture_output=True, text=True, check=True)
    assert "Teaching-sized Momo agent harness" in result.stdout


def test_readme_main_mapping_points_to_existing_files():
    repo_root = Path(__file__).resolve().parents[3]
    main_files = [
        "momo/cli.py",
        "momo/runtime.py",
        "momo/agent_loop.py",
        "momo/context_manager.py",
        "momo/providers/clients.py",
        "momo/tool_executor.py",
        "momo/tools.py",
        "momo/task_state.py",
        "momo/run_store.py",
        "momo/workspace.py",
    ]
    for path in main_files:
        assert (repo_root / path).exists()
