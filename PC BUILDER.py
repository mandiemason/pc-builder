# Mandie Mason - Final - Part 3

# Declarations
buildPc = ""
rebuildPc = ""
START = "yes"
QUIT = "no"
REPEAT = "yes"

arrows = "\u00BB"
dots = "\u00b7"
long_line = "\u2500"
custom_lotus = "𖥸"
circle_bullet = "\u274D"

usages = ["gaming", "streaming", "work", "general use", "1", "2", "3", "4"]
budgets = ["1", "2", "3", "4", "5"]

cpu_brands = ["Intel", "AMD", "intel", "amd"]

intel_cpu_options = {
    "1": "Intel Core i5-12400F",
    "2": "Intel Core i5-14600K",
    "3": "Intel Core i7-14700K",
    "4": "Intel Core i9-14900K",
    "5": "Intel Core i9-14900K"
}

amd_cpu_options = {
    "1": "AMD Ryzen 5 4500",
    "2": "AMD Ryzen 5 5600X",
    "3": "AMD Ryzen 7 5800X",
    "4": "AMD Ryzen 9 5900X",
    "5": "AMD Ryzen 9 5950X"
}

motherboard_options = ["ASUS Prime B550-PLUS", "MSI B550 GAMING GEN3"]

intel_ram_options = {
    "1": "G.SKILL Ripjaws V Series 32GB (2 x 16GB)",
    "2": "CORSAIR Vengeance RGB 32GB (2 x 16GB)",
    "3": "G.SKILL Trident Z5 RGB Series 64GB (2 x 32GB)",
    "4": "G.SKILL Trident Z5 RGB Series 64GB (2 x 32GB)",
    "5": "G.SKILL Trident Z5 RGB Series 64GB (2 x 32GB"
}

amd_ram_options = {
    "1": "CORSAIR Vengeance RGB Pro 32GB (2 x 16GB)",
    "2": "G.SKILL Trident Z5 RGB Series 32GB (2 x 16GB)",
    "3": "G.SKILL Trident Z5 RGB Series 32GB (2 x 16GB)",
    "4": "G.SKILL Trident Z5 RGB Series 64GB (2 x 32GB)",
    "5": "G.SKILL Trident Z5 RGB Series 64GB (2 x 32GB)"
}

intel_gpu_options = {
    "1": "MSI Ventus GeForce RTX 4060 8GB DDR6",
    "2": "GIGABYTE WINDFORCE GeForce RTX 4070 12GB DDR6)",
    "3": "ASUS Dual GeForce RTX 4070 Super 12GB DDR6",
    "4": "ASUS Dual GeForce RTX 4070 Super 12GB DDR6",
    "5": "GIGABYTE Gaming GeForceRTX 4090 24GB DDR6"
}

amd_gpu_options = {
    "1": "MSI Ventus GeForce RTX 3060 12GB DDR6",
    "2": "GIGABYTE Radeon RX 7800 XT 16GB DDR6",
    "3": "SAPPHIRE PULSE Radeon RX 7900 XT 20GB DDR6",
    "4": "ASUS TUF NVIDIA GeForce RTX 4070 Ti Super DDR6",
    "5": "GIGABYTE Gaming GeForceRTX 4090 24GB DDR6"
}

intel_case_options = {
    "1": "Fractal Design Focus G Black ATX Mid Tower",
    "2": "Corsair 4000D Black ATX Mid Tower",
    "3": "Fractal Design Pop XL Air RGB Black ATX Mid Tower",
    "4": "Fractal Design Pop XL Air RGB Black ATX Mid Tower",
    "5": "Fractal Design Pop XL Air RGB Black ATX Mid Tower"
}

amd_case_options = {
    "1": "DIYPC Rainbow Flash-F1-B",
    "2": "Montech Sky Two Black ATX Mid Tower",
    "3": "Montech Sky Two Black ATX Mid Tower",
    "4": "Fractal Design North Black ATX mATX Mid Tower",
    "5": "Corsair 4000D Airflow Black ATX Mid Tower"
}

intel_power_options = {
    "1": "Thermaltake Smart Series 700W",
    "2": "CORSAIR RM750e",
    "3": "CORSAIR RM1000e",
    "4": "CORSAIR RM1000e",
    "5": "CORSAIR RM1000e"
}

amd_power_options = {
    "1": "MSI MAG A650BN 650W",
    "2": "Thermaltake GF1 850W",
    "3": "MSI MAG A850GL PCIE 5.0",
    "4": "CORSAIR RM1000e",
    "5": "CORSAIR RM1000e"
}

intel_storage_options = {
    "1": "Kinston NV2 M.2 2280 1TB",
    "2": "SAMSUNG 970 EVO PLUS SSD NVMe M.2 1TB",
    "3": "SAMSUNG 980 PRO SSD NVMe M.2 1TB",
    "4": "SAMSUNG 980 PRO SSD NVMe M.2 2TB",
    "5": "SAMSUNG 980 PRO SSD NVMe M.2 2TB"
}

amd_storage_options = {
    "1": "Western Digital WD_BLACK SN770 SSD M.2 1TB",
    "2": "Kingston NV2 SSD M.2 1TB",
    "3": "Team Group MP33 SSD NVMe M.2 1TB",
    "4": "Western Digital WD_BLACK SN850X SSD NVMe M.2 2TB",
    "5": "Western Digital WD_BLACK SN770 SSD M.2 2TB"
}

intel_cooler_options = {
	"1": "Pure Rock 2 CPU Air Cooler",
    "2": "DeepCool AK620 High-Performance CPU Cooler",
    "3": "Corsair H100x RGB ELITE Liquid CPU Cooler",
    "4": "DeepCool LT720 Premium Liquid CPU Cooler",
    "5": "DeepCool LT720 Premium Liquid CPU Cooler"
}

amd_cooler_options = {
	"1": "Pure Rock 2 CPU Air Cooler",
    "2": "DeepCool AG400 BK ARGB CPU Cooler",
    "3": "DeepCool AG400 BK ARGB CPU Cooler",
    "4": "DeepCool AK620 ZERO DARK High-Performance CPU Cooler",
    "5": "DeepCool AK620 High-Performance CPU Cooler"
}

# introduction / start or quit
while True:
    print("")
    print(dots * 2, long_line * 8, dots, custom_lotus, dots, long_line * 8, dots * 2)   # prints decorative partition
    print("Welcome to Mandie's PC Builder!")
    print("Would you like to build a PC based on your budget and requirements?")
    print("")
    print("Enter", START, "to begin or", QUIT, "to quit using PC Builder.")

    buildPc = input()       # gathers user input
    if buildPc.lower() == START:    # checks input
        print("")
        print("Great! Let's get started building your perfect PC!")
        break       # continues to next part
    elif buildPc.lower() == QUIT:
        print("")
        print("Well that's a shame. Goodbye!")
        exit()      # exits program
    else:
        print("Invalid input. Please only enter 'Yes' or 'No'.")
    continue

# use of PC
while True:
    print("")
    print("")
    print(dots * 2, long_line * 8, dots, custom_lotus, dots, long_line * 8, dots * 2)
    print("What do you primarily want to use your PC for?")
    print("1. Gaming")
    print("2. Streaming")
    print("3. Work")
    print("4. General use")
    print("")

    usage = input("Enter your usage here: ").lower()    # converts input to lowercase
    if usage in usages:
        print("Great!")
        break
    else:
        if usage not in usages:
            print("")
            print("Invalid usage. Please try again.")
        continue

# budget of PC
while True:
    print("")
    print("")
    print(dots * 2, long_line * 8, dots, custom_lotus, dots, long_line * 8, dots * 2)
    print("Now, what is your preferred budget?")
    print("1. Budget: Under $1,000")
    print("2. Low-end: $1,000 - $1,500")
    print("3. Mid-range: $1,501 - $2,000")
    print("4. High-end: $2,001 - $2,500")
    print("5. Premium: Over $2,500")
    print("")

    budget = input("Enter your budget here: ").lower()      # converts input to lowercase
    if budget in budgets:
        print("Got it!")
        break
    else:
        if budget not in budgets:
            print("")
            print("Invalid budget. Please try again.")
        continue

# Processor Choice
while True:
    print("")
    print("")
    print(dots * 2, long_line * 8, dots, custom_lotus, dots, long_line * 8, dots * 2)
    print("One more thing before I give you a PC build that fits your preferences...")
    print("")
    print("What processor brand do you prefer for your CPU? Intel or AMD?")
    print("1. Intel")
    print("2. AMD")
    print("")
    print("")
    print(dots * 2, long_line * 8, dots, custom_lotus, dots, long_line * 8, dots * 2)
    print("If you are unsure, please note that each brand has their pros and cons.")
    print("The best processor for you depends on your:")
    print(arrows + " Budget: ")
    print("    - Intel can cost less than AMD, but it can consume more power.")
    print(arrows + " How you will be using your PC: ")
    print("    - Both are fantastic for gaming, but AMD may be overkill if your main use is general browsing/use.")
    print("")
    print("")
    print(dots * 2, long_line * 8, dots, custom_lotus, dots, long_line * 8, dots * 2)

    cpu_brand_choice = input("With that being said, enter your choice here: ").lower()
    if cpu_brand_choice.lower() in cpu_brands:  # checks if input is a valid option
        print("Great choice!")
        break
    else:
        if cpu_brand_choice.lower() not in cpu_brands:  # if not valid, gives error message and asks again
            print("Invalid entry. Please try again.")


while True:
    if cpu_brand_choice == "intel":
        selected_cpu = intel_cpu_options[budget]    # selects a part based on cpu selection and budget
        break
    else:
        if cpu_brand_choice == "amd":
            selected_cpu = amd_cpu_options[budget]
            break

# Part Select
while True:
    if cpu_brand_choice == "intel":
            selected_motherboard = motherboard_options[0]   # selects a part based on cpu selection
            break
    else:
        if cpu_brand_choice == "amd":
            selected_motherboard = motherboard_options[1]
            break


while True:
    if cpu_brand_choice == "intel":
        selected_ram = intel_ram_options[budget]    # selects a part based on cpu selection and budget
        break
    else:
        if cpu_brand_choice == "amd":
            selected_ram = amd_ram_options[budget]
            break


while True:
    if cpu_brand_choice == "intel":
        selected_gpu = intel_gpu_options[budget]    # selects a part based on cpu selection and budget
        break
    else:
        if cpu_brand_choice == "amd":
            selected_gpu = amd_gpu_options[budget]
            break


while True:
    if cpu_brand_choice == "intel":
        selected_case = intel_case_options[budget]  # selects a part based on cpu selection and budget
        break
    else:
        if cpu_brand_choice == "amd":
            selected_case = amd_case_options[budget]
            break


while True:
    if cpu_brand_choice == "intel":
        selected_power = intel_power_options[budget]    # selects a part based on cpu selection and budget
        break
    else:
        if cpu_brand_choice == "amd":
            selected_power = amd_power_options[budget]
            break

while True:
    if cpu_brand_choice == "intel":
        selected_storage = intel_storage_options[budget]    # selects a part based on cpu selection and budget
        break
    else:
        if cpu_brand_choice == "amd":
            selected_storage = amd_storage_options[budget]
            break

while True:
    if cpu_brand_choice == "intel":
        selected_cooler = intel_cooler_options[budget]  # selects a part based on cpu selection and budget
        break
    else:
        if cpu_brand_choice == "amd":
            selected_cooler = amd_cooler_options[budget]
            break

# prints all the selected parts in a neat list with fancy bullet points
# Part Reveal
while True:
    print("")
    print("")
    print(dots * 2, long_line * 8, dots, custom_lotus, dots, long_line * 8, dots * 2)
    print("It's time for the moment you've been waiting for!")
    print("")
    print("Based on what you've entered, your ideal PC will include the following hardware:")
    print(circle_bullet + " CPU: ", selected_cpu)
    print(circle_bullet + " Motherboard: ", selected_motherboard)
    print(circle_bullet + " RAM (Memory): ", selected_ram)
    print(circle_bullet + " GPU: ", selected_gpu)
    print(circle_bullet + " Case: ", selected_case)
    print(circle_bullet + " Power Supply: ", selected_power)
    print(circle_bullet + " Storage: ", selected_storage)
    print(circle_bullet + " CPU Cooler: ", selected_cooler)
    break

# asks user if they want to build again or quit
# repeat and store
while True:
    print("")
    print("")
    print(dots * 2, long_line * 8, dots, custom_lotus, dots, long_line * 8, dots * 2)
    print("Would you like to build another PC?")
    print("Enter", START, "to store your build and restart or", QUIT, "to quit using PC Builder.")

    rebuildPc = input()
    if rebuildPc.lower() == START:     # checks input, prints a storing message, and stores build into StoredBuilds.txt
        print("")
        print("Storing your build...")

        fout = open("StoredBuilds.txt", "a")    # "a" appends file instead of write so that when restarted the info stays
        line1 = " CPU: " + selected_cpu + "\n"  # sets line to specified part
        fout.write(line1)                       # writes line in file

        line2 = " Motherboard: " + selected_motherboard + "\n"
        fout.write(line2)

        line3 = " RAM (Memory): " + selected_ram + "\n"
        fout.write(line3)

        line4 = " GPU: " + selected_gpu + "\n"
        fout.write(line4)

        line5 = " Case: " + selected_case + "\n"
        fout.write(line5)

        line6 = " Power Supply: " + selected_power + "\n"
        fout.write(line6)

        line7 = " Storage: " + selected_storage + "\n"
        fout.write(line7)

        line8 = " CPU Cooler: " + selected_cooler + "\n"
        fout.write(line8)

        line9 = "    \n"    # prints blank lines after first pc is entered into file
        fout.write(line9)

        line10 = "    \n"
        fout.write(line10)
        break

    #exit
    elif rebuildPc.lower() == QUIT:     # checks input, prints a goodbye message, and ends
        print("")
        print(dots * 2, long_line * 8, dots, custom_lotus, dots, long_line * 8, dots * 2)
        print("Thanks for using PC Builder! Goodbye!")
        break