from Building import Building
from  Calls_List import Calls_List


def main():
    #b = Building()
    b = Building("B2.json")
    print(b.elevators)

    #call = CallForElevator()
   # call.load_csv("Calls_a.csv")
   # print(call)

    call_l = Calls_List("Calls_a.csv")
    print(call_l.rows_list)








if __name__ == '__main__':
    main()
