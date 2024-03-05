import { createClient } from 'redis';

const client = createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.error('Redis client not connected to the server: ', err);
});

client.subscribe('holberton school channel')

client.on('message', (channel, message) => {
    if (message == 'KILL_SERVER')
        client.ununsubscribe('holberton school channel');
    else
        console.log(message);
  });
