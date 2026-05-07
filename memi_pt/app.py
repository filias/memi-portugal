"""Memi Portugal - pratica a tua memória sobre Portugal."""

from memi_engine import MemiConfig, create_app

# Import providers to register them
import memi_pt.providers  # noqa: F401

config = MemiConfig(
    title="memi portugal",
    subtitle="pratica a tua memória",
    favicon_color="#006600",
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
    done_html="""
        <svg width="200" height="180" viewBox="0 0 80 72" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <clipPath id="heart-clip">
                    <path d="M40 68 C40 68 4 44 4 22 C4 10 14 2 24 2 C30 2 36 6 40 12 C44 6 50 2 56 2 C66 2 76 10 76 22 C76 44 40 68 40 68Z"/>
                </clipPath>
            </defs>
            <g clip-path="url(#heart-clip)">
                <rect x="0" y="0" width="32" height="72" fill="#006600"/>
                <rect x="32" y="0" width="48" height="72" fill="#FF0000"/>
            </g>
            <path d="M40 68 C40 68 4 44 4 22 C4 10 14 2 24 2 C30 2 36 6 40 12 C44 6 50 2 56 2 C66 2 76 10 76 22 C76 44 40 68 40 68Z"
                  fill="none" stroke="var(--subtle, #888)" stroke-width="1.5"/>
        </svg>
    """,
)

import os
instance_static = os.path.join(os.path.dirname(__file__), "..", "static")
app = create_app(config, instance_static=instance_static)

if __name__ == "__main__":
    app.run(debug=True, port=8090)
