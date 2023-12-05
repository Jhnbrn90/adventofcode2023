import re


def main():
    games = {}

    # The amount of cubes of each color, available
    # in the bag.
    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    valid_ids = []

    with open('input.txt', 'r') as f:
        for game in f.readlines():

            # Get the game ID
            game_id = re.match(r'^Game (\d+):', game)[1]
            valid_ids.append(int(game_id))

            # Get the game results
            game_result = game.split(": ")[1]

            # Count how many times each color was
            # drawn and add the highest number to
            # the tally.
            highest_count_by_color = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            for color in ('red', 'green', 'blue'):
                color_matches = re.findall(rf'(\d+) {color}', game_result)
                highest_count = max([int(count) for count in color_matches])
                highest_count_by_color[color] = highest_count

            # Update the games dictionary for the given game ID
            # and the results: the highest number of draws for each
            # given color.
            games.update({
                int(game_id): highest_count_by_color
            })

        for game_id, results in games.items():
            for color, count in results.items():
                if count > constraints[color] and int(game_id) in valid_ids:
                    valid_ids.remove(int(game_id))

        print(f'Valid game ids: {valid_ids}')
        print(f'Sum: {sum(valid_ids)}')


if __name__ == "__main__":
    main()
