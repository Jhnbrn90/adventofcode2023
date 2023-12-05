import re


def main():
    games = {}
    cube_powers = []

    with open('input.txt', 'r') as f:
        for game in f.readlines():

            # Get the game ID
            game_id = re.match(r'^Game (\d+):', game)[1]

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
            cube_power = results['blue'] * results['red'] * results['green']
            cube_powers.append(cube_power)

        print(f'Cube powers: {sum(cube_powers)}')


if __name__ == "__main__":
    main()
