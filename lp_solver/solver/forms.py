# from django import forms

# class ProductionForm(forms.Form):
#     n = forms.IntegerField(label="Количество видов продукции", initial=4)
#     m = forms.IntegerField(label="Количество видов ресурсов", initial=3)
    
#     # Тестовые данные для теста 1 и 2
#     цены = forms.CharField(label="Цены на продукцию (через запятую)", initial="23, 14, 19, 12")
#     постоянные_затраты = forms.CharField(label="Постоянные затраты (через запятую)", initial="4, 3, 6, 4")
#     переменные_затраты = forms.CharField(label="Переменные затраты (через запятую)", initial="10, 8, 5, 7")
#     спрос = forms.CharField(label="Ограничение по спросу (через запятую)", initial="6, 8, 5, 10")
#     фонд_ресурсов = forms.CharField(label="Фонд ресурсов (через запятую)", initial="35, 23, 42")
#     использование_ресурсов = forms.CharField(
#         label="Использование ресурсов на единицу продукции (через точку с запятой для каждой продукции)", 
#         initial="4,2,6,7;3,1,4,4;2,4,9,6"
#     )

#     # Дополнительные ограничения
#     мин_продукция_1 = forms.IntegerField(label="Мин. производство продукции 1", required=False, initial=2)
#     мин_продукция_2 = forms.IntegerField(label="Мин. производство продукции 2", required=False, initial=2)



from django import forms

class ProductionForm(forms.Form):
    n = forms.IntegerField(label="Количество видов продукции")
    m = forms.IntegerField(label="Количество видов ресурсов")
    
    # Тестовые данные для теста 1 и 2
    цены = forms.CharField(label="Цены на продукцию (через запятую)")
    постоянные_затраты = forms.CharField(label="Постоянные затраты (через запятую)")
    переменные_затраты = forms.CharField(label="Переменные затраты (через запятую)")
    спрос = forms.CharField(label="Ограничение по спросу (через запятую)")
    фонд_ресурсов = forms.CharField(label="Фонд ресурсов (через запятую)")
    использование_ресурсов = forms.CharField(
        label="Использование ресурсов на единицу продукции (через точку с запятой для каждой продукции)", 
    )

    # Дополнительные ограничения
    мин_продукция_1 = forms.IntegerField(label="Мин. производство продукции 1", required=False)
    мин_продукция_2 = forms.IntegerField(label="Мин. производство продукции 2", required=False)
