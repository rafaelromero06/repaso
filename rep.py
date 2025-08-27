class F:
    def read(self,filename):
        with open(filename,"r", encoding ="utf-8") as f:
            for linea in f:
                print(linea.strip())

    def write(self,filename,dictionary):
        enable = 1
        id=1
        with open(filename, "w", encoding="utf-8") as f:
            labels = list(dictionary.keys())
            for label in labels:
                f.write(label + ",")
            f.write("status "+"\n")
            for a in dictionary:
                list(a.keys)
                count=0
                f.write(str(id))
                for d in a.values():
                    f.write(d)
                    count +=1
                    f.write(",")
                id+=1
                f.write(str(enable)+"\n")

    def delete(self,filename,id):
        list=[]
        with open(filename, "r", encoding="utf-8") as f:
            list = f.readlines()
        for l in list:
            arr =l.split(",")
            if str(arr[0]==str(id)):
                print(id)
            else:
                newlist.append()


f = F()
people