from driver_info import DriverInfo
from settings import BColors
import argparse

driverInfo = DriverInfo()
driverInfo.process_data()


def should_read_json():
    print(f"""{BColors.UNDERLINE}{BColors.OKBLUE}{BColors.BOLD}Test: should_read_json{BColors.ENDC}""")

    if len(driverInfo.drivers) == 12:
        print(f"""{BColors.OKGREEN}PASS: {BColors.ENDC}{len(driverInfo.drivers)} drivers loaded successfully.""")
    else:
        print(f"""{BColors.FAIL}FAIL: Error loading drivers.{BColors.ENDC}""")

    if len(driverInfo.rides) == 32:
        print(f"""{BColors.OKGREEN}PASS: {BColors.ENDC}{len(driverInfo.rides)} rides loaded successfully.""")
    else:
        print(f"""{BColors.FAIL}FAIL: Error loading rides.{BColors.ENDC}""")

    if len(driverInfo.driver_rides) == 32:
        print(f"""{BColors.OKGREEN}PASS: {BColors.ENDC}{len(driverInfo.driver_rides)} loaded successfully.""")
    else:
        print(f"""{BColors.FAIL}FAIL: Error loading driver_rides.{BColors.ENDC}""")


def should_return_only_ten():
    print(f"""{BColors.UNDERLINE}{BColors.OKBLUE}{BColors.BOLD}Test: should_return_only_ten.{BColors.ENDC}""")
    if len(driverInfo.top_ten['prompt']) == 10:
        print(f"""{BColors.OKGREEN}PASS: {BColors.ENDC}{len(driverInfo.top_ten['prompt'])} prompts.""")
    else:
        print(f"""{BColors.FAIL}FAIL: Error ranking prompts.{BColors.ENDC}""")

    if len(driverInfo.top_ten['clean']) == 10:
        print(f"""{BColors.OKGREEN}PASS: {BColors.ENDC}{len(driverInfo.top_ten['clean'])} cleans.""")
    else:
        print(f"""{BColors.FAIL}FAIL: Error ranking cleans.{BColors.ENDC}""")

    if len(driverInfo.top_ten['friendly']) == 10:
        print(f"""{BColors.OKGREEN}PASS: {BColors.ENDC}{len(driverInfo.top_ten['friendly'])} friendly.""")
    else:
        print(f"""{BColors.FAIL}FAIL: Error ranking friendly.{BColors.ENDC}""")


def should_be_sorted():
    print(f"""{BColors.UNDERLINE}{BColors.OKBLUE}{BColors.BOLD}Test: should_be_sorted.{BColors.ENDC}""")
    top_ten = driverInfo.get_top_ten()

    first = list(top_ten['prompt'][0].keys())[0]
    second = list(top_ten['prompt'][1].keys())[0]

    if top_ten['prompt'][0][first] >= top_ten['prompt'][1][second]:
        print(
            f"""{BColors.OKGREEN}PASS: {BColors.ENDC} Prompt => {first}:{top_ten['prompt'][0][first]} >= {second}:{top_ten['prompt'][1][second]}.""")
    else:
        print(f"""{BColors.FAIL}FAIL: Error ranking prompts.{BColors.ENDC}""")

    first = list(top_ten['clean'][0].keys())[0]
    second = list(top_ten['clean'][1].keys())[0]

    if top_ten['clean'][0][first] >= top_ten['clean'][1][second]:
        print(
            f"""{BColors.OKGREEN}PASS: {BColors.ENDC} Clean => {first}:{top_ten['clean'][0][first]} >= {second}:{top_ten['clean'][1][second]}.""")
    else:
        print(f"""{BColors.FAIL}FAIL: Error ranking clean.{BColors.ENDC}""")

    first = list(top_ten['friendly'][0].keys())[0]
    second = list(top_ten['friendly'][1].keys())[0]

    if top_ten['friendly'][0][first] >= top_ten['friendly'][1][second]:
        print(
            f"""{BColors.OKGREEN}PASS: {BColors.ENDC} Friendly => {first}:{top_ten['friendly'][0][first]} >= {second}:{top_ten['friendly'][1][second]}.""")
    else:
        print(f"""{BColors.FAIL}FAIL: Error ranking friendly.{BColors.ENDC}""")


def run_test():
    should_read_json()
    should_return_only_ten()
    should_be_sorted()


def show_ranking():
    rankings = driverInfo.get_top_ten()
    print(f"""{BColors.OKBLUE}{BColors.BOLD}Prompts: {BColors.ENDC}""")
    for i, rank in enumerate(rankings['prompt']):
        print(f"""{BColors.OKGREEN}{i + 1}:{BColors.ENDC} {rank}""")

    print(f"""{BColors.OKBLUE}{BColors.BOLD}Cleans: {BColors.ENDC}""")
    for i, rank in enumerate(rankings['clean']):
        print(f"""{BColors.OKGREEN}{i + 1}:{BColors.ENDC} {rank}""")

    print(f"""{BColors.OKBLUE}{BColors.BOLD}Friendly: {BColors.ENDC}""")
    for i, rank in enumerate(rankings['friendly']):
        print(f"""{BColors.OKGREEN}{i + 1}:{BColors.ENDC} {rank}""")


# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--action", help="Specifies and action to perform. (run_test, rankings)", required=True)
args = parser.parse_args()

if __name__ == "__main__":
    if args.action == 'run_test':
        print(f"""{BColors.HEADER}Action: Running tests...{BColors.ENDC}""")
        run_test()

    if args.action == 'rankings':
        print(f"""{BColors.HEADER}Action: Show rankings...{BColors.ENDC}""")
        show_ranking()
