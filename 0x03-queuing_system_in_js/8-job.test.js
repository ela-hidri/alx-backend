import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';

describe("createPushNotificationsJobs suite", function(){
    const queue = kue.createQueue();

    const list = [{
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    }];    
    before(() => queue.testMode.enter());
    afterEach(() => queue.testMode.clear());
    after(() => queue.testMode.exit());

    it("should validate jobs inside the queue", function(){
        createPushNotificationsJobs(list, queue);
        expect(queue.testMode.jobs.type).to.equal(Array);
    })
})
