from discord import Embed
from pydantic import BaseModel
from bot.constants import IGNORE_FIELDS


def add_fields(embed: Embed, model: BaseModel):
    for key, val in model.model_dump().items():
        if key not in IGNORE_FIELDS and val is not None:
            embed.add_field(name=key, value=str(val))
