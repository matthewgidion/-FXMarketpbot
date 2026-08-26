import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# Enable logging to see what's happening
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Import sensitive data from config
import config

# --- Command Handlers ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when /start is issued."""
    welcome_text = (
        "👋 *Welcome to the Forex Insights Bot!*\n\n"
        "I provide market analysis, price alerts, and educational resources.\n"
        "Use /help to see what I can do.\n"
        "🔐 *Note:* This bot is for educational purposes only. Not financial advice."
    )
    keyboard = [[InlineKeyboardButton("📊 View Demo Analysis", callback_data='demo')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, parse_mode='Markdown', reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message when /help is issued."""
    help_text = (
        "Here are the commands I understand:\n\n"
        "/start - Start the bot\n"
        "/help - Show this message\n"
        "/analysis - Get a sample market analysis\n"
        "/alert - Set up a price alert (coming soon)\n"
        "/education - Get a trading term of the day\n"
    )
    await update.message.reply_text(help_text)

async def analysis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """A placeholder for real market analysis."""
    analysis_text = (
        "*Sample Market Analysis (EUR/USD)*\n"
        "• Trend: Bullish on daily timeframe\n"
        "• Key Resistance: 1.1200\n"
        "• Key Support: 1.1000\n"
        "• RSI: 65 (Neutral)\n\n"
        "*⚠️ Disclaimer:* This is a simulated analysis for demonstration only."
    )
    await update.message.reply_text(analysis_text, parse_mode='Markdown')

async def education(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random educational fact."""
    fact = "*📚 Trading Term: Pip*\n\nA pip is the smallest price move that a given exchange rate can make. For most major currency pairs, it is 0.0001."
    await update.message.reply_text(fact, parse_mode='Markdown')

async def demo_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the button press from the welcome message."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="You requested a demo! 🚀\n\nHere is a sample market insight... (Feature coming soon)")

# --- Main Bot Runner ---

if __name__ == '__main__':
    # 1. Create the Application
    application = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()

    # 2. Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("analysis", analysis))
    application.add_handler(CommandHandler("education", education))
    application.add_handler(CallbackQueryHandler(demo_button, pattern='demo'))

    # 3. Start the bot
    print("Bot is starting...")
    application.run_polling()
