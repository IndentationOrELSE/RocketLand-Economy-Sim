import random
import matplotlib.pyplot as plt

Buyers = [
    {'name': 'Buyer1' , 'limit': 10} ,
    {'name': 'Buyer2' , 'limit': 20} ,
    {'name': 'Buyer3' , 'limit': 60} ,
    {'name': 'Buyer4' , 'limit': 90} ,
    {'name': 'Buyer5' , 'limit': 20} ,
]
Sellers = [
    {'name': 'Seller1' , 'limit': 10} ,
    {'name': 'Seller2' , 'limit': 20} ,
    {'name': 'Seller3' , 'limit': 30} ,
    {'name': 'Seller4' , 'limit': 40} ,
]


def transact(minlimit , maxlimit , seller , customer):
    if minlimit <= maxlimit:
        print(
            f"Transaction successful between {seller['name']} ({seller['limit']}) and {customer['name']} ({customer['limit']})!")
        seller['limit'] += 5
        customer['limit'] -= 5
    else:
        print(
            f"Transaction failed between {seller['name']} ({seller['limit']}) and {customer['name']} ({customer['limit']})!")
        seller['limit'] -= 5
        customer['limit'] += 5
    print(
        f"{seller['name']}'s limit is now {seller['limit']} and {customer['name']}'s limit is now {customer['limit']}." ,
        end="\n\n")


def avg(sellers=False):
    if not sellers:
        total = 0
        for buyer in Buyers:
            total += buyer['limit']
        return round(total / len(Buyers))
    else:
        total = 0
        for seller in Sellers:
            total += seller['limit']
        return round(total / len(Sellers))


def run():
    BusyCustomers = []  # Clear BusyCustomers for each seller
    for Seller in Sellers:
        customer = random.choice(Buyers)
        if (customer in BusyCustomers) and (len(BusyCustomers) != len(Buyers)):
            while customer in BusyCustomers:
                customer = random.choice(Buyers)
                if customer not in BusyCustomers:
                    break
        else:
            transact(Seller['limit'] , customer['limit'] , Seller , customer)
            BusyCustomers.append(customer)
            break


NoOfDays = 50

averagesBuyers = []
averagesSellers = []
averages = []
for i in range(NoOfDays):
    run()
    averagesBuyers.append(avg())
    averagesSellers.append(avg(True))
    averages.append((avg() + avg(True)) / 2)

days = []
i = 0
if __name__ == '__main__':
    for i in range(NoOfDays):
        i += 1
        days.append(i)
    # Buyers
    plt.plot(days , averagesBuyers , label="Buyer maximum" , color="orange")
    # Sellers
    plt.plot(days , averagesSellers , label="Seller maximum" , color="blue")
    # Mean of both
    plt.plot(days , averages , label="Average sale" , color="red")
    plt.xlabel('Days')
    plt.ylabel('Economy Averages')
    plt.title('The economy in Rocketland - a simulation of supply and demand.')
    plt.legend()
    plt.show()
