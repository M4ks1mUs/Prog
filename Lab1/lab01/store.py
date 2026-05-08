#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_store_inventory():
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }

    store = {
        '12345': [
            {'quantity': 27, 'price': 42},
        ],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }

    lamp_code = goods['Лампа']
    lamps_item = store[lamp_code][0]
    lamps_quantity = lamps_item['quantity']
    lamps_price = lamps_item['price']
    lamps_cost = lamps_quantity * lamps_price
    lamp_result = f'Лампа - {lamps_quantity} шт, стоимость {lamps_cost} руб'

    tables_cost1 = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
    tables_cost2 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
    tables_cost = tables_cost1 + tables_cost2  # Стоимость всех столов на складе
    tables_quantity = store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']
    table_result = f'Стол - {tables_quantity} шт, стоимость {tables_cost} руб'

    sofas_cost1 = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
    sofas_cost2 = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
    sofas_cost = sofas_cost1 + sofas_cost2  # Стоимость всех диванов на складе
    sofas_quantity = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']
    sofa_result = f'Диван - {sofas_quantity} шт, стоимость {sofas_cost} руб'

    chairs_cost1 = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
    chairs_cost2 = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
    chairs_cost3 = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
    chairs_cost = chairs_cost1 + chairs_cost2 + chairs_cost3   # Стоимость всех стульев на складе
    chairs_quantity = store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] + store[goods['Стул']][2]['quantity']
    chair_result = f'Стул - {chairs_quantity} шт, стоимость {chairs_cost} руб'

    return lamp_result, table_result, sofa_result, chair_result