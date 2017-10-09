library(rtweet)
library(RMariaDB)

con <- dbConnect(RMariaDB::MariaDB(), dbname = "sawi_tweets", user="root")

appname <- "rwtsafjjkhuouj"

## api key (example below is not a real key)
key <- "nBFl2Ruc4c8kXtsRD3QC7SP9q"

## api secret (example below is not a real key)
secret <- "mjCACAd5uDOqLVy8ru6MIFNcFCuXCdDeXR7VQNsXWJJZ4t489f"

## create token named "twitter_token"
twitter_token <- create_token(
  app = appname,
  consumer_key = key,
  consumer_secret = secret)

newesttweets <- lists_statuses(owner_user="ChillinQuillen", slug="Apple", token=twitter_token)
max_id_newesttweets = newesttweets[1,2]

since_id_asd <- asd[1,2]
asd <- lists_statuses(owner_user="ChillinQuillen", slug="Apple", token=twitter_token, 
                      max_id= max_id_newesttweets, since_id = since_id_asd)


dbWriteTable(conn = con, "sawi_tweets_R", asd, append=TRUE)


a <- stream_tweets("iphoneX", timeout = 30, parse = FALSE,
              file_name = "twee1")

#http://rtweet.info/articles/intro.html
## stream 3 random samples of tweets
for (i in seq_len(3)) {
  stream_tweets(q = "iphoneX", timeout = 60,
                file_name = paste0("rtw", i), parse = FALSE)
  if (i == 3) {
    message("all done!")
    break
  } else {
    # wait between 0 and 300 secs before next stream
    Sys.sleep(runif(1, 0, 300))
  }
}

## parse the samples
tw <- lapply(c("rtw1.json", "rtw2.json", "rtw3.json"),
             parse_stream)

## collapse lists into single data frame
tw.users <- do.call("rbind", users_data(tw))
tw <- do.call("rbind", tw)
attr(tw, "users") <- tw.users

## preview data
head(tw)
users_data(tw) %>%
  head()




