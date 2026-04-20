# memi portugal

A Portuguese memory card game built on [memi-engine](https://github.com/filias/memi-engine).

Live at [pt.memi.click](https://pt.memi.click)

## Categories

- **Distritos** — 20 Portuguese districts and autonomous regions
- **Monumentos** — 63 landmarks and monuments across Portugal
- **Comida** — 20 traditional Portuguese dishes
- **Pessoas: Monarquia** — 101 figures from the monarchy era (kings, queens, explorers, writers)
- **Pessoas: República** — 64 figures from the republic (presidents, artists, athletes)
- **Natureza: Animais** — 49 native Portuguese animals
- **Natureza: Plantas** — 29 native Portuguese plants and trees

## Setup

```bash
uv sync
uv run python -m memi_portugal.app
```

## How it works

Each category is a `CategoryProvider` subclass that tells the engine what items to show and where to fetch images. Adding a new category is just a Python class with a list of items and a `get_image` method.

Built with [memi-engine](https://github.com/filias/memi-engine) — anyone can create their own country version.

## License

MIT
