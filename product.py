import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='minha_fila')

message = 'Olá !!!!'
channel.basic_publish(exchange='', routing_key='minha_fila', body=message)



connection.close()
