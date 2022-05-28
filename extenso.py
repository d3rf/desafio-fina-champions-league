numbers = ['','um','dois','três','quatro','cinco','seis','sete','oito','nove']
numbers_plus = ['dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
dozens = ['','dez','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
hundreds = ['','cento','duzentos','trezentos','quatrozentos','quinhetos','seiscentos','setecentos','oitocentos','novecentos']

def translate_extenso(number):
    stringfy_number = str(number)
    digit_extension = ''
    decimal_part = 0
    integer_part = stringfy_number
    if '.' in stringfy_number:
        aux = stringfy_number.split('.')
        integer_part = aux[0]
        decimal_part = aux[1]
        if len(decimal_part) == 1:
            digit_extension = dozens[int(decimal_part)]
        elif len(decimal_part) == 2:
            if int(decimal_part[0]) == 1:
                digit_extension = numbers_plus[int(decimal_part[1])]
            else:
                digit_extension = dozens[int(decimal_part[0])] +' e '+numbers[int(decimal_part[1])]
    pos = 0
    final_order = [digit_extension]
    reversed_decimal_part = integer_part[::-1]
    for n in reversed_decimal_part:
        number_to_handler = int(n)
        if pos == 0:
            if number_to_handler > 0: final_order.append(numbers[number_to_handler])
        elif pos == 1:
            item = dozens[number_to_handler]
            if item == 'dez' and int(last_number_to_help) > 0:
                final_order.pop()
                item = numbers_plus[last_number_to_help]
            if len(item) > 0:
                final_order.append(item)
        elif pos == 2:
            item = hundreds[number_to_handler]
            if reversed_decimal_part[0:2] == '00' and item == 'cento':
                item = "cem"
            final_order.append(item)
        last_number_to_help = number_to_handler
        pos = pos + 1
    
    print(' e '.join(final_order[::-1]))

number_example = 19.99
translate_extenso(number_example)
