cd app/
# Start rasa server with nlu model
rasa run actions  & rasa run --model models --enable-api --cors "*" --debug -p 5005