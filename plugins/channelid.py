from pyrogram import filters
from pyrogram import Client, enums
from pyrogram.file_id import FileId
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    if msg.forward_from:
        text = "<u>ššØš«š°šš«š šš§ššØš«š¦šš­š¢šØš§ š</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>š¤ ššØš­ šš§ššØ</u>"
        else:
            text += "<u>š¤šš¬šš« šš§ššØ</u>"
        text += f'\n\nšØāš¼ ššš¦š : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:

            text += f'\n\nš šš¬šš«ššš¦š : @{msg.forward_from["username"]} \n\nš ID : <code>{msg.forward_from["id"]}</code>\n\nš«DC : {msg.forward_from["dc_id"]}'           
        else:
            text += f'\n\nš šš : `{msg.forward_from["id"]}`\n\n\n\nš«DC : {msg.forward_from["dc_id"]}'

        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"āļøšš«š«šØš« <b><i>{hidden}</i></b> āļøšš«š«šØš«",
                quote=True,
            )
        else:
            text = f"<u>ššØš«š°šš«š šš§ššØš«š¦šš­š¢šØš§ š</u>.\n\n"
            if msg.forward_from_chat["type"] == enums.ChatType.CHANNEL:
                text += "<u>š¢ šš”šš§š§šš„</u>"
            if msg.forward_from_chat["type"] == enums.ChatType.GROUP:
                text += "<u>š£ļø šš«šØš®š©</u>"
            text += f'\n\nš ššš¦š {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:

                text += f'\n\nā”ļø šš«šØš¦ : @{msg.forward_from_chat["username"]}'
                text += f'\n\nš šš : `{msg.forward_from_chat["id"]}`\n\nš«DC : {msg.forward_from_chat["dc_id"]}'
            else:
                text += f'\n\nš šš `{msg.forward_from_chat["id"]}`\n\n{msg.forward_from_chat["dc_id"]}'                                           

            await msg.reply(text, quote=True)









