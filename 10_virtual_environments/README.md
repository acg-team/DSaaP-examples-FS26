# Virtual Environments Example (DSaaP FS26)

This project demonstrates Python dependency management and reproducible execution across:

- a local `venv`;
- a `mamba` environment;
- a Docker container;
- a VS Code devcontainer.

The main script is [src/analysis.py](src/analysis.py). It:

- prints a text argument;
- runs a NumPy-based matrix operation;
- tries to run `blastn -version`.

## Requirements

- Python 3.10+;
- `pip`;
- `mamba` (or `micromamba`);
- Docker;
- optional: VS Code Dev Containers extension.

## Project Setup With Python `venv`

```bash
# from this folder
python3 -m venv demo-env
source demo-env/bin/activate

# install runtime dependencies
pip install '.'

# optional: install package + dev/test extras
pip install -e '.[dev,test]'
```

Run the script:

```bash
python src/analysis.py --text "Hello from venv"
```

Expected behavior:

- NumPy step runs;
- `blastn` may fail on host systems that do not have BLAST installed.

## Setup With `mamba`

Use the environment file:

```bash
mamba env create -f mamba_env.yml
mamba activate demo_mamba_env
python src/analysis.py --text "Hello from mamba"
```

If you prefer to install from scratch with mamba:

```bash
mamba create -n demo_mamba_env python=3.10 pip numpy=2.2.6 -c conda-forge
mamba activate demo_mamba_env
```

## Run With Docker

The Docker image is defined in [Dockerfile](Dockerfile). It installs:

- Python 3.10
- this package (`pip install .`)
- `ncbi-blast+` (so `blastn` is available)

Build and run:

```bash
docker build -t dsapp-venv-demo .
docker run --rm dsapp-venv-demo --text "Hello from Docker"
```

Because BLAST is installed in the image, the `blastn -version` call should succeed inside the container.

## Use The VS Code Devcontainer

The devcontainer config is in [.devcontainer/devcontainer.json](.devcontainer/devcontainer.json) and builds from the project [Dockerfile](Dockerfile).

1. Open this folder in VS Code.
2. Run: `Dev Containers: Reopen in Container`.
3. Wait for `postCreateCommand` to finish (`pip install --no-cache-dir '.[dev,test]'`).
4. Run in the VS Code terminal:

```bash
python src/analysis.py --text "Hello from devcontainer"
```

The devcontainer also installs recommended Python extensions and formatter settings.

## Authors

Jūlija Pečerska, Applied Computational Genomics Team.

Developing Software as a Product (DSaaP), Spring semester 2026 (FS26).

## License

Licensed under the MIT License. See [LICENSE](LICENSE).