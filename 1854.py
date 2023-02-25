def maximumPopulation(logs) -> int:
    dates = []
    for birth, death in logs:
        dates.append((birth, 1))
        dates.append((death, -1))

    dates.sort()

    population = max_population = max_year = 0
    for year, change in dates:
        population += change
        if population > max_population:
            max_population = population
            max_year = year

    return max_year

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1993,1999],[2000,2010]],
            "expected": 1993
        },
        {
            "name": "simple case 2",
            "input": [[1950,1961],[1960,1971],[1970,1981]],
            "expected": 1960
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maximumPopulation(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))