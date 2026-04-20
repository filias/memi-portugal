"""Portuguese category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_portugal.categories.distritos import DISTRICTS
from memi_portugal.categories.monumentos import (
    MONUMENTS,
    LOCATIONS,
    WIKIPEDIA as MONUMENT_WIKI,
)
from memi_portugal.categories.comida import FOOD
from memi_portugal.categories.monarquia import (
    ALL as MONARCHY_ALL,
    WIKIPEDIA as MONARCHY_WIKI,
    TAGS as MONARCHY_TAGS,
)
from memi_portugal.categories.republica import (
    ALL as REPUBLIC_ALL,
    WIKIPEDIA as REPUBLIC_WIKI,
    TAGS as REPUBLIC_TAGS,
)


class DistrictsProvider(CategoryProvider):
    key = "distritos"
    items = DISTRICTS
    override_name = True

    def get_image(self, item):
        result = images.get_wikipedia_image(f"{item} District")
        if not result or not result.get("image"):
            result = images.get_wikipedia_image(item)
        return result


class MonumentsProvider(CategoryProvider):
    key = "monumentos"
    items = MONUMENTS
    override_name = True

    def get_image(self, item):
        wiki = MONUMENT_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return LOCATIONS.get(item)


class FoodProvider(CategoryProvider):
    key = "comida"
    items = FOOD

    def get_image(self, item):
        result = images.get_wikipedia_image(item)
        if not result or not result.get("image"):
            result = images.get_wikipedia_image(item + " (food)")
        return result


class MonarchyProvider(CategoryProvider):
    key = "pessoas:monarquia"
    items = MONARCHY_ALL
    override_name = True

    def get_image(self, item):
        wiki = MONARCHY_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return MONARCHY_TAGS.get(item)


class RepublicProvider(CategoryProvider):
    key = "pessoas:república"
    items = REPUBLIC_ALL
    override_name = True

    def get_image(self, item):
        wiki = REPUBLIC_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return REPUBLIC_TAGS.get(item)


register(DistrictsProvider())
register(MonumentsProvider())
register(FoodProvider())
register(MonarchyProvider())
register(RepublicProvider())
