"""Portuguese category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_pt.categories.cidades import CITIES, WIKIPEDIA as CITY_WIKI, REGIONS as CITY_REGIONS
from memi_pt.categories.clubes import CLUBS, LOGOS as CLUB_LOGOS, TAGS as CLUB_TAGS
from memi_pt.categories.pinturas import PAINTINGS, COMMONS_FILES as PAINTING_FILES, TAGS as PAINTING_TAGS
from memi_pt.categories.rios import RIVERS, WIKIPEDIA as RIVER_WIKI, TAGS as RIVER_TAGS
from memi_pt.categories.distritos import DISTRICTS, MAP_FILES as DISTRICT_MAPS
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
from memi_pt.categories.pre_reino import (
    FIGURES as PRE_KINGDOM_ALL,
    WIKIPEDIA as PRE_KINGDOM_WIKI,
    TAGS as PRE_KINGDOM_TAGS,
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
        map_file = DISTRICT_MAPS.get(item)
        if map_file:
            result = images.get_wikipedia_file_image(map_file)
            if result:
                return result
        return images.get_wikipedia_image(item)


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
    key = "pessoas:1143-1910"
    items = MONARCHY_ALL
    override_name = True

    def get_image(self, item):
        wiki = MONARCHY_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return MONARCHY_TAGS.get(item)


class RepublicProvider(CategoryProvider):
    key = "pessoas:1910-presente"
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


class PreKingdomProvider(CategoryProvider):
    key = "pessoas:antes de 1143"
    items = PRE_KINGDOM_ALL
    override_name = True

    def get_image(self, item):
        wiki = PRE_KINGDOM_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return PRE_KINGDOM_TAGS.get(item)


class RiversProvider(CategoryProvider):
    key = "geografia:rios"
    items = RIVERS
    override_name = True

    def get_image(self, item):
        wiki = RIVER_WIKI.get(item, item)
        result = images.get_river_map(wiki)
        if not result or not result.get("image"):
            result = images.get_wikipedia_image(wiki)
        return result

    def get_tag(self, item):
        return RIVER_TAGS.get(item)


class ClubsProvider(CategoryProvider):
    key = "cultura:clubes"
    items = CLUBS
    override_name = True
    light_bg = True

    def get_image(self, item):
        logo = CLUB_LOGOS.get(item)
        if logo:
            return {"name": item, "image": logo}
        return images.get_wikipedia_image(item)

    def get_tag(self, item):
        return CLUB_TAGS.get(item)


class PaintingsProvider(CategoryProvider):
    key = "cultura:pinturas"
    items = PAINTINGS
    override_name = True

    def get_image(self, item):
        filename = PAINTING_FILES.get(item)
        if filename:
            return images.get_commons_file_image(filename)
        return None

    def get_tag(self, item):
        return PAINTING_TAGS.get(item)


register(PreKingdomProvider())
register(MetroProvider())
register(DistrictsProvider())
register(CitiesProvider())
register(RiversProvider())
register(MonumentsProvider())
register(FoodProvider())
register(ClubsProvider())
register(PaintingsProvider())
register(MonarchyProvider())
register(RepublicProvider())
register(AnimalsProvider())
register(PlantsProvider())
