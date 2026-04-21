"""Memi Portugal - pratica a tua memória sobre Portugal."""

from memi_engine import MemiConfig, create_app

# Import providers to register them
import memi_pt.providers  # noqa: F401

config = MemiConfig(
    title="memi portugal",
    subtitle="pratica a tua memória",
    themes=["light", "green", "blue", "dark"],
    default_theme="light",
    sponsor_url="https://github.com/sponsors/filias",
    sponsor_text="apoiar",
    about_html="""
        <p>Memi Portugal é um jogo de memória sobre Portugal.</p>
        <p>Escolhe uma categoria, olha para a imagem e tenta adivinhar
        o que é antes de revelar a resposta.</p>
        <p>Distritos, monumentos, comida, pessoas famosas — há sempre
        algo novo para aprender.</p>
    """,
    # Portuguese labels
    label_theme="tema",
    label_about="sobre",
    label_report="reportar",
    label_reported="reportado",
    label_clues_on="pistas: sim",
    label_clues_off="pistas: não",
    label_show_letter="mostrar letra",
    label_pick_category="escolhe uma categoria",
    label_loading="a carregar...",
    label_all_done="tudo feito! clica para recomeçar",
    label_click_to_reveal="clica na imagem para revelar a resposta",
    label_click_for_new="clica novamente para outra",
    label_back="voltar a jogar",
)

app = create_app(config)

if __name__ == "__main__":
    app.run(debug=True, port=8090)
