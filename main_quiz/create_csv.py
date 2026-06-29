"""
This file contains the functions for reading and writing the quiz results to csv.
"""

import csv
class CsvCreate:
    """Create CSV file which logs the name and score of user
    """

    @staticmethod
    def save_result(name, score):

        with open("results.csv", "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([name, score])

    @staticmethod
    def read_results():

        results = []
        """""
        The try and except is used if the CSV file does not exist yet, preventing the quiz from crashing.
        """
        try:
            with open("results.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    results.append(row)

        except FileNotFoundError:
            print("No results file found.")

        return results