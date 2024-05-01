# Pi Combination Finder

This project calculates the digits of the mathematical constant pi up to the 5 millionth decimal place and saves it to a .txt file. Then, it utilizes the script `piCombination.py` to check all 6-digit number combinations within the first 5 million digits of pi. It saves all combinations that are not found within the first 5 million digits to a file named `results.txt`.

## How it Works

1. **Calculate Pi**: The program computes the digits of pi up to the 5 millionth decimal place and saves it to a file named `pi5mn.txt`.
2. **Find Combinations**: The script `piCombination.py` scans through the first 5 million digits of pi to find all 6-digit number combinations.
3. **Save Results**: It saves all combinations that are not found within the first 5 million digits of pi to a file named `results.txt`.

## Usage

1. Run the script `piCalculation.py` to calculate the digits of pi and save them to a file.
2. Run the script `piCombination.py` to find and save all 6-digit number combinations that are not present within the first 5 million digits of pi.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or suggestions.

## License

This project is licensed under the [MIT License](LICENSE).
