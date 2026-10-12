#!/usr/bin/env python3

import json
import subprocess
from pathlib import Path


def run(command: list[str]) -> None:
    print("+", " ".join(command), flush=True)
    subprocess.run(command, check=True)


def main() -> None:
    root = Path(
        subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            text=True,
        ).strip()
    )

    print(f"Preparing {root}", flush=True)

    # Composer
    if (root / "composer.lock").exists():
        run([
            "composer",
            "install",
            "--no-interaction",
            "--prefer-dist",
            "--no-progress",
        ])

    # npm
    package_json = root / "package.json"
    package_lock = root / "package-lock.json"

    if package_lock.exists():
        run([
            "npm",
            "ci",
            "--no-audit",
            "--no-fund",
        ])

    # Laravel + Vite
    if (
        (root / "artisan").exists()
        and package_json.exists()
        and any(root.glob("vite.config.*"))
    ):
        package = json.loads(package_json.read_text())
        scripts = package.get("scripts", {})

        if "build" in scripts:
            if not package_lock.exists():
                raise RuntimeError(
                    "Laravel/Vite project has no package-lock.json; "
                    "refusing to perform a non-deterministic npm install"
                )

            run(["npm", "run", "build"])

    print("Repository preparation complete.", flush=True)


if __name__ == "__main__":
    main()