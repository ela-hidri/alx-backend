const kue = require('kue');
const queue = kue.createQueue();

// Remove all jobs in the queue
queue.active((err, ids) => {
    ids.forEach(id => {
        kue.Job.get(id, (err, job) => {
            if (err) return console.error(`Error getting job ${id}: ${err}`);
            job.remove(() => {
                console.log(`Removed job ${id}`);
            });
        });
    });
});

queue.inactive((err, ids) => {
    ids.forEach(id => {
        kue.Job.get(id, (err, job) => {
            if (err) return console.error(`Error getting job ${id}: ${err}`);
            job.remove(() => {
                console.log(`Removed job ${id}`);
            });
        });
    });
});

queue.complete((err, ids) => {
    ids.forEach(id => {
        kue.Job.get(id, (err, job) => {
            if (err) return console.error(`Error getting job ${id}: ${err}`);
            job.remove(() => {
                console.log(`Removed job ${id}`);
            });
        });
    });
});

queue.failed((err, ids) => {
    ids.forEach(id => {
        kue.Job.get(id, (err, job) => {
            if (err) return console.error(`Error getting job ${id}: ${err}`);
            job.remove(() => {
                console.log(`Removed job ${id}`);
            });
        });
    });
});
