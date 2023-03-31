# use ps aux to view running processes (will show up as python3)
# use kill to end processes

nohup python3 src/worker.py &
nohup python3 src/bot.py &