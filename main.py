from mendeleev import element
compound = input('enter a binary compound (e.g. H2O) ')

vsepr_shapes = {
    (1, 0): "linear",
    (2, 0): "linear",
    (2, 1): "bent",
    (2, 2): "bent",
    (3, 1): "trigonal pyramidal",
    (3, 0): "trigonal planar",
    (4, 0): "tetrahedral",
    (5, 0): "trigonal bipyramidal",
    (6, 0): "octahedral"
}
def get_compound(compound):
    arr = list(compound)
    elms = [] #stores the different atoms 
    nums = [] #stores the respective quantity of these atoms
    #adds '1' to specify number of atoms where not specified
    for i in range(len(arr) - 1):
        if (arr[i].islower() or arr[i].isupper()) and arr[i + 1].isupper():
            arr.insert(i + 1, '1')
    
    if arr[-1].isupper() or arr[-1].islower():
        arr.append('1') 
    #concatenates lowercase letters to the previous uppercase letter for 2-letter long element symbols
    j = 0
    while j < len(arr):
        if arr[j].islower():
            arr[j-1] += arr[j]
            arr.pop(j)
            j -= 1
        j += 1

    for i in range(0, len(arr), 2):
        elms.append(arr[i])
        nums.append(arr[i+1])
    nums = [int(s) for s in nums]
    total = []
    total.append(elms)
    total.append(nums)
    return(total)


def find_total_valence(elms, nums):
    val = [] #stores the number of valence electrons for each element
    num = len(elms)
    for i in range(num):
        a = element(elms[i])
        val.append(a.nvalence())
    # calculates the total number of valence electrons for the compound   
    totalval = 0
    for i in range(num):
        totalval += val[i] * nums[i]
    return(totalval, num)

arr = get_compound(compound)
elms = arr[0]
nums = arr[1]


totalval, num = find_total_valence(elms, nums)
en = []
#chooses central atom based on electronegativity
for i in range(num):
    a = element(elms[i])
    en.append(a.electronegativity_pauling())
    
center = elms[en.index(min(en))]
#changes central atom if current central atom is hydrogen(exception to electronegativity rule)
if center == "H":
    f = en
    f[elms.index("H")] = 10
    center = elms[f.index(min(f))]

totalelms = []
for i in range(num):
    for j in range(nums[i]):
        totalelms.append(elms[i])

valence = [0] * len(totalelms) #stores the number of valence electrons wanted by each atom
for i in range(len(totalelms)):
    if totalelms[i] == "H":
        valence[i] = 2
    else:
        valence[i] = 8
totalelms.remove(center)
centern = 8
valence.remove(8) #removes the central atom
nbonds = len(valence)

for i in range(len(valence)):
    valence[i] -= 2

lone = int((totalval - 2*nbonds - sum(valence))/2)
# calculates the number of polar and nonpolar bonds
polar_bonds = 0
nonpolar_bonds = 0
center_en = element(center).electronegativity_pauling()
for elm in totalelms:
    elm1_en = element(elm).electronegativity_pauling()
    if abs(elm1_en - center_en) > 0.4:
        polar_bonds += 1
    else:
        nonpolar_bonds += 1

print(f"compound given: {compound}")       
print(f"total valence electrons: {totalval}")
print(f"central atom: {element(center).name}")
print(f"shared electron domains: {nbonds}")
print(f"lone pairs: {lone}")
print(f"shape: {vsepr_shapes[(nbonds, lone)]}")
print(f"polar bonds: {polar_bonds}")
print(f"nonpolar bonds: {nonpolar_bonds}")