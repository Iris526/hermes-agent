from pathlib import Path

from hermes_cli.default_soul import DEFAULT_SOUL_MD


def test_docker_seeded_soul_matches_runtime_default_persona():
    repo_root = Path(__file__).parents[2]
    docker_soul = (repo_root / "docker" / "SOUL.md").read_text(encoding="utf-8")

    assert docker_soul.strip() == DEFAULT_SOUL_MD.strip()
