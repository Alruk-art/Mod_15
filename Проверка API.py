import json

with open('api1.json', encoding = 'utf8') as f:
    templates = json.load(f)
    print('Список=', templates)


def ChekInt(item):
    return isinstance(item, int)


def CheckStr(item):
    return isinstance(item, str)


def CheckBool(item):
    return isinstance(item, bool)


def CheckUrl(item):
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False


def CheckStrValue(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False


def ErrorLog(item, value, string):
    Error.append({item: f'{value}, {string}'})


listOfItems = {'timestamp': 'int', 'referer': 'url', 'location': 'url', 'remoteHost': 'str', 'partyId': 'str',
               'sessionId': 'str', 'pageViewId': 'str', 'eventType': 'str', 'item_id': 'str', 'item_price': 'int',
               'item_url': 'url','basket_price': 'int', 'detectedDuplicate': 'bool', 'detectedCorruption': 'bool',
               'firstInSession': 'bool', 'userAgentName': 'str'}
Error = []
for items in templates:
    for item in items:
        print ('item =', item)
        if item in listOfItems:
            print('Тип', type(items[item]))
            print('lOI=', listOfItems[item])
            print ('значение=', items[item])


            if listOfItems[item] == 'int':
                print ('число')
                if not ChekInt(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
                    print ('ожидали другой тип int')
            elif listOfItems[item] == 'str':
                print ('stroka')
                if not CheckStr(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
                    print('ожидали другой тип url')
            elif listOfItems[item] == 'bool':
                print ('BOOL')
                if not CheckBool(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'url':
                print ('URL')
                if not CheckUrl(items[item]):
                   ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'val':
                print ('val')
                if not CheckStrValue(items[item], ['itemBuyEvent', 'itemViewEvent']):
                    ErrorLog(item, items[item], f'ожидали тип {listOfItems}')
                    print('ожидали другой тип val')
            else:
                ErrorLog(item, items[item], 'неожиданное значение')
                print('неожиданное значение')
        else:
            ErrorLog(item, items[item], 'неизвестная переменная')
            print('неизвестная переменная')

if Error == []:
    print('Pass')
else:
    print('Fail')
    print('Error')
