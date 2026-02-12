from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇨🇿🇸🇰🇭🇺🇵🇱 V4 Resilience Bot\n\n"
        "Příkazy:\n"
        "/fest - šablona festivalu\n" 
        "/trh - lokální inzerát\n"
        "/manifesto - PDF manifest\n"
        "/mapa - tvůj region"
    )

async def fest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🗓️ RESILIENCE FEST | 1. MÁJ 2026

10:00 Sousedský trh (jídlo, služby, půda)
12:00 Regionální gril  
14:00 Debata: Půda vs hypotéka
16:00 Slavnost + networking

Stáhni šablonu: github.com/TVUJ_REPO/fest-template.md
#v4resilience_[tvuj_region]
    """
    await update.message.reply_text(text)

async def trh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📢 LOKÁLNÍ TRH\n\n"
        "Příklad inzerátu:\n"
        "Prodám 2ha louky v [vesnici] – 500k Kč\n"
        "Nabízím truhlářství – 800 Kč/hod\n\n"
        "Sdílej do místní FB skupiny!"
    )

def main():
    # Nahraď TVŮJ_TOKEN z t.me/BotFather
    app = Application.builder().token("TVŮJ_BOT_TOKEN").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("fest", fest))
    app.add_handler(CommandHandler("trh", trh))
    app.run_polling()

if __name__ == '__main__':
    main()
