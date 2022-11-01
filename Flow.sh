#Flow

# 1: Rebin data
python rebin_data.py

# 2: Run IFT on GenApp (manually) > IFT folder

# 3: fit with nanodisc model (to rebinned and rescaled data)
cd model_19
python main_DMPC.py 
python main_POPC.py

# summarize refined params
cd ..
python table_results.py

# fit with micelle model (to rebinned and rescaled data)
cd model_11
python main_DMPC.py 
python main_POPC.py

# plot data
cd ..
python plot_all.py