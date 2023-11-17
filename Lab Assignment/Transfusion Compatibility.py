'''
Transfusion_compatibility.py -- Nguyen Hung Anh -- 09-11-2023
This program takes a donor and a recipients blodd type and outputs whether
or not Blood Donation is possible
'''

def transfusion(s_dbt, s_dRH, s_pbt, s_pRH):
    b_donorOm = s_dRH=='-' and s_dbt=='o'
    b_donorOp = s_dRH=='+' and s_dbt=='o' and s_pRH=='+'
    b_donorAp = s_dRH=='+' and s_dbt=='a' and s_pRH=='+' and (s_pbt=='ab' or s_pbt=='a')
    b_donorAm = s_dRH=='-' and s_dbt=='a' and (s_pbt=='AB' or s_pbt=='a')
    b_donorBp = s_dRH=='+' and s_dbt=='b' and s_pRH=='+' and (s_pbt=='ab' or s_pbt=='b')
    b_donorBm = s_dRH=='-' and s_dbt=='b' and (s_pbt=='AB' or s_pbt=='b')
    b_patientABm = s_pRH=='-' and s_pbt=='ab' and s_dRH=='-'
    b_patientABp = s_pRH=='+' and s_pbt=='ab'
    b_possible = (b_donorOm or b_donorOp or b_donorAp or b_donorAm 
                  or b_donorBp or b_donorBm
                  or b_patientABm or b_patientABp)
    return b_possible

def main():
    s_dbt =input("Donor's blood type: ")
    s_dRH =input("Donor's RH factor: ")
    s_pbt =input("Patient's blood type: ")
    s_pRH =input("Patient's RH factor: ")
    b_possible=transfusion(s_dbt, s_dRH, s_pbt, s_pRH)
    if b_possible==True:
        s_possible="Valid Donation"
    else:
        s_possible="Invalid Donation"
    print(s_possible)

if __name__ == "__main__":
    main()
