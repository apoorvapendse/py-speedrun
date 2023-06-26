class Flower:
    totalFlowers = 0;
    totalPrice = 0;
    pricePerFlower = 100;
    def __init__(self,name,color) :
        self.name = name;
        self.color = color;
        Flower.totalFlowers+=1;
        Flower.totalPrice+=Flower.pricePerFlower
    @classmethod
    def changePrice(cls,amount):
        cls.pricePerFlower = amount
    def tellTotalPrice():
        print(Flower.totalPrice)

marigold = Flower('marigold',"yellow");
sunflower = Flower("sunflower","golden")

Flower.tellTotalPrice();
Flower.changePrice(300)
daisy = Flower("Daisy","Violet");
Flower.tellTotalPrice();

# classmethod is defined using @classmethod and makes use of one arguenment that represents that class
print(daisy.__dict__);

