import json
import os
import TradingBotConfig as theConfig

class GDAXCurrencies:
    
    @staticmethod
    def get_all_pairs():
        return [
                "ALGO-"+theConfig.CONFIG_FIAT_TYPE,
                "AAVE-"+theConfig.CONFIG_FIAT_TYPE,
                "AMP-"+theConfig.CONFIG_FIAT_TYPE,
                "COMP-"+theConfig.CONFIG_FIAT_TYPE, 
                "DAI-"+theConfig.CONFIG_FIAT_TYPE,
                "DOGE-"+theConfig.CONFIG_FIAT_TYPE, 
                "ETC-"+theConfig.CONFIG_FIAT_TYPE,
                "ETH-"+theConfig.CONFIG_FIAT_TYPE,
                "GRT-"+theConfig.CONFIG_FIAT_TYPE,
                "1INCH-"+theConfig.CONFIG_FIAT_TYPE,  
                "ADA-"+theConfig.CONFIG_FIAT_TYPE,
                "ANKR-"+theConfig.CONFIG_FIAT_TYPE,
                "ATOM-"+theConfig.CONFIG_FIAT_TYPE,
                "BAL-"+theConfig.CONFIG_FIAT_TYPE,
                "BAND-"+theConfig.CONFIG_FIAT_TYPE,
                "BAT-"+theConfig.CONFIG_FIAT_TYPE,
                "BCH-"+theConfig.CONFIG_FIAT_TYPE,
                "BNT-"+theConfig.CONFIG_FIAT_TYPE,
                "BON-"+theConfig.CONFIG_FIAT_TYPE,
                "BTC-"+theConfig.CONFIG_FIAT_TYPE,
                "CGLD-"+theConfig.CONFIG_FIAT_TYPE,
                "CHZ-"+theConfig.CONFIG_FIAT_TYPE,
                "CRV-"+theConfig.CONFIG_FIAT_TYPE,
                "CTSI-"+theConfig.CONFIG_FIAT_TYPE,
                "DASH-"+theConfig.CONFIG_FIAT_TYPE,
                "DOT-"+theConfig.CONFIG_FIAT_TYPE,
                "ENJ-"+theConfig.CONFIG_FIAT_TYPE,
                "EOS-"+theConfig.CONFIG_FIAT_TYPE,
                "FIL-"+theConfig.CONFIG_FIAT_TYPE,
                "FORTH-"+theConfig.CONFIG_FIAT_TYPE,
                "GTC-"+theConfig.CONFIG_FIAT_TYPE,
                "ICP-"+theConfig.CONFIG_FIAT_TYPE,
                "KEEP-"+theConfig.CONFIG_FIAT_TYPE,
                "KNC-"+theConfig.CONFIG_FIAT_TYPE,
                "LOOM-"+theConfig.CONFIG_FIAT_TYPE,
                "LPT-"+theConfig.CONFIG_FIAT_TYPE,
                "LRC-"+theConfig.CONFIG_FIAT_TYPE,
                "LTC-"+theConfig.CONFIG_FIAT_TYPE,
                "MATIC-"+theConfig.CONFIG_FIAT_TYPE,
                "MIR-"+theConfig.CONFIG_FIAT_TYPE,
                "MLN-"+theConfig.CONFIG_FIAT_TYPE,
                "NKN-"+theConfig.CONFIG_FIAT_TYPE,
                "NMR-"+theConfig.CONFIG_FIAT_TYPE,
                "NU-"+theConfig.CONFIG_FIAT_TYPE,
                "OGN-"+theConfig.CONFIG_FIAT_TYPE,
                "OMG-"+theConfig.CONFIG_FIAT_TYPE,
                "OXT-"+theConfig.CONFIG_FIAT_TYPE,
                "QNT-"+theConfig.CONFIG_FIAT_TYPE,
                "REN-"+theConfig.CONFIG_FIAT_TYPE,
                "RLC-"+theConfig.CONFIG_FIAT_TYPE,
                "SKL-"+theConfig.CONFIG_FIAT_TYPE,
                "SNX-"+theConfig.CONFIG_FIAT_TYPE,
                "SOL-"+theConfig.CONFIG_FIAT_TYPE,
                "STORJ-"+theConfig.CONFIG_FIAT_TYPE,
                "SUSHI-"+theConfig.CONFIG_FIAT_TYPE,
                "TRB-"+theConfig.CONFIG_FIAT_TYPE,
                "UMA-"+theConfig.CONFIG_FIAT_TYPE,
                "UNI-"+theConfig.CONFIG_FIAT_TYPE,
                "WTBC-"+theConfig.CONFIG_FIAT_TYPE,
                "XLM-"+theConfig.CONFIG_FIAT_TYPE,
                "XTZ-"+theConfig.CONFIG_FIAT_TYPE,
                "YFI-"+theConfig.CONFIG_FIAT_TYPE,
                "ZE-"+theConfig.CONFIG_FIAT_TYPE,
                "ZRX-"+theConfig.CONFIG_FIAT_TYPE
        ]

    @staticmethod
    def get_currencies_list():
        PATH = './menu.json'
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            f = open(PATH)
            data = json.load(f)
            map = []
            for i in data["menu"]:
                map.append({
                    "full": i["pair"],
                    "coin": i["crypto"],
                    "fiat": i["fiat"]
                })
            return map
        else:    
            pairs = GDAXCurrencies.get_all_pairs()
            map = []
            for pair in pairs:
                pieces = pair.split('-')
                map.append({
                    "full": pair,
                    "coin": pieces[0],
                    "fiat": theConfig.CONFIG_FIAT_TYPE
                })

            return map
        
    @staticmethod
    def get_index_for_currency_pair(pair):
        return GDAXCurrencies.get_all_pairs().index(pair)