types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

# Удаляем дубликаты внутри списков
def remove_duplicates_in_lists(tickets):
    new_tickets = {}
    for k, v in tickets.items():
        unique = []
        for ticket in v:
            if ticket not in unique:
                unique.append(ticket)
        new_tickets[k] = unique
    return new_tickets

# Составляем словарь с названиями критичности от 1 до 5
def organize_tickets(types, tickets):
    tickets = remove_duplicates_in_lists(tickets)
    result = {}
    used_tickets = []

    for level in sorted(types):  # Уровни от 1 до 5
        current = []
        for ticket in tickets.get(level, []):
            if ticket not in used_tickets:
                current.append(ticket)
                used_tickets.append(ticket)
        result[types[level]] = current
    return result