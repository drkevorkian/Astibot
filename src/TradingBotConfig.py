import argparse
from argparse import RawTextHelpFormatter
import textwrap
parser = argparse.ArgumentParser(description='AstiBot command line Arguements:', formatter_class=RawTextHelpFormatter)
parser.add_argument('--debug', dest='debug', type=str, help='Enable or Disable Debug console.\n', default=False)
parser.add_argument('--fiat', dest='fiat', type=str, help='Fiat choice, USD/EUR/GBP.\n', default="USD")
parser.add_argument('--cvsmarket', dest='cvsMar', type=str, help='False: CSV file input. True: Real-time market price.\n', default=False)
parser.add_argument('--mtick', dest='mTick', type=int, help='Main ticker : Retrieves the next samples and processes them.\n', default=250)
parser.add_argument('--retsamptimems', dest='retSampTimems', type=int, help='Terrestrial time between two retrieved samples.\n Should be equal to mtick in live mode, custom value in simulation mode depends on the csv file sampling time.\n', default=10000)
parser.add_argument('--maxbuy', dest='maxBuyPrice', type=int, help='Maximum amount to spend on any single Coin.\n', default=100000)
parser.add_argument('--uigraphupdate', dest='uiGraphUpdate', type=int, help='UI Graph refresh per call to the main ticker.\n', default=1)
parser.add_argument('--cvssave', dest='cvsSave', type=str, help='True to record price in output csv file. For the live mode only.\n', default=False)
parser.add_argument('--realtrans', dest='realTrans', type=str, help='True to enable real buy and sell transaction to the market.\n', default=True)

parser.add_argument('--preloadhours', dest='preLoadHours', type=int, help='Number of hours of historical samples to retrieve.\n', default=10)
parser.add_argument('--simmaxbal', dest='simMaxBal', type=int, help='Maximum fiat balance in simulation mode.\n', default=5000)
parser.add_argument('--riskperabovemaxthreshbuy', dest='riskPerAboveMaxThreshBuy', type=int, help='RiskLine MAX Threshold Buy.\n', default=0.95)
parser.add_argument('--riskperaboveminthreshbuy', dest='riskPerAboveMinThreshBuy', type=int, help='RiskLine MIN Threshold Buy.\n', default=1.05)
parser.add_argument('--riskperabovegenthreshbuy', dest='riskPerAboveGenThreshBuy', type=int, help='RiskLine General Threshold Buy.\n', default=0.994)
parser.add_argument('--buypolicyone', dest='buyPolicyOne', type=int, help=textwrap.dedent("\nBuy policy: \n" 
     " When MACD indicator is < BUY1 THRESHOLD : No buy signal, do nothing \n"
     " When MACD indicator is > BUY1 THRESHOLD and < BUY1 THRESHOLD : Try to place a buy limit order on top of the order book \n"
     " When MACD indicator is > BUY2 THRESHOLD : Do a market buy order\n"
     " => The limit order mode (betwen B1 and B2 threshold) has not been fully tested. So I recommend to only use market orders. \n"
     " For that, set BUY1 THRESHOLD to a value greater than BUY2 THRESHOLD in Config file so that only MACD > B2 THRESHOLD will occur.', default=0.994)\n"), default=999)
parser.add_argument('--buypolicytwo', dest='buyPolicyTwo', type=int, help=textwrap.dedent("\nBuy policy: \n" 
     " When MACD indicator is < BUY1 THRESHOLD : No buy signal, do nothing \n"
     " When MACD indicator is > BUY1 THRESHOLD and < BUY1 THRESHOLD : Try to place a buy limit order on top of the order book \n"
     " When MACD indicator is > BUY2 THRESHOLD : Do a market buy order\n"
     " => The limit order mode (betwen B1 and B2 threshold) has not been fully tested. So I recommend to only use market orders. \n"
     " For that, set BUY1 THRESHOLD to a value greater than BUY2 THRESHOLD in Config file so that only MACD > B2 THRESHOLD will occur.', default=0.994)\n"), default=0)
parser.add_argument('--marketorders', dest='marketOrdersEnabled', type=str, help='Orders policy : MAKER or TAKER (default = True)\n', default=True)
############################################################################################################
####### STYLING PARAMS ########
############################################################################################################
parser.add_argument('--bgcolour', dest='bgColour', type=str, help='Background Colour', default="#3e6ebb")
parser.add_argument('--fontcolour', dest='fontColour', type=str, help='Font Colour', default="#f8f8ff")
parser.add_argument('--labelbgcolour', dest='labelbgColour', type=str, help='Label Background Colour', default="#5b87ff")
parser.add_argument('--widgetbgcolour', dest='widgetbgColour', type=str, help='Widget Background Colour', default="#7195d0")
parser.add_argument('--graphbgcolour', dest='graphbgColour', type=str, help='Graph Background Colour', default="#355ea0")

args = parser.parse_args()

if(args.debug == True):
    print(args)
####################################################################################################################
######## Operational Parameters Do not chance unless you know what you are doing.
#####################################################################################################################
# Fiat Type USD/EUR/GBP full list :https://help.coinbase.com/en/pro/trading-and-funding/cryptocurrency-trading-pairs/locations-and-trading-pairs

CONFIG_FIAT_TYPE = str(args.fiat)
    
# False: CSV file input. True: Real-time market price 
CONFIG_INPUT_MODE_IS_REAL_MARKET = args.cvsMar

# Main ticker : Retrieves the next samples and processes them
CONFIG_MAIN_TICK_DURATION_IN_MS = args.mTick

# Terrestrial time between two retrieved sample. 
#Should be equal to CONFIG_MAIN_TICK_DURATION_IN_MS in live mode, custom value in simulation mode that
# depends on the csv file sampling time
CONFIG_TIME_BETWEEN_RETRIEVED_SAMPLES_IN_MS = args.retSampTimems

# UI Graph refresh per call to the main ticker
CONFIG_UI_GRAPH_UPDATE_SUBSCHEDULING = args.uiGraphUpdate

# True to record price in output csv file. For the live mode only
CONFIG_RECORD_PRICE_DATA_TO_CSV_FILE = args.cvsSave

# True to enable real buy and sell transaction to the market
CONFIG_ENABLE_REAL_TRANSACTIONS = args.realTrans

# Number of hours of historical samples to retrieve
NB_HISTORIC_DATA_HOURS_TO_PRELOAD_FOR_TRADING = args.preLoadHours

NB_SECONDS_THRESHOLD_FROM_NOW_FOR_RELOADING_DATA = 1000

CONFIG_NB_POINTS_LIVE_TRADING_GRAPH = 2500
CONFIG_NB_POINTS_SIMU_GRAPH = 620
CONFIG_NB_POINTS_INIT_SIMU_GRAPH = CONFIG_NB_POINTS_SIMU_GRAPH

# Quantum = 0.05 (%)
CONFIG_PLATFORM_TAKER_FEE_QUANTUM = 0.05 # 0.05 %
CONFIG_PLATFORM_TAKER_FEE_DEFAULT_VALUE = 5 # 0.25 %
CONFIG_PLATFORM_TAKER_FEE_MIN_ON_SLIDER = 0 # 0 %
CONFIG_PLATFORM_TAKER_FEE_MAX_ON_SLIDER = 40 # 2 %

# Quantum = 0.05 (%)
CONFIG_SELL_TRIGGER_PERCENTAGE_QUANTUM = 0.05 # 0.05 %
CONFIG_SELL_TRIGGER_PERCENTAGE_DEFAULT_VALUE = 0 # 0.0 %
CONFIG_SELL_TRIGGER_PERCENTAGE_MIN_ON_SLIDER = 0 # 0 %
CONFIG_SELL_TRIGGER_PERCENTAGE_MAX_ON_SLIDER = 40 # 2 %

# Quantum = 0.25 (%)
CONFIG_PLATFORM_AUTO_SELL_THRESHOLD_QUANTUM = 0.25 # 0.25 %
CONFIG_PLATFORM_AUTO_SELL_THRESHOLD_DEFAULT_VALUE = 0 # 0 %
CONFIG_PLATFORM_AUTO_SELL_THRESHOLD_MIN_ON_SLIDER = 0 # 0 %
CONFIG_PLATFORM_AUTO_SELL_THRESHOLD_MAX_ON_SLIDER = 40 # 10 %

CONFIG_SIMU_INITIAL_BALANCE_MIN = 0.001
CONFIG_SIMU_INITIAL_BALANCE_MAX = int(args.simMaxBal)

CONFIG_MIN_INITIAL_FIAT_BALANCE_TO_TRADE = 0.0001

CONFIG_DONATION_DEFAULT_AMOUNT_IN_BTC = 0.0002
CONFIG_BTC_DESTINATION_ADDRESS = "136wzpD2fYFRAAHLU5yVxiMNcARQtktoDo"


#####################################################################################################################
######## Trading Parameters
#####################################################################################################################
CONFIG_RISK_LINE_PERCENTS_ABOVE_THRESHOLD_TO_BUY_MIN = args.riskPerAboveMaxThreshBuy
CONFIG_RISK_LINE_PERCENTS_ABOVE_THRESHOLD_TO_BUY_MAX = args.riskPerAboveMinThreshBuy
CONFIG_RiskLinePercentsAboveThresholdToBuy = args.riskPerAboveGenThreshBuy

CONFIG_MAX_BUY_PRICE = args.maxBuyPrice


# Buy policy: 
#     When MACD indicator is < BUY1 THRESHOLD : No buy signal, do nothing
#     When MACD indicator is > BUY1 THRESHOLD and < BUY1 THRESHOLD : Try to place a buy limit order on top of the order book
#     When MACD indicator is > BUY2 THRESHOLD : Do a market buy order
#     => The limit order mode (betwen B1 and B2 threshold) has not been fully tested. So I recommend to only use market orders.
#     For that, set BUY1 THRESHOLD to a value greater than BUY2 THRESHOLD in Config file so that only MACD > B2 THRESHOLD will occur.
CONFIG_MACD_BUY_1_THRESHOLD = args.buyPolicyOne
CONFIG_MACD_BUY_2_THRESHOLD = args.buyPolicyTwo


# Sell policy:
#     When MACD indicator is > SELL1 THRESHOLD : No sell signal, do nothing
#     When MACD indicator is < SELL1 THRESHOLD and > SELL2 THRESHOLD : Try to place a sell limit order on top of the order book
#     When MACD indicator is < SELL2 THRESHOLD : Do a market sell order
#     => The limit order mode (betwen S1 and S2 threshold) has not been fully tested. So I recommend to only use market orders.
# To do that, set SELL1 THRESHOLD to a value greater than SELL2 THRESHOLD in TradingBotConfig file so that only MACD < S2 THRESHOLD will occur.
CONFIG_MACD_SELL_1_THRESHOLD = -999
CONFIG_MACD_SELL_2_THRESHOLD = 0

# A bit too approximative
MIN_CRYPTO_AMOUNT_REQUESTED_TO_SELL = 0.0005

# Minimum percentage ratio to sell with no loss : shall not include fees
CONFIG_MIN_PRICE_ELEVATION_RATIO_TO_SELL = 1.0005

# Orders policy : 'MAKER' or 'TAKER'
CONFIG_ENABLE_MARKET_ORDERS = args.marketOrdersEnabled

# Percentage of the highest ask price to set buy price
CONFIG_LIMIT_BUY_PRICE_RADIO_TO_HIGHEST_ASK = 0.999

# Percentage of the highest ask price to set buy price
CONFIG_LIMIT_BUY_PRICE_RATIO_TO_HIGHEST_ASK = 1.0000

# Percentage of the lowest ask price to set buy price
CONFIG_LIMIT_SELL_PRICE_RATIO_TO_HIGHEST_BID = 1.0000

# Crypto price quantum. Useful for rounds
CONFIG_CRYPTO_PRICE_QUANTUM = 0.0000001

# Number of confirmed samples below auto-sell threshold to actually perform auto sell
CONFIG_AUTO_SELL_NB_CONFIRMATION_SAMPLES = 10



####################################################################################################################
###########   Styling Info #######
####################################################################################################################

CONFIG_STYLE_BG_COLOUR = args.bgColour
CONFIG_STYLE_FONT_COLOUR = args.fontColour
CONFIG_STYLE_LABEL_BG_COLOUR = args.labelbgColour
CONFIG_STYLE_WIDGET_BG_COLOUR = args.widgetbgColour
CONFIG_STYLE_GRAPH_BG_COLOUR = args.graphbgColour

#####################################################################################################################
######## Debug Parameters
#####################################################################################################################

CONFIG_PUBLIC_SANDBOX_API = "https://public.sandbox.pro.coinbase.com"
CONFIG_PUBLIC_API = "https://api.pro.coinbase.com"
CONFIG_DEBUG = True
CONFIG_DEBUG_SWITCH = args.debug  

    
CONFIG_DEBUG_ENABLE_DUMMY_WITHDRAWALS = False
###########################################################################
###### VERSION INFO 
###########################################################################
CONFIG_VERSION = "0.9.8.8 RC 2"
