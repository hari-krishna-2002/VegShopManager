from datetime import datetime


vegetables=['tomato','potato','bringal','cucumber','ladyfinger','drumstick','green chilli','cabege']
dump=[40,20,20,30,15,15,10,25]
quantity=[40,20,20,30,15,15,10,25]
price=[40,50,40,30,40,40,60,30]
cart=[]
trash=[]
pin_number='2002'

now = datetime.now()
current_date = now.date()
current_time = now.time()
current_time1 = now.strftime("%H%M%S")
t=int(current_time1)

shop_status='open'



print('*'*20,'Vegetable Shop','*'*20)
#print('choos your designation below')
while True:
    print('choos your designation below\n'
          'OR if you wanna exit type "EXIT"')
    desg=input('owner/customer:')
    if desg=='owner':
        passkey=input('enter passkey:')
        if passkey==pin_number:
            if t >=200000:
                print("Hello..! sir. It's already 8 pm.")
                close_req=input('Do you want to close the Shop (yes/no):')
                if close_req=='yes':
                    shop_status='closed'
                    print(f'Shop is {shop_status}...!')
                    continue
            while True:
                print('\nwhat you wanna do?\n'
                      '0. Exit\n'
                      '1. View available vegetables\n'
                      '2. View price of each vegetable\n'
                      '3. view sales report\n'
                      '4. Add Vegetables\n'
                      '5. Remove vegetables\n'
                      '6. Change prices\n'
                      '7. Change Passkey\n')
                ch1=int(input('your choice:'))
                if ch1==1:
                    #print(vegetables)
                    for i in zip(vegetables,quantity):
                        print(i[0],'->',i[1],'kgs')
                elif ch1==0:
                    break
                elif ch1==2:
                    for i in zip(vegetables,price):
                        print(i[0],'->',i[1],'rupees')
                elif ch1==3:
                    print('*'*10,'Salse Report','*'*10)
                    print(f'date:{current_date}\n'
                          f'time:{current_time}\n')
                    print('name  ->  dump  ->  saled  ->  price  ->   amt')
                    total_revenu = 0
                    for i in vegetables:
                        idx = vegetables.index(i)
                        print()
                        amt=(dump[idx] - quantity[idx]) * price[idx]
                        total_revenu = total_revenu+ amt
                        print(i, ' -> ', dump[idx], ' -> ', dump[idx] - quantity[idx], '  ->  ', price[idx], '  ->   ',amt)
                    print('\n','Total Revenu= ',total_revenu)
                    print('*' * 30)
                elif ch1==4:
                    item=input('enter vegetable name:')
                    if item in vegetables:
                        idx = vegetables.index(item)
                        print(item,'is availabe of',quantity[idx],'kgs')
                        add_qty=int(input('enter how much quantity adding(Kgs):'))
                        quantity[idx]=quantity[idx]+add_qty
                        #dump[idx] += add_qty
                        print('added successfully')
                    else:
                        print('this is a new vegetable..!')
                        vegetables.append(item)
                        item_qty=int(input('enter how much Quantity adding(KGs):'))
                        idx=vegetables.index(item)
                        #print(idx)
                        quantity.insert(idx,item_qty)
                        #print(quantity)
                        item_price=int(input(f'enter price of {item} per KG:'))
                        price.insert(idx,item_price)
                        #print(price)
                        print('added successfully')
                    dump=quantity
                elif ch1==5:
                    rem_item=input('which vegetable you wanna remove:')
                    if rem_item in vegetables:
                        idx=vegetables.index(rem_item)
                        #print('index of rem_item',idx)
                        print(f'Available {rem_item} : {quantity[idx]} kgs only')
                        rem_quantity=int(input(f'how much quantity of {rem_item} has to be removed:'))
                        if quantity[idx]>=rem_quantity:
                            #print(quantity[idx])

                            quantity[idx] -= rem_quantity
                            #print('quty',quantity[idx])
                            #dump[idx] -= rem_quantity

                            #print(dump)
                            #print(dump[idx])
                            #dump[idx] = dump[idx]-rem_quantity
                            print('Removed Successfully..!')
                        elif quantity[idx]==0:
                            print(f'there are no {vegetables[idx]} in the shop')
                        else:
                            print(f'we only have {quantity[idx]} kgs of {rem_item} only')
                    else:
                        print(f'{rem_item} is not available in the shop.')

                elif ch1==6:
                    veg_name=input('which vegetable price is changing:')
                    if veg_name in vegetables:
                        idx=vegetables.index(veg_name)
                        print(f'current price of {veg_name}={price[idx]}rupees/kg')
                        new_price=int(input('enter new price:'))
                        price[idx]=new_price
                        print('changed successfully')
                elif ch1==7:
                    print(f'your old passkey is {pin_number}')
                    while True:
                        pre_pin=input('enter a new pass key:')
                        if len(pre_pin)>=4:
                            pin_number=pre_pin
                            print('passkey changed successfully..!')
                            break
                        else:
                            print('passkey must greater 4 charaters')
                else:
                    print('invalid choice')
        else:
            print('incorrect passkey...!')
    elif desg=='customer':
        if shop_status=='closed':
            print(f'Sorry..! the shop is {shop_status} for today.')
            continue
        while True:
            print('*'*5,'Available Vegetables','*'*5)
            for i in zip(vegetables,price):
                print(i[0],'->',i[1],'rupees /Kg')
            ch2=input('\nAre you wanna buy somthing? (yes/no):')

            if ch2=='yes':
                print(" if you don't want anything type 'nothing else'")
                while True:
                    req_item=input('what do you want:')
                    if req_item in vegetables:
                        idx=vegetables.index(req_item)
                        req_qty=float(input('how much quantity you want(kgs):'))
                        if quantity[idx]==0:
                            print('Sorry out of Stock..!')
                        elif req_qty<=quantity[idx]:
                            print(f'for {req_qty}kgs of {req_item} pay {req_qty * price[idx]}')
                            packet=(req_item,req_qty,req_qty * price[idx])
                            cart.append(packet)
                            quantity[idx] -= req_qty

                        else:
                            print(f'Available {req_item}:{quantity[idx]} kgs only')
                    elif req_item=='nothing else':
                        print('your Bill is Here\n')
                        print('/*\*'*10)
                        print(f'date:{current_date}\n'
                              f'time:{current_time}\n')
                        sum=0
                        for i in cart:
                            print(i[0],'-',i[1],'kgs  -',i[2],'rupees')
                            sum+=i[2]
                        print(f'\nTotal Amount={sum}')
                        print('/*\*' * 10)
                        print('\n')
                        #print(cart)
                        break
                    else:
                        print(f'Sorry!, We dont sale {req_item}')
            elif ch2 != 'yes' and ch2 != 'no':
                print("sorry..!, i didn't get you")
            else:
                print('Thank you..!, Visit Again.\n')
                cart.clear()
                break
    elif desg=='EXIT':
        break
    else:
        print('choose valid designation...!')