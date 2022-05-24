from telefone import Bot

from src.blueprints import bps
from src.config import BOT_TOKEN
from src.initialize import setup_db
from src.middlewares import mws


def init_bot() -> "Bot":
    """Инстанцирует класс `Bot`"""
    bot = Bot(token=BOT_TOKEN)
    setup_blueprints(bot)
    setup_middlewares(bot)
    return bot


def setup_blueprints(bot: Bot):
    """Загружает блюпринты из пакета `blueprints`"""
    for bp in bps:
        bp.load(bot)


def setup_middlewares(bot: Bot):
    """Загружает мидлвари из пакета `middlewares`"""
    for mw in mws:
        mw.load(bot)


bot = init_bot()
bot.loop_wrapper.on_startup.append(setup_db())
