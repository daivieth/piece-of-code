
install.packages('jsonlite')

library('jsonlite')
tick = 'AAPL'

c <- fromJSON(paste("https://api-v2.intrinio.com/companies/",tick,"?api_key=OjcxNWQ0Mjc0ZTA3NGU5OTNiNzZlYTM2MDdiZTQ5MzEx") )
c[8]
