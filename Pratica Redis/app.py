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

#Questão 4 - Sistema de amigos online


while True:
    menu = input("O que você quer fazer (1 - Fazer Login, 2 - Verificar usuários online, 3 - Fazer Logout, 4 - Desligar): ")
    if menu == "1":
        login = input("Digite seu ID: ")
        r.sadd('usuarios_online', login)
    elif menu == "2":
        print(r.smembers('usuarios_online'))
    elif menu == "3":
        logout = input("Digite o seu ID: ")
        r.srem('usuarios_online', logout)
    elif menu == "4":
        break
    else:
        print("Opção inválida")


print(r.smembers('usuarios_online'))

#Questão 5 - Contador de acessos
usuario = "403"
chave = f"rate_limit:{usuario}"
requisicoes = r.incr(chave)

if requisicoes == 1:
    r.expire(chave, 60)

if requisicoes > 10:
    print(f"Acesso bloqueado! Tente novamente em {r.ttl(chave)}")
else:
    print(f"Ação permitida.")
"""

#Questão 6 - Operações com conjuntos
r.sadd('usuario:seguidores', '402', '401', '004', '510')
r.sadd('usuario:seguindo', '402', '004', '404')
print(f"Total seguindo no começo: {r.smembers('usuario:seguindo')}")


amigos_comum = r.sinter('usuario:seguidores', 'usuario:seguindo')
print(f"Amigos em comum: {amigos_comum}")

contato_unico = r.sunion('usuario:seguidores', 'usuario:seguindo')
print(f"Contatos unicos: {contato_unico}")

seguindo_dif = r.sdiff('usuario:seguindo', 'usuario:seguidores')
print(f"Você segue mas não te segue de volta: {seguindo_dif}")

r.srem('usuario:seguindo', '404')
print(f"Total seguindo no final: {r.smembers('usuario:seguindo')}")
