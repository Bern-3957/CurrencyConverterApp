from django.shortcuts import render
import requests
# Create your views here.

def converter(request):

    list_cours = requests.get('https://openexchangerates.org/api/latest.json?app_id=1c1e670597d244a59eff84e669cb70a1').json()
    fin_list = list_cours['rates']

    if request.method == 'GET':
        context = {'fin_list': fin_list}
        return render(request, 'Converter/index.html', context=context)

    if request.method == 'POST':
        input_value = float(request.POST.get('input_value'))
        give_away_valute = request.POST.get('give_away')
        receive = request.POST.get('receive')

        give_away_value = fin_list[give_away_valute]
        res = (input_value/give_away_value) * fin_list[receive]

        context = {
            'fin_list': fin_list,
            'input_value': input_value,
            'give_away_valute': give_away_valute,
            'receive': receive,
            'res': res

        }
        return render(request, 'Converter/index.html', context=context)
