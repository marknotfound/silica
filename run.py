from silica import Silica
from silica import handlers

app = Silica()

app.attach('generate-flask', handlers.GenerateFlaskHandler)
app.run()
