from argentina_rates import Rates

def main():
	rate = Rates()
	rates = rate.get_btc_rates()
	print(rates)


if __name__ == "__main__":
	main()