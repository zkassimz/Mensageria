import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='minha_fila')


def process_message(ch, method, properties, body):
    print("Mensagem recebida:", body.decode('utf-8'))


channel.basic_consume(queue='minha_fila', on_message_callback=process_message, auto_ack=True)

print('Aguardando mensagens...')
channel.start_consuming()
