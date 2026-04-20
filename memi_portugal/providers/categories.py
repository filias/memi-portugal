"""Portuguese category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_portugal.categories.distritos import DISTRITOS
from memi_portugal.categories.monumentos import (
    MONUMENTOS,
    LOCALIZACOES,
    WIKIPEDIA as MONUMENT_WIKI,
)
from memi_portugal.categories.comida import COMIDA
from memi_portugal.categories.monarquia import (
    ALL as MONARQUIA_ALL,
    WIKIPEDIA as MONARQUIA_WIKI,
    TAGS as MONARQUIA_TAGS,
)
from memi_portugal.categories.republica import (
    ALL as REPUBLICA_ALL,
    WIKIPEDIA as REPUBLICA_WIKI,
    TAGS as REPUBLICA_TAGS,
)


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


class MonarquiaProvider(CategoryProvider):
    key = "pessoas:monarquia"
    items = MONARQUIA_ALL
    override_name = True

    def get_image(self, item):
        wiki = MONARQUIA_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return MONARQUIA_TAGS.get(item)


class RepublicaProvider(CategoryProvider):
    key = "pessoas:república"
    items = REPUBLICA_ALL
    override_name = True

    def get_image(self, item):
        wiki = REPUBLICA_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return REPUBLICA_TAGS.get(item)


register(DistritosProvider())
register(MonumentosProvider())
register(ComidaProvider())
register(MonarquiaProvider())
register(RepublicaProvider())
