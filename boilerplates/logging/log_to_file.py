import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def main():
	logging.warning('Hello, World!')


if __name__ == "__main__":
	main()