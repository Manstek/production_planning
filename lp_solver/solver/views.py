from django.shortcuts import render
from .forms import ProductionForm
import pulp

def solve_problem(form_data):
    n = form_data.cleaned_data['n']
    m = form_data.cleaned_data['m']
    цены = list(map(int, form_data.cleaned_data['цены'].split(',')))
    постоянные_затраты = list(map(int, form_data.cleaned_data['постоянные_затраты'].split(',')))
    переменные_затраты = list(map(int, form_data.cleaned_data['переменные_затраты'].split(',')))
    спрос = list(map(int, form_data.cleaned_data['спрос'].split(',')))
    фонд_ресурсов = list(map(int, form_data.cleaned_data['фонд_ресурсов'].split(',')))
    использование_ресурсов = [
        list(map(int, row.split(','))) for row in form_data.cleaned_data['использование_ресурсов'].split(';')
    ]
    
    # Дополнительные ограничения
    мин_продукция_1 = form_data.cleaned_data['мин_продукция_1'] or 0
    мин_продукция_2 = form_data.cleaned_data['мин_продукция_2'] or 0

    # Модель решения
    problem = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

    # Переменные
    x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat='Continuous') for j in range(n)]
    y = [pulp.LpVariable(f"y_{j}", cat='Binary') for j in range(n)]

    # Целевая функция
    profit = pulp.lpSum([цены[j] * x[j] - (y[j] * постоянные_затраты[j] + переменные_затраты[j] * x[j]) for j in range(n)])
    problem += profit, "Total Profit"

    # Ограничения по ресурсам
    for i in range(m):
        problem += pulp.lpSum([использование_ресурсов[i][j] * x[j] for j in range(n)]) <= фонд_ресурсов[i], f"Resource_{i+1}_constraint"

    # Ограничения по спросу
    for j in range(n):
        problem += x[j] <= спрос[j] * y[j], f"Demand_{j+1}_constraint"

    # Дополнительные ограничения
    problem += x[0] >= мин_продукция_1, "Min_x1"
    problem += x[1] >= мин_продукция_2, "Min_x2"

    # Решение задачи
    problem.solve()

    # Получение результата
    solution = {
        'status': pulp.LpStatus[problem.status],
        'results': {f'Продукция {j+1}': x[j].varValue for j in range(n)},
        'profit': pulp.value(problem.objective)
    }
    
    return solution

def solve_view(request):
    if request.method == 'POST':
        form = ProductionForm(request.POST)
        if form.is_valid():
            result = solve_problem(form)
            return render(request, 'solver/result.html', {'form': form, 'result': result})
    else:
        form = ProductionForm()
    
    return render(request, 'solver/index.html', {'form': form})
