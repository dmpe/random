library(data.table)
library(openxlsx)
library(jsonlite)

###############################
#awd <- stream_in(file("C:/Users/jm/Music/xaa.jsonl",open="r"), verbose=T)
#nrow(awd)
#out <- lapply(readLines("C:/Users/jm/Music/xaa.jsonl"), fromJSON)
#connn <- file("C:/Users/jm/Music/xaa.jsonl")
#test <- readLines(con = connn)
#lapply(test, fromJSON)
###############################


###############################
# This file needs to be considered as an example. 
# Here, it reads the WHOLE 250MB CSV file and only then creates the sample with pre-processing steps
# Another approach is to use shuf bash command and load already much smaller file that would be processed.
###############################

# pics only necessary columns that are worth the information
columns_to_use <- c(1:3,6, 7, 9,12:16,19:24,28:30,32,34,35,37)
a2500 <- seq(from = 1 , to = 400000, by =160)
b5000 <- seq(from = 1 , to = 400000, by =80)
c1000 <- seq(from = 1 , to = 400000, by =400)
d1500 <- seq(from = 1 , to = 400000, by =266)

Sys.setlocale("LC_ALL","English")

# before A + B
mt <- fread("xaa.csv") # loads the whole 250 MB file
mt <- mt[a2500,..columns_to_use] # essentially a subset
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST") # prepare time to have GMT+1
fwrite(mt, "5000 samples/before_sample_2500_a.csv", sep = ";", col.names = T, dateTimeAs = "write.csv") # write the sample in CSV
#openxlsx::write.xlsx(mrrrr, "5000 samples/before_sample_2500_a.xlsx", colNames = T, asTable =T)

mta <- fread("xab.csv")
mta <- mta[a2500,..columns_to_use]
mta$created_at <- as.POSIXct(mta$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mta, "5000 samples/before_sample_2500_b.csv", sep = ";", col.names = F, dateTimeAs = "write.csv")

# during
mt_dur <- fread("xac.csv", nrows = 194600)
mt <- mt_dur[sample(.N, 5000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/during_sample_5000_a.csv", sep = ";", col.names = T, dateTimeAs = "write.csv")

mt <- mt_dur[sample(.N, 5000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/during_sample_5000_b.csv", sep = ";", col.names = T, dateTimeAs = "write.csv")

mt <- mt_dur[sample(.N, 5000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/during_sample_5000_c.csv", sep = ";", col.names = T, dateTimeAs = "write.csv")

# after
mt <- fread("xad.csv")
mt <- mt[d1500,..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/xad_sample_1500.csv", sep = ";", col.names = T, dateTimeAs = "write.csv")

mt <- fread("xae.csv")
mt <- mt[sample(.N, 2600),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/xae_sample_2500b.csv", sep = ";", col.names = F, dateTimeAs = "write.csv")

# because there are error in files -> files are one huge mess. 
mt <- fread("sed 's/\\0//g' xaf.csv")
mt <- mt[sample(.N, 1500),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/xaf_sample_1500.csv", sep = ";", col.names = F, dateTimeAs = "write.csv")

mt <- fread("xag.csv")
mt <- mt[sample(.N, 1000),..columns_to_use]
mt$created_at <- as.POSIXct(mt$created_at, format = "%a %b %e %H:%M:%S %z %Y", tz="EST")
fwrite(mt, "5000 samples/xag_sample_1000.csv", sep = ";", col.names = F, dateTimeAs = "write.csv")

