"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='cats-hydrant-juice-83664.db.redis.io',
    port=12254,
    decode_responses=True,
    username="default",
    password="qb5Oo2NDR97EL53n8qsa2kaEdFtm0k3L",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

#Questão 1 - Lista de tarefas
"""

r.rpush('fila', 'Tarefa2 Jales')
#r.rpop('fila')
print(r.lrange('fila', 0, -1))


#Questão 2 - Ranking 

r.zadd('ranking', {'Dante': 810, 'Samuel': 900})
print(r.zrange('ranking', 0, -1, withscores=True))


#Questão 3 - Contador

contador = r.incr('contador')
print(contador)
"""