import twint

# Configure
user = "NicolasMaduro"
c = twint.Config()
c.Search = user
c.Since = "2021-03-01"
c.Until = "2021-03-15"
c.Store_csv = 'TRUE'
c.Output = str(user)+".csv"

# Run
twint.run.Search(c)