url = 'https://www.ihavenet.com/Basketball/NBA-Basketball-All-Time-Scoring-Leaders.html'

df = pd.read_html(url)

df = df[0] #grabbing the first list of the url 

df["Player"] = df['Player'].str.upper() #adding upper to every player name

df = df.drop(31) #dropping row 31

df['Points'] = df['Points'].astype(int)  #chaning the points data type from object to integer

df['Points'] =  df.Points.apply(lambda x : "{:,}".format(x)) #inser comma as thousand separator

df.head()
