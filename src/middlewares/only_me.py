from telefone import BaseMiddleware, BotBlueprint, Message

from src.config import USER_ID


bp = BotBlueprint("only_me_mw")


@bp.labeler.message_view.register_middleware
class OnlyMe(BaseMiddleware[Message]):
    async def pre(self) -> None:
        if self.update.from_.id != USER_ID:
            self.stop()
