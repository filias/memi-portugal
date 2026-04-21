"""Portuguese category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_pt.categories.cidades import CITIES, WIKIPEDIA as CITY_WIKI, REGIONS as CITY_REGIONS
from memi_pt.categories.distritos import DISTRICTS
from memi_pt.categories.metro import STATIONS, COMMONS_FILES as METRO_FILES, LINES as METRO_LINES
from memi_pt.categories.monumentos import (
    MONUMENTS,
    LOCATIONS,
    WIKIPEDIA as MONUMENT_WIKI,
)
from memi_pt.categories.comida import FOOD
from memi_pt.categories.monarquia import (
    ALL as MONARCHY_ALL,
    WIKIPEDIA as MONARCHY_WIKI,
    TAGS as MONARCHY_TAGS,
)
from memi_pt.categories.republica import (
    ALL as REPUBLIC_ALL,
    WIKIPEDIA as REPUBLIC_WIKI,
    TAGS as REPUBLIC_TAGS,
)
from memi_pt.categories.natureza import (
    ALL_ANIMALS,
    ALL_PLANTS,
    ANIMAL_WIKIPEDIA,
    PLANT_WIKIPEDIA,
    SCIENTIFIC_NAMES,
)


class DistrictsProvider(CategoryProvider):
    key = "geografia:distritos"
    items = DISTRICTS
    override_name = True

    def get_image(self, item):
        # Show a photo of the district capital / main city
        wiki = item
        if item == "Açores":
            wiki = "Azores"
        elif item == "Madeira":
            wiki = "Madeira"
        result = images.get_wikipedia_image(wiki)
        if not result or not result.get("image"):
            result = images.get_wikipedia_image(f"{item} (city)")
        return result


class MonumentsProvider(CategoryProvider):
    key = "cultura:monumentos"
    items = MONUMENTS
    override_name = True

    def get_image(self, item):
        wiki = MONUMENT_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return LOCATIONS.get(item)


class FoodProvider(CategoryProvider):
    key = "cultura:comida"
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


class MetroProvider(CategoryProvider):
    key = "cultura:metro de lisboa"
    items = STATIONS
    override_name = True

    def get_image(self, item):
        filename = METRO_FILES.get(item)
        if filename:
            return images.get_commons_file_image(filename)
        return None

    def get_tag(self, item):
        line = METRO_LINES.get(item)
        return f"Linha {line}" if line else None


class CitiesProvider(CategoryProvider):
    key = "geografia:cidades"
    items = CITIES
    override_name = True

    def get_image(self, item):
        wiki = CITY_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return CITY_REGIONS.get(item)


register(MetroProvider())
register(DistrictsProvider())
register(CitiesProvider())
register(MonumentsProvider())
register(FoodProvider())
register(MonarchyProvider())
register(RepublicProvider())
register(AnimalsProvider())
register(PlantsProvider())
