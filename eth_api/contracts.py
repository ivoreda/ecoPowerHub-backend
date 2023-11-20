from web3 import Web3

class SmartContract:
    def __init__(self, contract_address, contract_abi, ethereum_node_url):
        self.w3 = Web3(Web3.HTTPProvider(ethereum_node_url))
        self.contract = self.w3.eth.contract(
            address=contract_address, abi=contract_abi)

    def create_company(self, name, totalCompanyValue, totalShares, sharePrice, buyableShares):
        try:
            company = self.contract.functions.createCompany(
                str(name), int(totalCompanyValue), int(totalShares), int(sharePrice), int(buyableShares)).call()
            
            print(company)
            # or event tracker here
            return company
        except Exception as e:
            raise RuntimeError(f"Error calling create_company: {str(e)}")

    # write event tracker here
    

    # def invest(self, )
    # invest
    # buy stuff
    # withdraw
    # check balance




        

    def check_fav_num(self):
        try:
            number = self.contract.functions.checkFavNumber().call()
            return number
        except Exception as e:
            raise RuntimeError(f"Error calling check_fav_num: {str(e)}")

    def increase_fav_num(self):
        try:
            number = self.contract.functions.increaseFavNumber().call()
            return number
        except Exception as e:
            raise RuntimeError(f"Error calling increase_fav_num: {str(e)}")

    def decrease_fav_num(self):
        try:
            number = self.contract.functions.decreaseFavNumber().call()
            return number
        except Exception as e:
            raise RuntimeError(f"Error calling decrease_fav_number: {str(e)}")
