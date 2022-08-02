import matplotlib.pyplot as plt
def mainmenu():
    choice=0
    while choice !=6:
        print("\n***************************************")
print("\n***************************************")
print("                  COVID                 ")
print("***************************************")
print("      1. International Report ")
print("      2. National Report")
print("      3. COVID Zones")
print("      4. COVID Centres")
print("      5. Data visualisation")
print("                                     as per 27th august ")
choice= int(input("Choose any reports and its visualistuion"))
if choice==1:
    print("***************************************")
    print("         International Reports")
    print("***************************************")
    dq=pd.read_csv(r'D:\read\INTERNATIONAL REPORT.csv')
    print(dq)
    
elif choice==2:
    print("***************************************")
    print("           Nation Reports ")
    print("***************************************")
    df=pd.read_csv (r'D:\read\NATIONAL REPORT.csv')
    print(df)
elif choice==3:
    print("***************************************")
    print("             COVID zones")
    print("***************************************")
    db=pd.read_csv(r'D:\read\CSVCOVIDZONES.csv')
    print(db)
elif choice==4:
    print("***************************************")
    print("         Testing laboratories")
    print("***************************************")
    da=pd.read_csv(r'D:\read\testing centres for covid.csv')
    print(da)
elif choice==5:
    print("----------------------------------------")
    print("          DATA VISUALISATION")
    print("----------------------------------------")
    print("         1. International Reports ")
    print("         2. National Report    ")
    print("         3. Maharastra Report")
    print("         4. India's COVID Zones Percentage")
    print("         5. Testing laboratories")
    ch2= int(input("CHOOSE THE OPTOIN TO SEE DATA VISUALISATION"))
    if ch2==1:
        #create data plot
        n_groups = 10
        means_Cases = (6051431, 3764493, 3403555, 980405, 621997, 618286, 582022, 579914, 451792, 404102)
        means_deaths = (184967, 118726, 61857, 16914, 28277, 13628, 18468, 22594, 28996, 11072)
        means_recovered = (3348934, 2974725, 2596273, 798466, 429662, 531338, 417793, 400479, 0000, 377922)
        
        #create plot
        fig, ax=plt.subplots()
        index=np.arange(n_groups)
        bar_width=0.25
        opacity=0.99
        
        rect1=plt.bar(index, means_Cases, bar_width, alpha=opacity, color="b", label="Total Cases")
        
        rect2=plt.bar(index+bar_width, means_deaths, bar_width, alpha=opacity, color="r", label="Total deaths")
        
        rect3=plt.bar(index+0.50, means_recovered, bar_width, alpha=opacity, color="g", label="Total recovered")
        
        plt.xlabel("COUNTRY")
        plt.ylabel("NO of people")
        plt.title("International Report")
        plt.xticks(index + bar_width, ("USA", "BRAZIL", "INDIA", "RUSSIA", "PERU", "SOUTH AFRICA", "COLOMBIA", "MEXICO", "SPAIN", "CHILE"))
        plt.legend()
        
        plt.tight_layout()
        plt.show
    elif ch2==2:
        n_groups=52
        means_Cases=(719000, 397000, 393000, 300000, 203000, 166000, 148000, 127000, 124000, 114000, 96771, 91000, 90986, 84524, 74670, 68789, 66761, 58005, 56864, 47935, 3376, 47000, 34480, 33133, 33046, 30845, 28142, 24550, 19611, 16656, 16549, 15027, 14077, 0, 246, 399, 387, 436, 461, 449, 555, 580, 921, 920, 898, 865,  1022, 967, 1047, 1719, 2268, 2857)
        means_deaths=(23089, 6839, 3633, 5091, 3149, 4347, 2964, 530, 2564, 788, 274, 2900, 448, 4899, 992, 0, 276, 634, 1282, 1270, 41, 1200, 6567, 369, 362, 1700, 872, 231, 612, 200, 219, 165, 81, 0, 5, 24, 7, 11, 2, 14, 19, 15, 15, 12, 14, 31, 42, 0, 7, 15, 102, 149)
        means_recovered=(522000,338000, 295000, 212000, 149000, 148000, 118000, 106000, 109000, 86095, 76952, 73475, 62813, 55884, 59579, 0, 43757, 43256, 47659, 18156, 1796, 30966, 26093, 23189, 22349, 0, 13406, 14145, 0, 8994, 11524, 11511, 8542, 0, 172, 0, 192, 192, 250, 344, 375, 518, 357, 732, 572, 612, 782, 473, 461, 1200, 1800,2200)
        
        
        fig, ax=plt.subplots()
        index=np.arange(n_groups)
        bar_width=0.25
        opacity=0.99
        
        
        rect1=plt.bar(index, means_Cases, bar_width,  alpha=opacity, color="b", label="Total Cases")
        
        rect2=plt.bar(index+bar_width, means_deaths, bar_width, alpha=opacity, color="r", label="Total deaths")
        
        rect3=plt.bar(index+0.50, means_recovered, bar_width, alpha=opacity, color="g", label="Total recovered")
        
        
        plt.xlabel("STATES")
        plt.ylabel("NO. OF PEOPLE")
        plt.title("National Report")
        plt.xticks(index+bar_width, ("Maha", "T N", "Andh P","Karna", "UP", "DELHI", "WB", "Bihar", "Chenn", "Telag", "Assam", "Guj", "Odhis", "Mumbai", "Rajas", "Kolka", "Keral", "MP", "Thane", "Chandi", "Punjab", "J&K", "Chittor", "Jhar", "Ahem", "Pune", "Chattis", "Surat", "Luck", "Uttra", "Goa", "Tiruvan", "Laksav", "Sind", "Aravli", "Ranchi", "Snghli", "Aurang", "Ajmer", "Kota", "Ahmed", "Kheda", "Kolap", "Fatheh", "Ratna", "Firoza","Mizoram", "Naga", "Agra", "Jaipur"))
        plt.legend()
        plt.tight_layout()
        plt.show
    elif ch2==3:
        n_groups=10
        means_Cases = ( 84524, 47935, 28142, 399, 436, 461, 920, 1719, 580, 865)
        means_Recovered = ( 55884, 18156, 13406, 0, 192, 251, 732, 1200, 518, 612)
        means_Deaths = (4899, 1270, 872, 24, 11, 2, 12, 15, 15, 31)
        
        fig, ax=plt.subplots()
        index=np.arange(n_groups)
        bar_width=0.25
        opacity=0.99
        
        rect1=plt.bar(index, means_Cases, bar_width, alpha=opacity, color="b", label="Total Cases")
        
        rect2=plt.bar(index+bar_width, means_Recovered, bar_width, alpha=opacity, color="g", label="Total recovered")
        
        rect3=plt.bar(index+0.50, means_Deaths, bar_width, alpha=opacity, color="r", label="Total deaths")
        
        plt.xlabel("DISTRICT")
        plt.ylabel("NO of people")
        plt.title("Maharastra Report")
        plt.xticks(index + bar_width, ("Mumbai", "Thane", "Pune", "Aravali", "Sanghli", "Aurangabad", "Kolahpur", "Nagpur", "Ahmedhnagar"))
        plt.legend()
        
        plt.tight_layout()
        plt.show
    elif ch2==4:
        zones = ["Red Zone", "Orange Zone", "Yellow Zone", "Green Zone"] 
  
        data = [2, 13, 38, 50] 
  
  
# Creating explode data 
        explode = (0.0, 0.0, 0.0, 0.0) 
  
# Creating color parameters 
        colors = ( "red", "orange", "yellow", 
          "green" ) 
  
# Wedge properties 
        wp = { 'linewidth' : 1, 'edgecolor' : "green" } 
  
# Creating autocpt arguments 
        def func(pct, allvalues): 
            absolute = int(pct / 100.*np.sum(allvalues))
            return "{:.1f}%\n({:d} )".format(pct, absolute)
        fig, ax = plt.subplots(figsize =(10, 7)) 
        wedges, texts, autotexts = ax.pie(data,
                                          autopct = lambda pct: func(pct, data),
                                          explode = explode,  
                                          labels = zones, 
                                          shadow = True, 
                                          colors = colors, 
                                          startangle = 90, 
                                          wedgeprops = wp, 
                                          textprops = dict(color ="magenta"))
        ax.legend(wedges, zones,
                  title ="Zone", 
                  loc ="center left", 
                  bbox_to_anchor =(1, 0, 0.5, 1))
        plt.setp(autotexts, size = 8, weight ="bold")
        ax.set_title("India's COVID-19 Zone Percentage")
        plt.show
    elif ch2==5:
        n_groups = 36
        means_Government = (121, 77, 76, 73, 63, 49, 47, 44, 41, 34, 33, 32, 29, 27, 23, 22, 22, 20, 18, 18, 17, 14, 14, 13, 11, 7, 6, 5, 4, 4, 3, 3, 2, 2, 2, 1)
        means_Private = (48, 69, 13, 10, 76, 24, 61, 6, 7, 26, 9, 5, 41, 13, 3, 43, 0, 2, 3, 14, 32, 0, 11, 0, 1, 3, 1, 4, 0, 0, 1, 0, 0, 0, 0, 0)
        
        #create plot
        fig, ax=plt.subplots()
        index=np.arange(n_groups)
        bar_width=0.25
        opacity=0.99
        
        rect1=plt.bar(index, means_Government, bar_width, alpha=opacity, color="b", label="Total Government Laborataries")
        
        rect2=plt.bar(index+bar_width, means_Private, bar_width, alpha=opacity, color="r", label="Total Private Laborataries")
        
        plt.xlabel("STATES , CITIES AND ISLAND")
        plt.ylabel("NO of Laborataries")
        plt.title("COVID Centres")
        plt.xticks(index + bar_width, ("UP", "Maha", "MP", "AP", "TN", "WB", "KAR", "BIH", "ODI", "GUJ", "PUN", "JHA", "KER", "RAJ", "J&K", "DEL", "HP", "UK", "CHA", "HAR", "TEL", "NAG", "ASS", "ARU", "MEG", "MAN", "GOA", "PUD", "TRI", "A&N", "CHA", "LAD", "MIZ", "LAK", "SIK", "D&N"))
        plt.legend()
        
        plt.tight_layout()
        plt.show
        
    else:
        print("wrong option run the file again")
else:
    print("not valid run the file agin")
       
        







