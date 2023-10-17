import requests
import json


class parsing:
    buy_parrams = list
    sell_parrams = list

    indexes_binance = ('tradeType', 'asset', 'fiatUnit', 'price', 'surplusAmount', 'minSingleTransAmount',
               'maxSingleTransAmount',
               'tradeMethodShortName', 'classify', 'monthOrderCount', 'monthFinishRate', 'positiveRate')

    indexes_bybit = ('payments', 'tokenId', 'currencyId', 'price', 'lastQuantity', 'minAmount', 'maxAmount','recentOrderNum',
                     'recentExecuteRate')


    index_kucoin = ('side', 'currency', 'legal', 'floatPrice', 'currencyBalanceQuantity',
                    'limitMinQuote', 'limitMaxQuote', 'dealOrderRate', 'dealOrderNum',
                    'payTypeCode', 'displayStatus')

    def binance(self, asset, fiat, tradeType, payTypes, site):
        try:
            global result, URL
            if site == "BINANCE":
                URL = r'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
                data = {
                    'proMerchantAds': False,
                    'page': 1,
                    'rows': 10,
                    'payTypes': [payTypes],
                    'countries': [],
                    'publisherType': None,
                    'asset': asset,
                    'fiat': fiat,
                    'tradeType': tradeType,
                }
                result = requests.post(URL, json=data)
                result = json.loads(result.text)

            elif site == "BYBIT":
                pay_type = "65" if payTypes == "Revolut" else("78" if payTypes == "Wise" else None)
                trade_type = "1" if tradeType == 'BUY' else("0" if tradeType == 'SELL' else None)
                URL = r'https://api2.bybit.com/fiat/otc/item/online'
                data = {
                    'amount': "",
                    'authMaker': 'false',
                    'canTrade': 'false',
                    'currencyId': fiat,
                    'page': "1",
                    'payment': [pay_type],
                    'side': trade_type,  # 1 - покупка 2- продажа
                    'size': "10",
                    'tokenId': "USDT",
                    'userId': " "
                }
                result = requests.post(URL, json=data)
                result = json.loads(result.text)

            elif site == "KUKOIN":
                URL = f'https://www.kucoin.com/_api/otc/ad/list?currency=USDT&side={tradeType}&legal=' \
                      f'{fiat}&page=1&pageSize=10&status=PUTUP&lang=ru_RU'
                data = {
                    "success": "true",
                    "code": "200",
                    "msg": "success",
                    "retry": "false",
                    "currentPage": 1,
                    "pageSize": 10,
                    "totalNum": 36,
                }
                result = requests.get(URL, json=data)
                result = json.loads(result.text)

            x = result['data'][0] if site == "BINANCE" else(result['result']['items'][0] if site == "BYBIT"else (result['items'][0]if site == 'KUKOIN' else None))

            slov = map(lambda y: x['adv']['tradeMethods'][0][y] if y == 'tradeMethodShortName' else(x['advertiser'][y]
                if y in ('monthOrderCount', 'positiveRate', 'monthFinishRate') else x['adv'][y]), self.indexes_binance)\
                if site == "BINANCE" else(map(lambda y: x[y], self.indexes_bybit)if site == 'BYBIT'
                                          else(list(map(lambda y: x['adPayTypes'][0][y] if y == 'payTypeCode' else x[y], self.index_kucoin)))if site == 'KUKOIN'else None)

            return slov, site, payTypes

        except IndexError:
            pass
