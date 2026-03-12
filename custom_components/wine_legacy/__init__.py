from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configuration de Wine Legacy."""
    hass.data.setdefault(DOMAIN, {})
    
    # Cette ligne est cruciale : elle lance le fichier sensor.py
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Déchargement de l'intégration."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])

