import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';

const queue = kue.createQueue();

const list = [{
	phoneNumber: '4153518780',
	message: 'This is the code 1234 to verify your account'
}];
describe("createPushNotificationsJobs suite", function(){
    it("should validate jobs inside the queue", function(){
        queue.testMode.enter();
        createPushNotificationsJobs(list, queue);
        expect(queue.testMode.jobs.type).to.equal(Array);
        queue.testMode.clear();
        queue.testMode.exit();

    })
})
