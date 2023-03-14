import os
import pandas as pd
import matplotlib.pyplot as plt

##########################################################################################
# CODE DESCRIPTION
# 06_Plot_Climate_Rain_FR.py plots the climatology of rainfall events associated with flash floods.

# INPUT PARAMETERS DESCRIPTION
# Acc (number, in hours): accumulation to consider.
# EFFCI_list (list of integers, from 1 to 10): EFFCI indexes to consider.
# Max_Rain_Plot (positive integer, in mm): maximum rainfall values to plot.
# Max_Rain_Plot_Disc (positive integer, in mm): discretization for the rainfall values in the plot.
# MagnitudeInPerc_Rain_Event_FR_list (list of integers, from 0 to 100): magnitude, in 
#     percentile, of rainfall events that can potentially conduct to flash floods.
# MagnitudeInPerc_Rain_Event_FR_colours_list (list of strings): colours to assign to each magnitude
# RegionName_list (list of strings): names for the domain's regions.
# Git_repo (string): repository's local path.
# DirIN (string): relative path of the directory containing the the rainfall climatologies.
# DirOUT (string): relative path of the directory containing the plots of the rainfall climatology.

# INPUT PARAMETERS
Acc = 12
EFFCI_list = [1,6,10]
Max_Rain_Plot = 100
Max_Rain_Plot_Disc = 20
MagnitudeInPerc_Rain_Event_FR_list = [50, 75, 85, 90, 95, 98, 99]
MagnitudeInPerc_Rain_Event_FR_colours_list = ["orange", "lime", "purple", "cyan", "blue", "magenta", "red"]
RegionName_list = ["Costa","Sierra"]
Git_repo="/ec/vol/ecpoint/mofp/PhD/Papers2Write/FlashFloods_Ecuador"
DirIN = "Data/Compute/05_Climate_Rain_FR"
DirOUT = "Data/Plot/06_Climate_Rain_FR"
##########################################################################################

# Plotting the climatology of rainfall events associated with flash floods for a specific EFFCI index 
for EFFCI in EFFCI_list:

      # Plotting the climatology of rainfall events associated with flash floods for a specific region
      for RegionName in RegionName_list:

            print("Plotting the rainfall climatologies for EFFCI: " + str(EFFCI) + ", Region: " + RegionName)

            # Reading the rainfall climatology
            DirIN_temp = Git_repo + "/" + DirIN + "/" + f"{Acc:02d}" + "h/EFFCI" + f"{EFFCI:02d}"
            FileNameIN_temp = "Climate_Rain_FR_" + f"{Acc:02d}" + "h_EFFCI" + f"{EFFCI:02d}" + "_" +  RegionName + ".csv"
            climate_rain_FR_all = pd.read_csv(DirIN_temp + "/" + FileNameIN_temp)
            
            # Setting the figure for the plots 
            fig, ax = plt.subplots(figsize=(10, 8))

            # Selecting a specific magnitude, in percentile, of rainfall events that can potentially conduct to flash floods.
            for ind_magnitude in range(len(MagnitudeInPerc_Rain_Event_FR_list)):
                  
                  # Selecting the magnitudes to plot, and their correspondent colour in the plot
                  MagnitudeInPerc_Rain_Event_FR = MagnitudeInPerc_Rain_Event_FR_list[ind_magnitude]
                  MagnitudeInPerc_Rain_Event_FR_colours = MagnitudeInPerc_Rain_Event_FR_colours_list[ind_magnitude]

                  climate_rain_FR = climate_rain_FR_all["RainEvent_Magnitude_" + str(MagnitudeInPerc_Rain_Event_FR) + "th_Percentile"]
                  percentiles = climate_rain_FR_all["Climate_Percentiles"]
                  
                  # Plotting the rainfall climatology
                  ax.plot(climate_rain_FR, percentiles, color=MagnitudeInPerc_Rain_Event_FR_colours, linewidth=2)
            
            # Setting the plot metadata - Normal plot
            ax.plot([0,Max_Rain_Plot], [25, 25], "-", color="grey", linewidth=3)
            ax.set_title("Climatology of rainfall events associated with flash floods\n" + r"EFFCI>=" + str(EFFCI) + ", Region=" + RegionName, fontsize=20, pad=20)
            ax.set_xlabel("Rainfall [ mm/" + str(Acc) + "h ]", fontsize=18, labelpad=10)
            ax.set_ylabel("Percentiles [-]", fontsize=18, labelpad=10)
            ax.set_xlim([0,Max_Rain_Plot])
            ax.set_ylim([0,100])
            ax.set_xticks(range(0, Max_Rain_Plot + 1, Max_Rain_Plot_Disc))
            ax.set_yticks(range(0,101, 10))
            ax.xaxis.set_tick_params(labelsize=18)
            ax.yaxis.set_tick_params(labelsize=18)
            ax.grid()

            # Saving the plot
            DirOUT_temp = Git_repo + "/" + DirOUT + "/" + f"{Acc:02d}" + "h/EFFCI" + f"{EFFCI:02d}"
            FileNameOUT_temp = "Climate_Rain_FR_" + f"{Acc:02d}" + "h_EFFCI" + f"{EFFCI:02d}" + "_" +  RegionName + "_MaxRain" + str(Max_Rain_Plot) + ".jpeg"
            if not os.path.exists(DirOUT_temp):
                  os.makedirs(DirOUT_temp)
            plt.savefig(DirOUT_temp + "/" + FileNameOUT_temp)