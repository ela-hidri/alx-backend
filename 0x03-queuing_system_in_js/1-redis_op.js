import { createClient } from 'redis';
const redis = require("redis")
const client = createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.error('Redis client not connected to the server: ', err);
});

function setNewSchool(schoolName, value){
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName){
    client.get(schoolName, (err, value) => {
        console.log(value)
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
