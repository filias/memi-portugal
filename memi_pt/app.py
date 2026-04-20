"""Memi Portugal - pratica a tua memória sobre Portugal."""

from memi_engine import MemiConfig, create_app

# Import providers to register them
import memi_pt.providers  # noqa: F401

config = MemiConfig(
    title="memi portugal",
    subtitle="pratica a tua memória",
    themes=["light", "green", "blue", "dark"],
    default_theme="light",
    about_html="""
        <p>Memi Portugal é um jogo de memória sobre Portugal.</p>
        <p>Escolhe uma categoria, olha para a imagem e tenta adivinhar
        o que é antes de revelar a resposta.</p>
        <p>Distritos, monumentos, comida, pessoas famosas — há sempre
        algo novo para aprender.</p>
    """,
)

app = create_app(config)

if __name__ == "__main__":
    app.run(debug=True, port=8090)
