import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def run_alembic_upgrade_head():
    subprocess.run(["alembic", "downgrade", "base"], cwd=Path(__file__).parent.parent)
    subprocess.run(["alembic", "upgrade", "head"], cwd=Path(__file__).parent.parent)
