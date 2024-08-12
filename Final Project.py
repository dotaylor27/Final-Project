"""
Taylor Do
1677976
"""
# Import module to read csv files
import csv
from datetime import datetime

# Create class with all attributes
class Product:
    def __init__(self, prodId, manu, item, dam, price=None, serviceDate=None):
        self.prodId = prodId
        self.manu = manu
        self.item = item
        self.dam = dam
        self.price = price
        self.serviceDate = serviceDate

# Create library to hold all objects
def main():
    all_products = []

# Read ManufactererList file
    with open("ManufacturerList.csv", 'r') as manu_file:
        reader = csv.reader(manu_file)
        #loop through each entry and assign to product attibutes
        for each in reader:
            prodId = each[0]
            manu = each[1]
            item = each[2]
            # check if item is damaged 
            if each[3] != '':
                dam = each[3]
            else:
                dam = ''
            #create an instance of a product object based on file 
            prod = Product(prodId=prodId, manu=manu, item=item, dam=dam)
            #add product to Product library 
            all_products.append(prod)


# Read PriceList file
    with open("PriceList.csv", 'r') as price_file:
        reader = csv.reader(price_file)
        #read through each line 
        for each in reader:
            priceId = each[0]
            prodPrice = each[1]
            #search through all products library 
            for prod in all_products:
                # if product ids match, add price attribute 
                if prod.prodId == priceId:
                    prod.price = prodPrice
                    break
                
                   

# Read ServiceDates file
    with open("ServiceDatesList.csv", 'r') as date_file:
        reader = csv.reader(date_file)
        for each in reader:
            prodID = each[0]
            serviceDate = each[1]
            # search through all products library
            for prod in all_products:
                # if product ids match, add servicedate attribute
                if prod.prodId == prodID:
                    prod.serviceDate = serviceDate



# Output Files

    # sort library by manu
    all_products.sort(key=lambda x: x.manu)
    with open("FullInventory.csv", 'w') as full:
        writer = csv.writer(full)
        for each in all_products:
            row = [each.prodId, each.manu, each.item, each.price, each.serviceDate, each.dam]
            writer.writerow(row)

    
    # set todays date 
    currentDate = datetime.today()
    with open("PastServiceDateInventory.csv", 'w') as service:
        writer = csv.writer(service)
        for each in all_products:
            #convert product date to string 
            service_date_str = str(each.serviceDate)
            #convert service date to a datetime object 
            service_date = datetime.strptime(service_date_str, "%m/%d/%Y")
            if currentDate > service_date:
                row = [each.prodId, each.manu, each.item, each.price, each.serviceDate, each.dam]
                writer.writerow(row)

    with open("DamagedInventory.csv", 'w') as damaged:
        writer = csv.writer(damaged)
        # search through product library
        for each in all_products:
            # write product to newfile if item is damaged
            if dam != " ":
                row = [each.prodId, each.manu, each.item, each.price, each.serviceDate]
                writer.writerow(row)

if __name__ == '__main__':
    main()
