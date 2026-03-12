import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, CONF_GEMINI_API_KEY

class WineLegacyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gère le flux de configuration pour Wine Legacy."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Première étape de configuration via l'interface."""
        errors = {}

        if user_input is not None:
            # Ici, on pourrait ajouter une validation de la clé API
            return self.async_create_entry(
                title=user_input["cave_name"], 
                data=user_input
            )

        # Formulaire affiché à l'utilisateur
        data_schema = vol.Schema({
            vol.Required("cave_name", default="Ma Cave"): str,
            vol.Required(CONF_GEMINI_API_KEY): str,
        })

        return self.async_show_form(
            step_id="user", 
            data_schema=data_schema, 
            errors=errors
        )
