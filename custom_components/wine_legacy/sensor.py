from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    """Configuration des capteurs à partir d'une entrée de configuration."""
    # Pour l'instant, on crée un capteur d'exemple. 
    # Plus tard, ce code lira une base de données ou un fichier JSON.
    async_add_entities([
        WineLibrarySummarySensor(entry.title),
        WineBottleSensor("Bouteille Test", "Château Margaux", "Rouge", 2015, 600, 850, "A1")
    ])

class WineLibrarySummarySensor(SensorEntity):
    """Capteur global pour la cave."""
    def __init__(self, cave_name):
        self._attr_name = f"{cave_name} Stats"
        self._attr_unique_id = f"{cave_name}_stats"
        self._attr_native_value = 1 # Nombre de bouteilles
        self._attr_icon = "mdi:format-list-bulleted-type"

    @property
    def extra_state_attributes(self):
        return {
            "Total Valeur": "850€",
            "Dernière mise à jour": "Via Gemini AI"
        }

class WineBottleSensor(SensorEntity):
    """Représentation d'une bouteille individuelle."""
    def __init__(self, name, castle, color, year, buy_price, current_value, location):
        self._attr_name = name
        self._attr_unique_id = f"wine_{castle}_{year}"
        self._attr_native_value = "Présent"
        self._castle = castle
        self._color = color
        self._year = year
        self._buy_price = buy_price
        self._current_value = current_value
        self._location = location
        self._attr_icon = "mdi:bottle-wine"

    @property
    def extra_state_attributes(self):
        """Attributs détaillés pour l'affichage dans le dashboard."""
        return {
            "Château": self._castle,
            "Couleur": self._color,
            "Millésime": self._year,
            "Prix d'achat": f"{self._buy_price}€",
            "Valeur actuelle": f"{self._current_value}€",
            "Emplacement": self._location,
        }
