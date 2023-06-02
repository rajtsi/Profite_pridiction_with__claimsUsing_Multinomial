 import random
 import matplotlib.pyplot as plt 
 from scipy.stats import multinomial   
    
 print(" Pridiction of profite of an Mediacl Insurance providing company")
 mc = int(input('Number of time you want to run simulation?\n'))   
    #Change Terms for changing duration
    # Change customers value to change number of customers
    # Range of Sum Insured is between 4 lacks to 6 lacks
    # premium for now hab been set between 4 to 6 Thousands
    # And risk free interest rate had been set between 4-6 generaly FD use to have 6 to 7.5 interest rate.
 
 term = 10
 customers = 100000
 sumInsured = random.randint(400000, 600000)
 premium = random.randint(4000, 6000)
 rate = random.uniform(4, 6)    
 
 
 #Lets assume some money amount that will be claim by by these categories patients 
    
 #'High Blood Pressure'= prize_1
 # 'Cataract'= prize_2
 # 'Heart Diseases'= prize_3 
 #'Cancer'= prize_4 
 #'Diabetes'= prize_5
 # 'COVID-19'= prize_6 
 #'HIV/AIDS'= prize_7
 #'Critical Illnesses'= prize_8
    
 prize_1=0.6*sumInsured  
 prize_2=0.5*sumInsured 
 prize_3=1*sumInsured 
 prize_4=1*sumInsured 
 prize_5=0.8*sumInsured 
 prize_6=0.5*sumInsured 
 prize_7=1*sumInsured 
 prize_8=0.4*sumInsured
  

 prize=[prize_1,prize_2,prize_3,prize_4,prize_5,prize_6,prize_7,prize_8]
    
    
    
    
 x=[]
 y=[]   
 for i in range(1,term+1):
     x.append(i)
     #y.append(0)
     #print(i)
    
 #randomly generating number of claims asked for each time simulation runs
 def randomClaim():
    claim = []
    for i in range(term):
        claim.append(random.randint(0, customers))
    return claim
 
  # Estimated probabilities for each disease category and will be used in finding number of peoples 
  # in different claim categories  in function estimate_claim_counts
 def generate_random_probabilities(num_categories):
    probabilities = np.random.rand(num_categories)
    probabilities /= np.sum(probabilities)  # Normalize to ensure sum is 1
    return probabilities   

 
      
#The estimate_claim_counts function you provided estimates the number of claims for each disease category 
#based on the total number of claiming customers and the probabilities of claiming for each category. 
#It uses the multinomial.rvs function from the scipy.stats module to generate random samples from the multinomial distribution.
 
 def estimate_claim_counts(t_claming_customers, probabilities):
    categories = ['High Blood Pressure', 'Cataract', 'Heart Diseases', 'Cancer', 'Diabetes', 'COVID-19', 'HIV/AIDS', 'Critical Illnesses']
    claims = multinomial.rvs(n=t_claming_customers, p=probabilities)
    return claims
    
 
    
 # function accept number of time similation is to be done as mc and then

 def profit():
    net_profit = []
    randomclaim_list=randomClaim()
    
    p=0
    for loop in randomclaim_list:
     claimed_people=estimate_claim_counts(loop, probabilities) 
     amount_claimed=0
     for prize_i,i_claim in zip(prize,claimed_people):
           amount_claimed+=prize_i*i_claim 
            
     p=(p*((1+rate)/100) + sumInsured*customers -amount_claimed)
     net_profit.append(p)
    return net_profit 

 dummy=[0,0,0,0,0,0,0,0]   
 for i in range(mc):
    y = profit()
    if(y[-1]>=dummy[-1]):
     dummy.clear()
     dummy.extend(y)
    plt.plot(x,y)

# here again by copping dummy into y and highled by black to maximum profitable way     
 y=dummy
 plt.plot(x, y, color='black')
# Leveled the graph with max profite where leveling contain Input values and etc. 
 plt.text(x[-1], y[-1],f'("sumInsured={sumInsured} premium={premium}", "Risk free rate={rate} Profite after{term} years={y[-1]}Rs")', ha='center', va='bottom',color='red')
 
 plt.xlabel("term in years")
 plt.ylabel("net profit")
 plt.title("Profit visualization for Term Insuance with sum insured %d" %(sumInsured))
 #max_profit = max(profit(i))
 #plt.ylim(0, 1e9)

 plt.show()
    




    
 
 
