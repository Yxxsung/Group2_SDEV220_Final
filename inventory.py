#This is meant to be the file that holds all the inventory information for the POS system


#this is the class item. Think of it as the term human meaning several different individuals.
class item:

    def __init__(self):

        self.name='empty'
        self.UPC=00000000
        self.itemqty=00

#this is a method meant to allow the user to update the intended item
    def update(self):

        choice= input("Hi, the item you are updating is", self.name, "would you like to update 1. UPC, 2. Description, or 3. QTY?")

        if choice == 1:

            self.UPC=input("please input the new UPC")

        elif choice == 2:

            self.name=input("please input the new item description")

        else:

            self.itemqty=input("please input the new item QTY")


#These are the different things the store sells, in other words the inventory
MtnDew_BajaBlast = item("MtnDew_BajaBlast",12000130274,35)
BioreCharMask = item("BioreCharMask",19100194304,22)
DoveAvdDrySham_VF = item("DoveAvdDrySham_VF",79400202444,12)
singleweek_pillCase = item("singleweek_pillCase",311917144955,25)
Jergans_ArganOil = item("Jergans_ArganOil",19100247680,14)
WhiteOut_Liq = item("WhiteOut_Liq",70330506060,22)
EZReach_BIC = item("EZReach_BIC",70330658721,37)
Chapstick_cherr = item("Chapstick_cherr",305730705516,19)
Febreze_PetOdor = item("Febreeze_PetOdor",37000787372,25)
SHanson_InstaDri_523 = item("SHanson_InstaDri_523",74170454246,15)
SHanson_InstaDri_573 = item("SHanson_InstaDri_573",74170454291,20)
BArmor_FPunch = item("BArmor_FPunch",858176002324,11)
MM_ChocBark_Easter = item("MM_ChocBark_Easter",13413232203,4)
