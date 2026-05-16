"""Memi Portugal - pratica a tua memória sobre Portugal."""

from memi_engine import MemiConfig, create_app

# Import providers to register them
import memi_pt.providers  # noqa: F401

config = MemiConfig(
    title="memi portugal",
    subtitle="pratica a tua memória",
    favicon_color="#006600",
    sponsor_url="https://github.com/sponsors/filias",
    sponsor_text="apoiar",
    related_sites=[
        {"name": "memi", "url": "https://memi.click"},
        {"name": "memi lisboa", "url": "https://lx.memi.click"},
        {"name": "memi slovensko", "url": "https://sk.memi.click"},
        {"name": "memi US", "url": "https://us.memi.click"},
    ],
    label_related_sites="outros jogos memi",
    about_html="""
        <p>Memi Portugal é um jogo de memória sobre Portugal. Distritos,
        monumentos, comida, pessoas famosas &mdash; há sempre algo novo
        para aprender.</p>

        <h2>Como jogar</h2>
        <p>Escolhe uma categoria, olha para a imagem e tenta adivinhar
        o que é antes de revelar a resposta. Sem contas, sem pontuação,
        sem limite de tempo.</p>
        <p>Na barra inferior tens alguns auxiliares:</p>
        <ul>
            <li><strong>pistas:</strong> ativa pistas progressivas de
            letras &mdash; revela a primeira letra, depois a seguinte, e
            assim por diante. Útil quando o nome está na ponta da
            língua.</li>
            <li><strong>saber mais:</strong> aparece ao revelar e abre o
            artigo da Wikipédia (ou a página da fonte) do item, para que
            possas ler mais.</li>
            <li><strong>reportar:</strong> marca uma carta se a imagem não
            corresponder à resposta (imagem errada, miniatura partida,
            etc.).</li>
        </ul>
        <p>Podes jogar de duas formas:</p>
        <ul>
            <li><strong>Para aprender:</strong> quando não reconheces um
            item, revela a resposta e segue o link <em>saber mais</em>
            para ler sobre ele. Cada exposição reforça a associação entre
            a imagem e o nome.</li>
            <li><strong>Para te testares:</strong> quando uma categoria já
            te é familiar, percorre-a e vê quantas consegues nomear sem
            revelar.</li>
        </ul>

        <h2>Porque funciona</h2>
        <p>Esta é uma forma simples de <em>recordação ativa</em> &mdash;
        recuperar informação da memória em vez de a reler. O <em>efeito
        de teste</em>, bem documentado em psicologia cognitiva, mostra
        que a prática de recuperação cria memórias mais duradouras do que
        a simples re-exposição.</p>
        <p>Como cada estímulo é uma imagem, o jogo aproveita também o
        <em>efeito de superioridade da imagem</em>: as imagens são
        codificadas de forma mais rica do que as palavras e mais fáceis
        de recuperar depois. Nomear o item é uma forma de
        <em>recordação com pista</em>, situada entre o reconhecimento
        simples (&ldquo;já vi isto antes?&rdquo;) e a
        <em>recordação livre</em> sem ajuda.</p>
        <p>Sessões curtas e frequentes funcionam melhor do que sessões
        longas &mdash; o <em>efeito de espaçamento</em>. Alguns minutos
        por dia chegam.</p>
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
    label_more="saber mais",
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
