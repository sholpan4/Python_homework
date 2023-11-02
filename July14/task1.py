import json
import time

def load_quest(quest_file):
    try:
        with open(quest_file, 'r', encoding='utf-8') as file:
            quest_data = json.load(file)
        return quest_data
    except FileNotFoundError:
        print("Файл с квестом не найден.")
        return None
    except json.JSONDecodeError:
        print("Ошибка при чтении файла с квестом.")
        return None

def play_quest(quest_file):
    quest_data = load_quest(quest_file)

    if quest_data is None:
        return

    game_info = quest_data.get("game_info", {})
    game = quest_data.get("game", {})
    current_scene = game.get("SCENE_0")

    while current_scene:
        description = current_scene.get("DESCRIPTION")
        actions = current_scene.get("ACTIONS")

        if description:
            print(description)

        if actions:
            for action in actions:
                if is_action_available(action, game_info):
                    print(f" - {action['TEXT']}")

            user_input = input("Что будете делать? Введите номер действия: ")

            try:
                user_choice = int(user_input)
                if 1 <= user_choice <= len(actions):
                    selected_action = actions[user_choice - 1]
                    execute_action(selected_action, game_info)
                    time.sleep(2)
                else:
                    print("Некорректный выбор. Пожалуйста, выберите действие из списка.")
            except ValueError:
                print("Пожалуйста, введите номер действия.")

            current_scene = game.get(selected_action["GO"])

        else:
            print("Конец игры.")
            break

def is_action_available(action, game_info):
    conditions = action.get("when", [])

    for condition in conditions:
        if condition["condition"] == "HAVE":
            if condition["item"] not in game_info["inventory"]:
                return False
        elif condition["condition"] == "LACK":
            if condition["item"] in game_info["inventory"]:
                return False
        elif condition["condition"] == "MISSED":
            if condition["scene"] in game_info["visited_scenes"]:
                return False
        elif condition["condition"] == "PASSED":
            if condition["scene"] not in game_info["visited_scenes"]:
                return False

    return True

def execute_action(action, game_info):
    action_type = action["ACTION"]

    if action_type == "GO":
        print(action["TEXT"])
        game_info["visited_scenes"].append(action["GO"])
    elif action_type == "ALERT":
        print(action["TEXT"])
    elif action_type == "COLLECT":
        print(f"Вы взяли {action['item']}.")
        game_info["inventory"].append(action["item"])
    elif action_type == "DISPOSE":
        print(f"Вы избавились от {action['item']}.")
        game_info["inventory"].remove(action["item"])

if __name__ == "__main__":
    quest_file = "quest_file/kolobok.json"  
    play_quest(quest_file)