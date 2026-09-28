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

"""
#Questão 1 - Lista de tarefas

r.rpush('fila', 'atividade-orm')
r.lpop('fila')
print(r.lrange('fila', 0, -1))


#Questão 2 - Ranking 

r.zadd('ranking', {'Miguel': 500, 'Pedro': 320})
#r.zrem('ranking', 'Dante')
r.zincrby('ranking', 50, 'Miguel')
print(r.zrevrange('ranking', 0, 4, withscores=True))

#Questão 3 - Contador
def contador_pagina():
    contador = r.incr('contador')
    if contador == 1:
        r.expire('contador', 10)
    print(contador)

contador_pagina()
"""

#Questão 4 - Sistema de amigos online

r.sadd('usuarios_online', 'Robert: 401')
#print(r.srem('usuarios_online'))
print(r.smembers('usuarios_online'))
