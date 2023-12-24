def calculate_cgpa(sgpa_list):
    total_sgpa = sum(sgpa_list)
    number_of_semesters = len(sgpa_list)
    
    if number_of_semesters == 0:
        return 0 
    
    cgpa = total_sgpa / number_of_semesters
    return cgpa

def main():
    n = int(input("Enter the number of semesters: "))
    
    sgpa_list = []
    for i in range(n):
        sgpa_list.append(float(input(f"Enter the SGPA for semester {i + 1}: ")))

    cgpa = calculate_cgpa(sgpa_list)
    print("CGPA = {:.2f}".format(cgpa))

if __name__ == "__main__":
    main()
