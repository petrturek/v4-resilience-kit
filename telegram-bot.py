import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Railway env variable (nastavíš v Railway dashboardu)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8003982397:AAH2d-A5ArpXUGYnISbdrx16d7LlFaPg_6s")

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start příkaz"""
    await update.message.reply_text(
        "🇨🇿🇸🇰🇭🇺🇵🇱 <b>V4 Resilience Bot</b>\n\n"
        "Příkazy:\n"
        "• <b>/fest</b> - šablona festivalu\n"
        "• <b>/trh</b> - lokální trh\n"
        "• <b>/manifesto</b> - regionální manifest\n"
        "• <b>/mapa</b> - tvůj region\n\n"
        "<i>github.com/petrturek/v4-resilience-kit</i>",
        parse_mode='HTML'
    )

async def fest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Resilience Fest šablona"""
    await update.message.reply_text(
        "🗓️ <b>RESILIENCE FEST | 1. MÁJ 2026</b>\n\n"
        "📍 <b>PROGRAM (10:00–16:00)</b>\n"
        "• 10:00 <b>Sousedský trh</b> (jídlo, služby, půda)\n"
        "• 12:00 <b>Regionální gril</b>\n"
        "• 14:00 <b>Debata:</b> Půda vs hypotéka\n"
        "• 16:00 <b>Slavnost</b> + networking\n\n"
        "📋 <b>Stáhni šablonu:</b>\n"
        "github.com/petrturek/v4-resilience-kit/blob/main/fest-template.md\n\n"
        "<b>#v4resilience_[tvůj_region]</b>",
        parse_mode='HTML'
    )

async def trh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Lokální trh"""
    await update.message.reply_text(
        "📢 <b>LOKÁLNÍ TRH – příklady inzerátů</b>\n\n"
        "🌾 <b>Prodám:</b>\n"
        "• 2ha louky Třinec – 500k Kč\n"
        "• Staré auto bez STK – 30k Kč\n\n"
        "🔨 <b>Nabízím:</b>\n"
        "• Truhlářství – 800 Kč/hod\n"
        "• Úklid zahrady – 300 Kč/h\n\n"
        "<i>Sdílej do místní FB skupiny!</i>",
        parse_mode='HTML'
    )

async def manifesto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Regionální manifest"""
    await update.message.reply_text(
        "📜 <b>MANIFEST REGIONÁLNÍ AUTONOMIE</b>\n\n"
        "My, obyvatelé [Haná/Slezsko/Orava/…] žádáme:\n\n"
        "✅ <b>Vlastní daně</b> pro místní projekty\n"
        "✅ <b>Referenda</b> o velkých rozhodnutích\n"
        "✅ <b>Lokální měnu</b> pro sousedský obchod\n"
        "✅ <b>Přírodní hranice</b> našeho regionu\n\n"
        "<i>Podepiš na Resilience Fest 1.5.2026</i>",
        parse_mode='HTML'
    )

async def mapa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Regionální mapy"""
    await update.message.reply_text(
        "🗺️ <b>VYTVOŘ MAPU TVÉHO REGIONU</b>\n\n"
        "1️⃣ umap.openstreetmap.fr\n"
        "2️⃣ Importuj z repa: umap-hana.json\n"
        "3️⃣ Nakresli <b>přírodní hranice</b>\n"
        "4️⃣ Export PDF pro fest\n\n"
        "<i>Příklad Haná: github.com/petrturek/v4-resilience-kit</i>",
        parse_mode='HTML'
    )

def main():
    """Spustí bot"""
    app = Application.builder().token(TOKEN).build()
    
    # Handlery
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("fest", fest))
    app.add_handler(CommandHandler("trh", trh))
    app.add_handler(CommandHandler("manifesto", manifesto))
    app.add_handler(CommandHandler("mapa", mapa))
    
    logger.info("V4 Resilience Bot startuje...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
