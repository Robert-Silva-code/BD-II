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

r.set('nome', 'Robert')
r.set('contador', 10)
r.decrby('contador')

print(r.get('nome'))
print(r.exists('nome'))
print(r.get('contador'))
