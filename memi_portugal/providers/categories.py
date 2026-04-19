"""Portuguese category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_portugal.categories.distritos import DISTRITOS
from memi_portugal.categories.monumentos import MONUMENTOS, LOCALIZACOES, WIKIPEDIA as MONUMENT_WIKI
from memi_portugal.categories.comida import COMIDA
from memi_portugal.categories.pessoas import PESSOAS


class DistritosProvider(CategoryProvider):
    key = "distritos"
    items = DISTRITOS

    def get_image(self, item):
        result = images.get_wikipedia_image(f"{item} District")
        if not result or not result.get("image"):
            result = images.get_wikipedia_image(item)
        return result


class MonumentosProvider(CategoryProvider):
    key = "monumentos"
    items = MONUMENTOS
    override_name = True

    def get_image(self, item):
        wiki = MONUMENT_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return LOCALIZACOES.get(item)


class ComidaProvider(CategoryProvider):
    key = "comida"
    items = COMIDA

    def get_image(self, item):
        result = images.get_wikipedia_image(item)
        if not result or not result.get("image"):
            result = images.get_wikipedia_image(item + " (food)")
        return result


class PessoasProvider(CategoryProvider):
    key = "pessoas"
    items = PESSOAS

    def get_tag(self, item):
        return images.get_wikipedia_description(item) or None


register(DistritosProvider())
register(MonumentosProvider())
register(ComidaProvider())
register(PessoasProvider())
