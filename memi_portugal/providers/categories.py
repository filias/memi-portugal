"""Portuguese category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_portugal.categories.distritos import DISTRICTS, MAP_FILES as DISTRICT_MAPS
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
from memi_portugal.categories.natureza import (
    ALL_ANIMALS,
    ALL_PLANTS,
    ANIMAL_WIKIPEDIA,
    PLANT_WIKIPEDIA,
    SCIENTIFIC_NAMES,
)


class DistrictsProvider(CategoryProvider):
    key = "distritos"
    items = DISTRICTS
    override_name = True

    def get_image(self, item):
        map_file = DISTRICT_MAPS.get(item)
        if map_file:
            result = images.get_wikipedia_file_image(map_file)
            if result:
                return result
        return images.get_wikipedia_image(item)


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


class AnimalsProvider(CategoryProvider):
    key = "natureza:animais"
    items = ALL_ANIMALS
    override_name = True

    def get_image(self, item):
        wiki = ANIMAL_WIKIPEDIA.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return SCIENTIFIC_NAMES.get(item)


class PlantsProvider(CategoryProvider):
    key = "natureza:plantas"
    items = ALL_PLANTS
    override_name = True

    def get_image(self, item):
        wiki = PLANT_WIKIPEDIA.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return SCIENTIFIC_NAMES.get(item)


register(DistrictsProvider())
register(MonumentsProvider())
register(FoodProvider())
register(MonarchyProvider())
register(RepublicProvider())
register(AnimalsProvider())
register(PlantsProvider())
