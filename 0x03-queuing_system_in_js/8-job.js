
function createPushNotificationsJobs(jobs, queue) {
    if(!Array.isArray(jobs)){
        throw new Error("Jobs is not an array");
    }
    jobs.forEach(Job=>{
        const newJob = queue.create('push_notification_code_3', Job).save((err)=>{
            if (!err)
            console.log('Notification job created: ', newJob.id)
    })
    newJob.on('complete', ()=> console.log(`Notification job ${newJob.id} completed`))
    newJob.on('failed', (err)=> console.log(`Notification job ${newJob.id} failed: ${err}`))
    newJob.on('progress',(progress)=> console.log(`Notification job ${newJob.id} ${progress}% complete`))
});
}