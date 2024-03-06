const redis = require("redis")
const kue = require('kue');
const express = require('express')

const app = express();
const port = 1245

const client = redis.createClient();
const queue = kue.createQueue();

const getAsync = promisify(client.get).bind(client);
let reservationEnabled

function reserveSeat(number) { 
    client.set('available_seats', number)
}

function getCurrentAvailableSeats(){
    return getAsync('available_seats')
}

app.get('/available_seats', async(req, res)=>{
    getCurrentAvailableSeats().then((seats)=>{
        res.json({"numberOfAvailableSeats":seats})
    })
})

app.get('/reserve_seat', (req, res)=>{
    if (!reservationEnabled)
    {
        return res.json({ "status": "Reservation are blocked" })
    }else{
        const job = queue.create('reserve_seat', { task: 'reserve a seat' }).save((err)=>{
            if (!err){
                res.json({ "status": "Reservation in process" })
            }
            else{
                res.json({ "status": "Reservation failed" })
            }
        })
        job.on('complete', ()=> console.log(`Seat reservation job ${newJob.id} completed`))
        job.on('failed', (err)=> console.log(`Seat reservation job job ${newJob.id} failed: ${err}`))
    }
})
app.get('/process', async(req, res)=>{
    res.json({ status: 'Queue processing' });
    queue.process('reserve_seat', async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    availableSeats -= 1;
    reserveSeat(availableSeats);
    if (availableSeats >= 0) {
      if (availableSeats === 0) reservationEnabled = false;
      done();
    }
    done(new Error('Not enough seats available'));
  });
})

app.listen(port, () => {
    reserveSeat(50);
    reservationEnabled = true;
  });
