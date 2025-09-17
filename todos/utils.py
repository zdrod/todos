def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."
    elif not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters"
    else:
        return None

def find_list_by_id(list_id, lists):
    return next((lst for lst in lists if lst['id'] == list_id), None)

def error_for_todo(title):
    if not 1 <= len(title) <= 100:
        return "Todo title must be between 1 and 100 characters"

    return None

def find_todo_by_id(todo_id, todos):
    return next((todo for todo in todos if todo['id'] == todo_id), None)

def delete_todo_by_id(todo_id, lst):
    lst['todos'] = [todo for todo in lst['todos'] if todo['id'] != todo_id]
    return None

def mark_all_completed(lst):
    for todo in lst['todos']:
        todo['completed'] = True

    return None

def todos_remaining(lst):
    return sum(1 for todo in lst['todos'] if not todo['completed'])

def is_list_completed(lst):
    return len(lst['todos']) > 0 and todos_remaining(lst) == 0

def sort_lists(lists):
    sorted_lists = sorted(lists, key=lambda lst: lst['title'].casefold())

    incomplete_lists = [lst for lst in sorted_lists if not is_list_completed(lst)]
    complete_lists = [lst for lst in sorted_lists if is_list_completed(lst)]

    return incomplete_lists + complete_lists

def is_todo_completed(todo):
    return todo['completed']

def sort_todos(todos):
    sorted_todos = sorted(todos, key=lambda t: t['title'])
    incomplete_todos = [todo for todo in sorted_todos if not is_todo_completed(todo)]
    complete_todos = [todo for todo in sorted_todos if is_todo_completed(todo)]

    return incomplete_todos + complete_todos