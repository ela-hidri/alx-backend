const kue = require('kue');
const queue = kue.createQueue();

const blacklist = [4153518780, 4153518781]

function sendNotification(phoneNumber, message, job, done){
    job.progress(0, 100);

    if (blacklist.includes(phoneNumber)){
        job.failed().error(new Error(`Phone number ${phoneNumber} is blacklisted`));
        done();
    }
    else{
        job.progress(0, 50);
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    }
}

queue.process('push_notification_code_2', 2,(job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
    done();
})
