library(data.table)

#before 
mt <- fread("xaa.csv")
mt <- mt[sample(.N, 2500)]
fwrite(mt, "before_sample_2500_a.csv", sep = ";")

#before 
mt <- fread("xab.csv")
mt <- mt[sample(.N, 2500)]
fwrite(mt, "before_sample_2500_b.csv", sep = ";")

# during
mt_dur <- fread("xac.csv")
mt <- mt_dur[sample(.N, 5000)]
fwrite(mt, "during_sample_5000_a.csv", sep = ";")

mt <- mt_dur[sample(.N, 5000)]
fwrite(mt, "during_sample_5000_b.csv", sep = ";")

mt <- mt_dur[sample(.N, 5000)]
fwrite(mt, "during_sample_5000_c.csv", sep = ";")


# after
mt <- fread("xad.csv")
mt <- mt[sample(.N, 1000)]
fwrite(mt, "xad_sample_1000.csv", sep = ";")

mt <- fread("xae.csv")
mt <- mt[sample(.N, 1000)]
fwrite(mt, "xae_sample_1000.csv", sep = ";")

mt <- fread("xaf.csv")
mt <- mt[sample(.N, 1500)]
fwrite(mt, "xaf_sample_2500.csv", sep = ";")

mt <- fread("xag.csv")
mt <- mt[sample(.N, 1500)]
fwrite(mt, "xag_sample_2500.csv", sep = ";")