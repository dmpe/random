library(data.table)

columns_to_use <- c(1:3,6, 7, 9,12:15,19:24,28:30,32,34,35,37)
a2500 <- seq(from = 1 , to = 400000, by =160)
b5000 <- seq(from = 1 , to = 400000, by =80)
c1000 <- seq(from = 1 , to = 400000, by =400)
d1500 <- seq(from = 1 , to = 400000, by =266)

Sys.setlocale("LC_ALL","English")

#before 
mt <- fread("xaa.csv")
mt <- mt[a2500,..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="UTC")
fwrite(mt, "5000 samples/before_sample_2500_a.csv", sep = ";", col.names = T)

#before 
mta <- fread("xab.csv")
mta <- mta[a2500,..columns_to_use]
mta$created_at <- as.POSIXct(mta$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="UTC")
fwrite(mta, "5000 samples/before_sample_2500_b.csv", sep = ";", col.names = F)

# during
mt_dur <- fread("xac.csv")
mt <- mt_dur[sample(.N, 5000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/during_sample_5000_a.csv", sep = ";", col.names = T, dateTimeAs = "write.csv")

mt <- mt_dur[sample(.N, 5000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/during_sample_5000_b.csv", sep = ";", dateTimeAs = "write.csv")

mt <- mt_dur[sample(.N, 5000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/during_sample_5000_c.csv", sep = ";", dateTimeAs = "write.csv")


# after
mt <- fread("xad.csv")
mt <- mt[d1500,..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/xad_sample_1500.csv", sep = ";", col.names = T, dateTimeAs = "write.csv")

mt <- fread("xae.csv")
mt <- mt[a2500,..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/xae_sample_2500.csv", sep = ";", col.names = F, dateTimeAs = "write.csv")

#mt <- fread("xaf.csv")
#mt <- mt[sample(.N, 1500),..columns_to_use]
#mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
#fwrite(mt, "5000 samples/xaf_sample_1500.csv", sep = ";", col.names = F, dateTimeAs = "write.csv")

mt <- fread("xag.csv")
mt <- mt[sample(.N, 1000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/xag_sample_1000.csv", sep = ";", col.names = F, dateTimeAs = "write.csv")

