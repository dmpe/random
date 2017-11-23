library(data.table)

columns_to_use <- c(1:3,6, 7, 9,12:15,19:24,28:30,32,34,35,37)

#before 
mt <- fread("xaa.csv")
mt <- mt[sample(.N, 2500),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="UTC")
fwrite(mt, "5000 samples/before_sample_2500_a.csv", sep = ";", col.names = T)

#before 
mt <- fread("xab.csv")
mt <- mt[sample(.N, 2500),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="UTC")
fwrite(mt, "5000 samples/before_sample_2500_b.csv", sep = ";", col.names = T)

# during
mt_dur <- fread("xac.csv")
mt <- mt_dur[sample(.N, 5000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="UTC")
fwrite(mt, "5000 samples/during_sample_5000_a.csv", sep = ";")

mt <- mt_dur[sample(.N, 5000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="UTC")
fwrite(mt, "5000 samples/during_sample_5000_b.csv", sep = ";")

mt <- mt_dur[sample(.N, 5000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="UTC")
fwrite(mt, "5000 samples/during_sample_5000_c.csv", sep = ";")


# after
mt <- fread("xad.csv")
mt <- mt[sample(.N, 1000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="UTC")
fwrite(mt, "5000 samples/xad_sample_1000.csv", sep = ";")

mt <- fread("xae.csv")
mt <- mt[sample(.N, 1000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="UTC")
fwrite(mt, "5000 samples/xae_sample_1000.csv", sep = ";")

mt <- fread("xaf.csv")
mt <- mt[sample(.N, 1500),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="UTC")
fwrite(mt, "5000 samples/xaf_sample_2500.csv", sep = ";")

mt <- fread("xag.csv")
mt <- mt[sample(.N, 1500),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="UTC")
fwrite(mt, "5000 samples/xag_sample_2500.csv", sep = ";")