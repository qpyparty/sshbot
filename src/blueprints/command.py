from asyncssh import connect
from telefone.bot import (
    BotBlueprint, Message
)
from telefone.bot.rules import (
    VBML
)
from telefone.tools.text import markdown as md, ParseMode


bp = BotBlueprint("command")
bp.labeler.vbml_ignore_case = True


@bp.labeler.message(VBML("/ <code>"), blocking=False)
async def execute(m: Message, code: str) -> str:
    async with connect(
        host="127.0.0.1", port=8000
    ) as conn:
        result = await conn.run(code)
    await m.answer(
        md.bold("Code") +
        md.code_block_with_lang(code, "bash") +
        md.bold("STDOUT") +
        md.code_block(result.stdout) +
        md.bold("STDERR") +
        md.code_block(result.stderr),
        parse_mode=ParseMode.MARKDOWN
    )
