from parse_sites import parsing

class logics:
    pars = parsing()
    spred: {float: object} = {}
    fiats = ('GBP', 'USD', 'CZK')
    wallets = ('Revolut', 'Wise', "QIWI","Юmoney")
    sites = ('BINANCE', 'KUKOIN')

    def reload(self, site, fiat, wallet):
        try:
            self.spred.clear()
            if fiat == "ВСЕ" and wallet == 'ВСЕ' and site == 'ВСЕ':
                monsey = list(map(lambda z: list(map(lambda x: list(map(lambda y: self.all_money(y, x, z), self.fiats)), self.wallets)),self.sites))
                for i in monsey:
                    for ii in i:
                        for iii in ii:
                            self.calculate_spred(iii)

            elif fiat == "ВСЕ" and wallet == "ВСЕ":
                monsey = list(map(lambda x: list(map(lambda y:self.all_money(y,x,site),self.fiats)), self.wallets))
                for i in monsey:
                    for ii in i:
                        self.calculate_spred(ii)
            elif fiat == "ВСЕ" and site == "ВСЕ":
                monsey = list(map(lambda x: list(map(lambda y: self.all_money(y, wallet, x), self.fiats)), self.sites))
                for i in monsey:
                    for ii in i:
                        self.calculate_spred(ii)
            elif wallet == "ВСЕ" and site == "ВСЕ":
                monsey = list(map(lambda x: list(map(lambda y: self.all_money(fiat, y, x), self.wallets)), self.sites))
                for i in monsey:
                    for ii in i:
                        self.calculate_spred(ii)

            elif wallet == 'ВСЕ':
                monsey = list(map(lambda x: self.all_money(fiat, x, site), self.wallets))
                for i in monsey:
                    self.calculate_spred(i)
            elif fiat == 'ВСЕ':
                monsey = list(map(lambda x: self.all_money(x, wallet, site), self.fiats))
                for i in monsey:
                    self.calculate_spred(i)
            elif site == 'ВСЕ':
                monsey = list(map(lambda x: self.all_money(fiat, wallet, x), self.sites))
                for i in monsey:
                    self.calculate_spred(i)

            else:
                monsey = list(self.all_money(fiat, wallet, site))
                self.calculate_spred(monsey)

            return max(self.spred.keys()), self.spred[max(self.spred.keys())]
        except:
            pass

    def all_money(self, fiat, wallet, site):
        try:
            buy_map = self.pars.binance(asset='USDT', fiat=fiat, tradeType='BUY', payTypes=wallet, site=site)
            sell_map = self.pars.binance(asset='USDT', fiat=fiat, tradeType='SELL', payTypes=wallet, site=site)
            return list(buy_map[0]), list(sell_map[0]), buy_map[1], buy_map[2]
        except TypeError:
            return (),()

    def calculate_spred(self, monsey):
        try:
            spred = float(monsey[1][3]) / float(monsey[0][3]) * 100 - 100
            self.spred[spred] = monsey
        except IndexError:
            pass

